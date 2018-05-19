from src.astclasses.AST import *


class BlockNode(ASTNode):
    #check if variable that is to be returned exists and matches return type
    def handle(self, st):
        for child in self.children:
            child.handle(self.st)



class RootNode(ASTNode):
    def handle(self,st):
        for child in self.children:
            child.handle(self.st)


class EmptyNode(ASTNode):
    def handle(self,st):
        pass