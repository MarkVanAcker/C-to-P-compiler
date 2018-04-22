class ASTNode:
    def __init__(self,n="root",t=None,p=None):
        self.par = p
        self.children = []
        self.name = n
        self.token = t
        self.Typedcl = None
        self.hasChild = False

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
        self.hasChild = True

    def addchildren(self,c):
        for child in c:
            self.addchild(child)
        self.hasChild = True

    def getstr(self):
        if self.Typedcl is None:
            return self.name
        else:
            return "<font color = \"blue\">" +self.Typedcl +"</font><br/>"+ self.name


    def getchild(self,idx):
        return self.children[idx]

    def clearchildren(self):
        self.children = []
        self.hasChild = False


def ToDot(root):
    file = open(".AST.dot","w")

    file.write('''digraph G
{
    nodesep = 0.4;
    ranksep = 0.5;
''')


    root.todot(file)



    file.write('}')

    file.close()
