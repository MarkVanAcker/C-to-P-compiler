from src.parser.AST import *
from src.code_generation.environment import *



#class that will traverse our decorated AST and generate code accordingly
#TODO: make big if for all possible statements
#TODO: make big if for functioncalls etc

class CodegenTraverser:

    def __init__(self,root :ASTNode):
        self.node = root
        self.env = Environment({})
        self.address = 4
        self.env.readSymbolTable(self.root.symboltable,self.address)
        #All globale inlezen

