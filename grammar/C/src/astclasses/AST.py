from src.parser.SymbolTable import *
from build.CLexer import *
from build.CParser import *
from src.util.Instructionlist import *
from src.parser.traverser import AstVisitor
from src.error.Error import SemanticsError
from src.error.Warning import Warning
#utils


typecast = { CLexer.INTEGER :IntegerType , CLexer.CHARACTER : CharacterType, CLexer.DECIMAL : RealType ,
             CLexer.VOID: None,CLexer.INT : IntegerType, CLexer.FLOAT : RealType, CLexer.CHAR : CharacterType}



class ASTNode:
    def __init__(self,n="root",t=None):
        self.par = None
        self.children = []
        self.name = n
        self.token = t
        self.Typedcl = None
        self.symbtable = None
        self.isconst = False
        self.operator = None
        self.comp = False
        self.result = None
        self.ptrcount = 0
        self.ptrog = 0
        self.printlist = []

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
            return "<font color = \"blue\">" +str(self.Typedcl) +"</font><br/>"+ str(self.name)


    def getchild(self,idx):
        return self.children[idx]


    def clearchildren(self):
        self.children = []


    def hasChild(self):
        if(len(self.children) == 0):
            return False
        else:
            return True

    def pointerlevel(self,st : SymbolTable,number=0):
        if self.symbtable is not None:
            st = self.symbtable

        p = 0
        if self.Typedcl == 'id':
            entr = st.getVariableEntry(self.name)
            p = entr.ptr - self.ptrcount
        else:
            if self.ptrcount > 0:
                raise SemanticsError(self.getToken(),"Dereferncing non variables")
        if p < 0:
            raise SemanticsError(self.getCode(),"Accessing non pointer memory")
        return p


    def getToken(self): # sick depth first search token finder implementation
        if self.token is not None:
            return self.token
        else:
            for child in self.children:
                token = child.getToken()
                if token is None:
                    continue
                else:
                    return token
        return None


    def handle(self,st,type = None):
        pass

    def getCode(self):
        pass

    def getLValue(self):
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







