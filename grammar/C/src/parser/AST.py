class ASTNode:
    def __init__(self,n="root",t=None,hf=None):
        self.par = None
        self.children = []
        self.name = n
        self.token = t
        self.Typedcl = None
        self.symbtable = None

        #visiting
        self.handlefunction = hf


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
            return self.name
        else:
            return "<font color = \"blue\">" +self.Typedcl +"</font><br/>"+ self.name


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
        self.symbtable = st

        if self.handlefunction is None:
            return
        self.handlefunction(self,self.symbtable)






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
