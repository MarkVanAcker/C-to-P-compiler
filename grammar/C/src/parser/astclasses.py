from build.CParser import CParser
from src.parser.AST import ASTNode
from src.parser.SymbolTable import *
from copy import deepcopy
from src.parser.traverser import AstVisitor

typecast = { 17 : 1 , 15 : 3, 16 : 2 , 21: 4}

class TypeClass:
    INTEGER = 1
    FLOAT = 2
    CHAR = 3
    VOID = 4




def declaration_visit(ctx,st):


    type = ctx.getchild(0)
    entr = Entry()

    if (type.token.type == CParser.CONST):
        entr.const = True
        entr.type = typecast[type.getchild(0).token.type]
    else:
        entr.type = typecast[type.token.type]

    name = ''
    if ctx.getchild(1).name == '=':
        name = ctx.getchild(1).getchild(1)
    else:
        name = ctx.getchild(1)

    handleID(name,entr)

    if (st.LocalTableLookup(entr)):
        raise Exception("This variable was already declared in the local scope")
    if (st.GlobalTableLookup(entr)):
        #TODO : make general warning function that uses tokens and scope
        print("Warning: Variable is hiding data")

    st.addEntry(entr)

    if ctx.getchild(1).name == '=':
        assignment_visit(ctx.getchild(1),st)

    return entr


def handleID( idnode,entr):
    if idnode.Typedcl == "id":
        if entr.type == 4:
            raise Exception("Error: Declared variable void")
        entr.name = idnode.name
        return

    elif idnode.Typedcl == "func":

        entr.func = True
        entr.name = idnode.name
        if(len(idnode.children) == 0):
            entr.params = []

        else:
            entr.params = handleParams(idnode.getchild(0))

    elif idnode.Typedcl == "array":
        entr.name = idnode.name
        for child in reversed(idnode.children):
            #TODO: typecheck child.name and see scopecheck (if child.name == var)
            entr.type = "array("+child.name +","+ str(entr.type) + ")"
        return

    elif idnode.name == "pointer":
        entr.ptr = True
        handleID(idnode.getchild(0),entr)
        return


    else:
        handleID(idnode.getchild(0), entr)
        return



def handleParams(paramnode):
    paramlist = []
    for child in paramnode.children:
        if(child.name == "paramdecl"):
            paramlist.append(typecast[child.getchild(0).token.type])

        else:
            paramlist.append(typecast[child.token.type])

    return paramlist



def functiondefinition_visit(ctx,st):

    # delcartion visitor should throw if name is already in use (pass redeclarations)
    # TODO: delcare and after define function
    ctx.getchild(0).getchild(1).addchild(ctx.getchild(1))
    declaration_visit(ctx.getchild(0),st)

    for param in reversed(ctx.getchild(1).children):
        if param.name == "empty":
            continue
        ctx.getchild(2).children.insert(0,param)



    newst = SymbolTable()
    newst.name = ctx.getchild(0).getchild(1).name

    st.addchild(newst)
    v = AstVisitor(ctx.getchild(2),newst)

    v.traverse()

#typecheck condition and validity
def condition_visit(ctx,st):
    return expression_visit(ctx.getChild(0),st)

#typecheck condition and validity
def while_visit(ctx,st):
    #
    #  - validate condition
    #  - create new table and traverse block
    #

    # condition vist will validate and detect possible dead block code
    #TODO check if functionallity can be added
    if not condition_visit(ctx.getchild(1),st):
        pass


    newst = SymbolTable()
    newst.name = "iteration"

    st.addchild(newst)
    v = AstVisitor(ctx.getchild(1),newst)
    v.traverse()



#check if variable that is to be returned exists and matches return type
def return_visit(ctx,st):

    stFunc = st.getFuncRoot()
    if stFunc.parent == None:
        raise Exception("Error: Return in a non definition block")


    stParent = stFunc.parent
    returnType = ''
    funcReturnType = stParent.getVariableEntry(stFunc.name).type
    if ctx.getChildCount() == 0:
        # void return
        returnType = 4
        if funcReturnType!= 4:
            Exception("Error: Expected void return but got another type")
    else:
        returnType = expression_statement(ctx.getChild(0),st,funcReturnType)
















#check if every variable that is used exists and do type checking for conversions
#also add constant folding

def itemCheck(ctx,st,type):
    # variable
    node = ctx.getchild(0)
    if node.Typedcl == 'id':
        entry = st.getVariableEntry(node.name)
        if entry == False:
            raise Exception("Error: undeclared varaible (first use in this function)")
        Ltype = entry.type
        if not Ltype == type: # keeping void for what it is
            if type == 1: # void ?
                raise Exception("Warning: Converting to int")
                entry.type = 1
            elif type == 2:
                raise Exception("Warning: Converting to float")
                entry.type = 2
            elif type == 3:
                raise Exception("Warning: Converting to char")
                entry.type = 3

    # constant value (right?)
    else:
        Ltype = typecast[node.token.type]
        if not Ltype == type: # keeping void for what it is
            raise Exception("Warning: forced type conversion")
            if type == 1: # void ?
                raise Exception("Warning: Converting to int")
                node.Typedcl = 'intconst'
                node.name = int(node.name)
            elif type == 2:
                raise Exception("Warning: Converting to float")
                node.Typedcl = 'floatconst'
                node.name = float(node.name)
            elif type == 3:
                raise Exception("Warning: Converting to char")
                node.Typedcl = 'charconst'
                node.name = str(node.name)

def expression_visit(ctx,st,type = None):

    if ctx.name == 'empty' or ctx.getChildCount() == 0:
        return 4;


    #
    # HANDLE LEFT VALUE OF THE EXPRESSION
    #


    # no L-value to assign to OR no type reference on the left side.   EG  if(3 < 5.0)
    node = ctx.getChild(0)
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
        itemCheck(node,st,type)


    if ctx.getChildCount() == 1:
        return type

    #
    # HANDLE RIGHT VALUE OF THE EXPRESSION
    #

    node = ctx.getChild(1)
    if node.Typedcl == 'id' or node.Typedcl == 'intconst' or node.Typedcl == 'floatconst' or node.Typedcl == 'charconst':
        itemCheck(node,st,type)
    else:
        expression_visit(node,st,type)

    return type



#check if L-value and R-value are ok
def assignment_visit(ctx,st):
    # left side must be l-value
    # is l-value memory allocatable variable only (array included)
    entry = st.getVariableEntry(ctx.getchild(1).name)
    if entry == False:
        raise Exception("Error: undeclared varaible (first use in this function)")
    returnType = entry.type

    # Evaluate R-value with given l-value type
    expression_visit(ctx.getChild(2),st,returnType)






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
