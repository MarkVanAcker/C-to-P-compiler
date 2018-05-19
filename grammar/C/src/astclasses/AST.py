from src.parser.SymbolTable import *
from build.CLexer import *
from build.CParser import *
from src.util.Instructionlist import *
from src.parser.traverser import AstVisitor
from src.error.Error import SemanticsError
from src.error.Warning import Warning

#utils

class TypeClass:
    INTEGER = 1
    FLOAT = 2
    CHAR = 3
    VOID = 4


typecast = { CLexer.INTEGER : TypeClass.INTEGER , CLexer.CHARACTER : TypeClass.CHAR, CLexer.DECIMAL : TypeClass.FLOAT ,
             CLexer.VOID: TypeClass.VOID,CLexer.INT : TypeClass.INTEGER, CLexer.FLOAT : TypeClass.FLOAT, CLexer.CHAR : TypeClass.CHAR}





class ASTNode:
    def __init__(self,n="root",t=None):
        self.par = None
        self.children = []
        self.name = n
        self.token = t
        self.Typedcl = None
        self.symbtable = None

    def todot(self,file):

        file.write("\tNODE" + str(id(self)) + "[label=<" +self.getstr() + "> shape=box];\n")
        if(self.par is not None):
            file.write("\tNODE"+str(id(self.par))+"->NODE"+str(id(self))+"\n")
        for child in self.children:
            child.todot(file)


    def addchild(self,c):
        if c.name == "empty statement":
            return
        c.par = self
        self.children.append(c)


    def addchildren(self,c):
        for child in c:
            self.addchild(child)


    def getstr(self):
        if self.Typedcl is None:
            return self.__class__.__name__
        else:
            return "<font color = \"blue\">" +str(self.Typedcl) +"</font><br/>"+ self.__class__.__name__


    def getchild(self,idx):
        return self.children[idx]


    def clearchildren(self):
        self.children = []


    def hasChild(self):
        if(len(self.children) == 0):
            return False
        else:
            return True


    def handle(self,st):
        pass

    def getCode(self, env:SymbolTable):
        pass

    def getLValue(self, env:SymbolTable):
        pass

    




def ToDotAST(root):
    import os
    if not os.path.exists('./output'):
        os.makedirs('./output')

    file = open("./output/.AST.dot","w")

    file.write('''digraph G
{
    nodesep = 0.4;
    ranksep = 0.5;
''')


    root.todot(file)



    file.write('}')

    file.close()







#TODO: actual conversion, right now its just setting the type to x

def TypeCheck(node, st, type):
    # variable
    #node = node.getchild(0)
    if node.Typedcl == 'id':
        entry = st.getVariableEntry(node.name)
        if entry is None:
            raise SemanticsError(node.token,"undeclared varaible (first use in this function)")
        Ltype = entry.type
        if not Ltype == type: # keeping void for what it is
            if type == 1: # void ?
                Warning(node.token,"Converting to int")
                entry.type = 1
            elif type == 2:
                Warning(node.token,"Converting to float")
                entry.type = 2
            elif type == 3:
                Warning(node.token,"Converting to char")
                entry.type = 3

    # constant value (right?)
    else:
        print (node.name)
        Ltype = typecast[node.token.type]
        if not Ltype == type: # keeping void for what it is
            Warning(node.token,"forced type conversion")
            if type == TypeClass.INTEGER:
                Warning(node.token, "Converting to int")
                node.Typedcl = IntegerType()
                if Ltype == TypeClass.CHAR:
                    node.name = ord(node.name)
                    return
                node.name = int(node.name)
            elif type == TypeClass.FLOAT:
                Warning(node.token, "Converting to float")
                node.Typedcl = RealType()
                node.name = float(node.name)
            elif type == TypeClass.CHAR:
                Warning(node.token, "Converting to char")
                node.Typedcl = CharacterType()
                node.name = str(node.name)




'''


declaration v
function definition v
while
condition
return
funccall
array
operators
access
include

'''







