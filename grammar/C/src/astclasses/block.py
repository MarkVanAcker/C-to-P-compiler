from src.astclasses.AST import *
from src.astclasses.functions import *
from src.astclasses.declaration import *

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
        





class EmptyNode(ASTNode):
    def handle(self,st):
        pass


class ArrayCallNode(ASTNode):
    def handle(self,st, type = None):
        self.getchild(0).handle(st)