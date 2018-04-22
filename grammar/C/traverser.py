from SymbolTable import *
from AST import *
from CParser import CParser

typecast = { 17 : 1 , 15 : 3, 16 : 2 , 21: 4}

class TypeClass:
    INTEGER = 1
    FLOAT = 2
    CHAR = 3
    VOID = 4

class AstVisitor:
    def __init__(self,root,st):
        self.root = root
        self.st = st

    def handle(self, curstate = None):
        pass

    def traverse(self):
        for child in self.root.children:
            res = self.lookup(child)
            self.handle(child,res)





class declarationVisitor:

    def visit(self,ctx,st):



        type = ctx.getchild(0)
        entr = Entry()
        
        
        if (type.token.type == CParser.CONST):
            entr.const = True
            entr.type = typecast[type.getchild(0).token.type]
        else:
            entr.type = typecast[type.token.type]
            
        name = ctx.getchild(1)
        n = self.handleID(name)


    def handleID(self, idnode):
        if idnode.Typedcl == "id":
            return idnode.name

        elif idnode.:
            if id
        











'''

include
declaration
function definition
while
condition
return
funccall
array
operators
access


'''
