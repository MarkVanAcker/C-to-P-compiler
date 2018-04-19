class ASTNode:
    def __init__(self,n="root",p=None):
        self.par = p
        self.children = []
        self.name = n
        self.info = None

    def todot(self,file):

        file.write("\tNODE" + str(id(self)) + "[label=\"" + self.name + "\"];\n")
        if(self.par is not None):
            file.write("\tNODE"+str(id(self.par))+"->NODE"+str(id(self))+"\n")
        for child in self.children:
            child.todot(file)




def ToDot(root):
    file = open("AST.dot","w")

    file.write('''digraph G
{
    nodesep = 0.4;
    ranksep = 0.5;
''')


    root.todot(file)



    file.write('}')

    file.close()


