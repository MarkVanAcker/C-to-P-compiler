from build.CParser import CParser
from build.CLexer import CLexer
from src.parser.AST import ASTNode
from src.parser.SymbolTable import *
from copy import deepcopy
from src.parser.traverser import AstVisitor
from src.error.Error import SemanticsError
from src.error.Warning import Warning

class TypeClass:
    INTEGER = 1
    FLOAT = 2
    CHAR = 3
    VOID = 4


typecast = { CLexer.INTEGER : TypeClass.INTEGER , CLexer.CHARACTER : TypeClass.CHAR, CLexer.DECIMAL : TypeClass.FLOAT ,
             CLexer.VOID: TypeClass.VOID,CLexer.INT : TypeClass.INTEGER, CLexer.FLOAT : TypeClass.FLOAT, CLexer.CHAR : TypeClass.CHAR}



#TODO: split up in different files


class DeclarationNode(ASTNode):


    #maybe rewrite init to make it easier to process
    def handle(self, st):


        type = self.getchild(0)
        entr = Entry()

        if (type.token.type == CParser.CONST):
            entr.const = True
            entr.type = typecast[type.getchild(0).token.type]
        else:
            entr.type = typecast[type.token.type]


        if self.getchild(1).name == '=':
            entr.name = self.getchild(1).getchild(0).name
        else:
            entr.name = self.getchild(1).name


        if (st.LocalTableLookup(entr)):
            raise SemanticsError(self.token,"This variable was already declared in the local scope")
        if (st.GlobalTableLookup(entr)):
            #TODO : make general warning function that uses tokens and scope
            Warning(self.token,"Variable is hiding data")

        st.addEntry(entr)
        if self.getchild(1).name == '=':
            self.getchild(1).handle(st) #assignment visit


        return entr

class IDNode(ASTNode):
    def handle(self, entr, type=None,):

        if type is not None:
            TypeCheck(self,entr,type)
            return


        if self.Typedcl == "id":
            if entr.type == 4:
                raise SemanticsError(self.token,"Declared variable void")
            entr.name = self.name
            return

        elif self.Typedcl == "func":

            entr.func = True
            entr.name = self.name
            if(len(self.children) == 0):
                entr.params = []

            else:
                entr.params = self.getchild(0).handle()

        elif self.Typedcl == "array":
            entr.name = self.name
            for child in reversed(self.children):
                #TODO: typecheck child.name and see scopecheck (if child.name == var)
                entr.type = "array("+child.name +","+ str(entr.type) + ")"
            return

        elif self.name == "pointer":
            entr.ptr = True
            self.getchild(0).handle(entr)
            return


        else:
            self.getchild(0).handle(entr)
            return


class ParamNode(ASTNode):
    def handle(self,st = None):
        paramlist = []
        for child in self.children:
            if(child.name == "paramdecl"):
                paramlist.append(typecast[child.getchild(0).token.type])

            else:
                paramlist.append(typecast[child.token.type])

        return paramlist


class FunctionDefinitionNode(ASTNode):
    def handle(self, st):

        # delcartion visitor should throw if name is already in use (pass redeclarations)
        # TODO: delcare and after define function
        self.getchild(0).getchild(1).addchild(self.getchild(1))
        self.getchild(0).handle(st) #declaration visit

        for param in reversed(self.getchild(1).children):
            if param.name == "empty":
                continue
            self.getchild(2).children.insert(0, param)



        newst = SymbolTable()
        newst.name = self.getchild(0).getchild(1).name

        st.addchild(newst)
        v = AstVisitor(self.getchild(2), newst)

        v.traverse()


class ConditionNode(ASTNode):
    #typecheck condition and validity
    def handle(self,st):
        return self.getchild(0).handle(st) #expression visit

class WhileNode(ASTNode):

    #typecheck condition and validity
    def handle(self, st):
        #
        #  - validate condition
        #  - create new table and traverse block
        #

        # condition vist will validate and detect possible dead block code
        #TODO check if functionallity can be added
        if not self.getchild(1).handle(st): #conditionvisit
            pass


        newst = SymbolTable()
        newst.name = "iteration"

        st.addchild(newst)
        v = AstVisitor(self.getchild(1), newst)
        v.traverse()


