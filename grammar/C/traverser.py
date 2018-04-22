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


    #TODO: refactor
    def handle(self, currstate):
        if (currstate.name == "declaration"):
            dv = declarationVisitor()
            dv.visit(currstate,self.st)

            return

    def traverse(self):
        for child in self.root.children:
            self.handle(child)





class declarationVisitor:

    def __init__(self):
        pass

    def visit(self,ctx,st):


        type = ctx.getchild(0)
        entr = Entry()

        if (type.token.type == CParser.CONST):
            entr.const = True
            entr.type = typecast[type.getchild(0).token.type]
        else:
            entr.type = typecast[type.token.type]

        name = ctx.getchild(1)
        self.handleID(name,entr)

        if (st.LocalTableLookup(entr)):
            raise Exception("This variable was already declared in the local scope")
        if (st.GlobalTableLookup(entr)):
            #TODO : make general warning function that uses tokens and scope
            print("Warning: Variable is hiding data")

        st.addEntry(entr)


    def handleID(self, idnode,entr):
        if idnode.Typedcl == "id":
            entr.name = idnode.name
            return

        elif idnode.Typedcl == "func":
            entr.func = True
            entr.name = idnode.name
            if(len(idnode.children) == 0):
                entr.params = []

            else:
                entr.params = self.handleParams(idnode.getchild(0))

        elif idnode.name == "pointer":
            entr.ptr = True
            self.handleID(idnode.getchild(0),entr)
            return

        else:
            self.handleID(idnode.getchild(0), entr)
            return



    def handleParams(self,paramnode):
        paramlist = []
        for child in paramnode.children:
            if(child.name == "paramdecl"):
                paramlist.append(typecast[child.getchild(0).token.type])

            else:
                paramlist.append(typecast[child.token.type])

        return paramlist










""


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
