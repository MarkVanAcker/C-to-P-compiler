from src.astclasses.AST import *
from src.astclasses.atomictypes import *
from src.parser.SymbolTable import *

class BlockNode(ASTNode):
    #check if variable that is to be returned exists and matches return type
    def handle(self, st):
        self.symbtable = st
        for child in self.children:
            child.handle(self.symbtable)


    def getCode(self):
        pass



class RootNode(ASTNode):
    def handle(self,st):
        self.symbtable = st
        for child in self.children: # traverse
            if isinstance(child,FunctionDefinitionNode) or isinstance(child,DeclarationNode) or isinstance(child,IncludeNode):
                child.handle(self.symbtable)
            else:
                raise SemanticsError(self.token, "Invalid statement in global scope")

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
        print("adding stdio into global scope")
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

        