class ReturnNode(ASTNode):
    #check if variable that is to be returned exists and matches return type
    def handle(self, st):
        stFunc = st.getFuncRoot()
        if stFunc.parent == None:
            raise SemanticsError(self.token,"Return in a non definition block")


        stParent = stFunc.parent
        returnType = ''
        funcReturnType = stParent.getVariableEntry(stFunc.name).type
        if len(self.children) == 0:
            # void return
            returnType = 4
            if funcReturnType!= 4:
                SemanticsError(self.token,"Expected void return but got another type")
        else:
            returnType = self.getchild(0).handle(st, funcReturnType) #expression statement



#check if every variable that is used exists and do type checking for conversions
#also add constant folding

class ExpressionNode(ASTNode):

    def handle(self, st, type = None):

        if self.name == 'empty' or len(self.children) == 0:
            return 4


        #
        # HANDLE LEFT VALUE OF THE EXPRESSION
        #


        # no L-value to assign to OR no type reference on the left side.   EG  if(3 < 5.0)
        node = self.getchild(0)
        if type == None:
            # variable
            if node.Typedcl == 'id':
                entry = st.getVariableEntry(node.name)
                if entry == False:
                    raise Exception("Error: undeclared varaible (first use in this function)")
                type = entry.type

            # constant value (right?)
            else:
                type = typecast[node.token.type]

        # supertype given for the expression.    EG int var = 1 + 5;
        # typecheck left operant
        else:
            TypeCheck(node,st,type)


        if len(self.children) == 1:
            return type

        #
        # HANDLE RIGHT VALUE OF THE EXPRESSION
        #

        node = self.getchild(1)
        if node.Typedcl == 'id' or node.Typedcl == 'intconst' or node.Typedcl == 'floatconst' or node.Typedcl == 'charconst':
            TypeCheck(node,st,type)
        else:
            node.handle(st,type) #expression visit

        return type


class AssignmentNode(ASTNode):
    #check if L-value and R-value are ok
    def handle(self, st):
        # left side must be l-value
        # is l-value memory allocatable variable only (array included)
        entry = st.getVariableEntry(self.getchild(0).name)
        if entry is None:
            raise Exception("Error: undeclared varaible (first use in this function)")
        returnType = entry.type

        # Evaluate R-value with given l-value type
        self.getchild(1).handle(st, returnType) #expression visit


class ConstantNode(ASTNode):

    def handle(self,st,type=None):
        if type is not None:
            TypeCheck(self,st,type)


#TODO: actual conversion, right now its just setting the type to x

def TypeCheck(node, st, type):
    # variable
    #node = node.getchild(0)
    if node.Typedcl == 'id':
        entry = st.getVariableEntry(node.name)
        if entry is None:
            raise SemanticsError(node.token,"undeclared varaible (first use in this function)")
        Ltype = entry.type
        if not Ltype == type: # keeping void for what it is
            if type == 1: # void ?
                Warning(node.token,"Converting to int")
                entry.type = 1
            elif type == 2:
                Warning(node.token,"Converting to float")
                entry.type = 2
            elif type == 3:
                Warning(node.token,"Converting to char")
                entry.type = 3

    # constant value (right?)
    else:
        Ltype = typecast[node.token.type]
        if not Ltype == type: # keeping void for what it is
            Warning(node.token,"forced type conversion")
            if type == TypeClass.INTEGER:
                Warning(node.token, "Converting to int")
                node.Typedcl = 'intconst'
                node.name = int(node.name)
            elif type == TypeClass.FLOAT:
                Warning(node.token, "Converting to float")
                node.Typedcl = 'floatconst'
                node.name = float(node.name)
            elif type == TypeClass.CHAR:
                Warning(node.token, "Converting to char")
                node.Typedcl = 'charconst'
                node.name = str(node.name)


'''


declaration v
function definition v
while
condition
return
funccall
array
operators
access
include

'''
