class SymbolTable:
    def __init__(self):
        self.entries = []
        self.children = []
        self.parent = None
        self.name = ""

    def addEntry(self,entry):
        self.entries.append(entry)

    def findByName(self,name):
        pass

    def getFuncRoot(self):
        if self.name != 'block' or self.name != 'iteration' or self.name != 'condition':
            return self
        else:
            self.parent.getFuncRoot()

    def LocalTableLookup(self,entr):
        for entry in self.entries:
            if (entry == entr):
                return True

        return False

    def getVariableEntry(self,name):
        for entry in self.entries:
            if (entry.name == name):
                return entry

        if (self.parent is None):
            return None
        else:
            return self.parent.getVariableEntry(name)



    def addchild(self,st):
        st.parent = self
        self.children.append(st)


    def GlobalTableLookup(self,entr):
        for entry in self.entries:
            if (entry == entr):
                return True

        if (self.parent is None):
            return False
        else:
            return self.parent.GlobalTableLookup(entr)

    def toDot(self,file):
        file.write( "\tST" + str(id(self)) + ''' [label=< <table border="0" cellborder="1" cellspacing="0">
        <tr><td bgcolor="grey" >''' + self.name + '''</td></tr>
         <tr> <td bgcolor="yellow" >Name</td> <td bgcolor="yellow" >Type</td> <td bgcolor="yellow" >Pointer</td> <td bgcolor="yellow" >Const</td> <td bgcolor="yellow" >Func</td> <td bgcolor="yellow">Params</td></tr>
         \n''')
        for e in self.entries:
            file.write("<tr><td>"+e.name+"</td>  <td>"+ str(e.type) + "</td> <td>"+str(e.ptr)+"</td> <td>"+str(e.const)+"</td> <td>"+str(e.func)+"</td> <td>")
            for p in e.params:
                file.write(str(p) + " ")
            file.write("</td></tr>")
        file.write('''\n </table>>];''')
        if(self.parent is not None):
            file.write("\tST"+str(id(self.parent))+"->ST"+str(id(self))+"\n")
        for c in self.children:
            c.toDot(file)









class Entry:
    def __init__(self,n = "",t = None,s = 1):
        self.name = n
        self.type = t
        self.const = False
        self.ptr = False
        self.func = False
        self.params = []

        #needed for code convertion
        self.size = s

    def typecompare(self,other):
        if (self.type == other.type and self.ptr  == other.ptr):
            return True
        else:
            return False

    def __eq__(self, other):

        #TODO: This is not so shallow

        if( self.name == other.name):
            return True
        else:
            return False



def ToDotST(root):

    import os
    if not os.path.exists('./output'):
        os.makedirs('./output')

    file = open("./output/.ST.dot","w")

    file.write('''digraph G
{
    nodesep = 0.4;
    ranksep = 0.5;
    node [shape=plaintext]
\n''')


    root.toDot(file)

    file.write('\n}')

    file.close()
