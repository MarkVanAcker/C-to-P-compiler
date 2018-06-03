from src.astclasses.AST import *
from src.astclasses.atomictypes import *
from src.parser.SymbolTable import *
from src.astclasses.expression import *
from src.astclasses.statements import *

class BlockNode(ASTNode):


    #check if variable that is to be returned exists and matches return type
    def handle(self, st):
        self.symbtable = st

        returnfound = False
        childidx = 0
        while childidx < len(self.children):
            child = self.children[childidx]
            child.symbtable = st
            if returnfound: # removing useless or dead code after return
                child.par = None
                self.children.remove(child)
                continue
            if isinstance(child,ReturnNode):
                returnfound = True

            child.handle(self.symbtable) # should be ok or semantic will pop up

            #check if the handle resulted in a fold. In case of a fold becoming a clearly useless statement we can remove it
            child = self.children[childidx]
            if isinstance(child,IDNode) or isinstance(child,ConstantNode):
                self.children.remove(child)
                continue

            childidx += 1




    def getCode(self):
        ins = InstructionList()

        for child in self.children:
            ins.AddInstruction(child.getCode())

            #clear memory when unused
            if isinstance(child,ExpressionNode):
                #write garbage to address 0
                ins.AddInstruction(StoreAbsolute(child.type,0))
            elif isinstance(child,FunctionCallNode):
                ins.AddInstruction(StoreAbsolute(child.entry.type,0))

        return ins


class RootNode(ASTNode):
    def handle(self,st):
        self.symbtable = st
        childidx = 0
        currlen = len(self.children)
        while childidx < len(self.children): # traverse
            child = self.children[childidx]
            child.symbtable = st
            if isinstance(child,FunctionDefinitionNode) or isinstance(child,IncludeNode):
                child.handle(self.symbtable)
            elif isinstance(child,DeclarationNode):
                child.handle(self.symbtable)

                #if a function declaration node was deleted continue the loop without incrementing
                if(len(self.children) < currlen):
                    currlen = len(self.children)
                    continue

            else:
                raise SemanticsError(child.getToken(), "Invalid statement in global scope")

            childidx += 1

        for ent in st.entries:
            if ent.func == True and ent.defined == False:
                raise SemanticsError(None,"Linking error, function not defined: " + ent.name)

        for ent in st.entries:
            if ent.func == True and ent.defined == False:
                raise SemanticsError(None,"Linking error, function not defined: " + ent.name)

        for ent in st.entries:
            if ent.func == True and ent.name == "main" and ent.defined:
                return
            if ent.func == True and ent.name == "main" and not ent.defined:
                raise SemanticsError(None, "Function main not defined")
        raise SemanticsError(None,"No main function found")

    def getCode(self):

        self.symbtable.variablestacksize = 1

        code = InstructionList()

        functions = []

        globals = []

        for child in self.children:
            if isinstance(child,DeclarationNode):
                globals.append(child)

            elif isinstance(child, FunctionDefinitionNode):
                functions.append(child)

        #make place for all the global variables
        code.AddInstruction(SetStackPointer(self.symbtable.getGlobalSpace()))

        for globalvar in globals:
            code.AddInstruction(globalvar.getCode())


        code.AddInstruction(MarkStack(0))

        code.AddInstruction(CallUserProcedure(0,Label("function_main")))

        code.AddInstruction(Halt())

        for function in functions:
            code.AddInstruction(function.getCode())


        return code


class IncludeNode(ASTNode):
    def handle(self,st : SymbolTable):

        self.symbtable = st

        if st.parent is not None:
            raise SemanticsError(self.getchild(0).token,"Inlcude statement in non global scope")

        #ent = Entry('printf')
        #ent.func = True
        #ent.defined = True
        #ent.type = IntegerType()
        #ent.defined = True
        #ent.params = [CharacterType(), AnyType()]
#
        #ent2 = Entry('scanf')
        #ent2.func = True
        #ent2.defined = True
        #ent2.type = IntegerType()
        #ent2.defined = True
        #ent2.params = [CharacterType(), AnyType()]


        st.io = True


