from src.astclasses.AST import *
from src.astclasses.atomictypes import *

class BlockNode(ASTNode):
    #check if variable that is to be returned exists and matches return type
    def handle(self, st):
        self.symbtable = st
        for child in self.children:
            child.handle(self.symbtable)



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

        foundmain = False

        functions = {}

        globals = {}


        for globalvar in globals:
            code.AddInstruction(globalvar.getCode(self.symbtable))
        
