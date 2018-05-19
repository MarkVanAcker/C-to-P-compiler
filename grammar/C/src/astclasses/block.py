from src.astclasses.AST import *


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
            child.handle(self.symbtable)


class EmptyNode(ASTNode):
    def handle(self,st):
        pass


class ArrayCallNode(ASTNode):
    def handle(self,st, type = None):
        self.getchild(0).handle(st)