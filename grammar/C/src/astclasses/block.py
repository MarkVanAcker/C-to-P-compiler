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

            child.handle(self.symbtable) # should be ok or semantic will pop up


    def getCode(self):
        pass



class RootNode(ASTNode):
    def handle(self,st):
        self.symbtable = st
        for child in self.children[:]: # traverse
            child.symbtable = st
            if isinstance(child,FunctionDefinitionNode) or isinstance(child,IncludeNode):
                child.handle(self.symbtable)
            elif isinstance(child,DeclarationNode):
                child.handle(self.symbtable)
            else:
                raise SemanticsError(child.getToken(), "Invalid statement in global scope")

    def getCode(self):

        code = InstructionList()

        functions = []

        globals = []

        for child in self.children:
            if isinstance(child,DeclarationNode):
                globals.append(child)

        #make place for all the global variables
        code.AddInstruction(SetPointers(0,self.symbtable.getRequiredSpace()))

        self.symbtable.setupParameters(code)

        for globalvar in globals:
            code.AddInstruction(globalvar.getCode(self.symbtable))





        code.AddInstruction(Halt)


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


