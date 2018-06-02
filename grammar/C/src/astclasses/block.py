from src.astclasses.AST import *
from src.astclasses.atomictypes import *
from src.parser.SymbolTable import *
from src.astclasses.expression import *

class BlockNode(ASTNode):


    #check if variable that is to be returned exists and matches return type
    def handle(self, st):
        self.symbtable = st

        returnfound = False

        for child in self.children[:]:
            child.symbtable = st
            if returnfound: # removing useless or dead code after return
                child.par = None
                self.children.remove(child)
                continue
            if isinstance(child,ReturnNode):
                returnfound = True

            if isinstance(child,IDNode) or isinstance(child,ConstantNode) or isinstance(child,ExpressionNode):
                self.children.remove(child)
                continue

            child.handle(self.symbtable) # should be ok or semantic will pop up



    def getCode(self):
        pass


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

    def getCode(self):

        self.symbtable.variablestacksize = 0

        code = InstructionList()

        functions = []

        globals = []

        for child in self.children:
            if isinstance(child,DeclarationNode):
                globals.append(child)

            elif isinstance(child, FunctionDefinitionNode):
                functions.append(child)

        #make place for all the global variables
        code.AddInstruction(SetStackPointer(self.symbtable.getRequiredSpace()))

        for globalvar in globals:
            code.AddInstruction(globalvar.getCode())


        code.AddInstruction(Halt())

        return code


class IncludeNode(ASTNode):
    def handle(self,st : SymbolTable):

        self.symbtable = st

        if st.parent is not None:
            raise SemanticsError(self.getchild(0).token,"Inlcude statement in non global scope")

        ent = Entry('printf')
        ent.func = True
        ent.defined = True
        ent.type = IntegerType()
        ent.defined = True
        ent.params = [CharacterType(), AnyType()]

        ent2 = Entry('scanf')
        ent2.func = True
        ent2.defined = True
        ent2.type = IntegerType()
        ent2.defined = True
        ent2.params = [CharacterType(), AnyType()]

        st.addEntry(ent)
        st.addEntry(ent2)


