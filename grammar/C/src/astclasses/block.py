from src.astclasses.AST import *
from src.astclasses.atomictypes import *

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
        for child in self.children:
            if isinstance(child,FunctionDefinitionNode) or isinstance(child,DeclarationNode):
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
        
