from copy import copy
from src.util.PType import *

typeconversion = {1 : IntegerType, 2: RealType, 3: CharacterType}

class SymbolTable:
    def __init__(self):
        self.entries = []
        self.children = []
        self.parent = None
        self.name = ""
        self.io = False



        #scope info

        self.is_function = False
        self.return_type = None
        self.is_loop = False

        self.variablespace = 0

        self.symbollist = {}

        self.variablestacksize = 5

        self.maxvariablestacksize = 0


    def addEntry(self,entry):
        self.variablespace += entry.getVarspace()
        self.entries.append(entry)

    def findByName(self,name):
        pass

    def getFuncRoot(self):
        if self.is_function:
            return self
        else:
            if self.parent is None:
                return self
            return self.parent.getFuncRoot()

    def LocalTableLookup(self,entr):
        for entry in self.entries:
            if (entry.name == entr.name):
                return entry

        return None

    def isGlobal(self,entr,depth=0):

        if self.parent is None:
            if depth == 0:
                return False
            else:
                return True


        for entry in self.entries:
            if (entry.name == entr.name):
                return False

        return self.parent.isGlobal(entr,depth + 1)

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
        st.io = self.io
        self.children.append(st)


    def GlobalTableLookup(self,entr):
        for entry in self.entries:
            if (entry.name == entr.name):
                return entry

        if (self.parent is None):
            return None
        else:
            return self.parent.GlobalTableLookup(entr)




    #Environment functions


    def getLvalue(self,symbol:str):
        return self.symbollist[symbol][1]

    def getType(self,symbol:str):
        return self.symbollist[symbol][0]

    def setEnvironment(self):
        if self.parent.parent is not None:
            self.variablestacksize = self.parent.variablestacksize
        self.symbollist = copy(self.parent.symbollist)


    def addSymbol(self,name):

        entry = self.GlobalTableLookup(Entry(name))
        if entry.ptr > 0:
            self.symbollist[entry.name] = (AddressType(),self.variablestacksize)
        else:
            self.symbollist[entry.name] = (entry.type,self.variablestacksize)
        self.variablestacksize += entry.getVarspace()

    #returns the required global space
    def getGlobalSpace(self):
        counter = self.getRequiredSpace()

        for entry in self.entries:
            if entry.func:
                continue
            counter  += 1

        return counter

    def getRequiredSpace(self):
        return max(self.variablestacksize,self.maxvariablestacksize)









    def toDot(self,file):
        file.write( "\tST" + str(id(self)) + ''' [label=< <table border="0" cellborder="1" cellspacing="0">
        <tr><td bgcolor="grey" >''' + self.name + '''</td></tr>
         <tr> <td bgcolor="yellow" >Name</td> <td bgcolor="yellow" >Type</td> <td bgcolor="yellow" >Pointer</td> <td bgcolor="yellow" >Const</td> <td bgcolor="yellow" >Func</td>  <td bgcolor="yellow" >array</td> <td bgcolor="yellow">Params</td></tr>
         \n''')
        for e in self.entries:
            file.write("<tr><td>"+e.name+"</td>  <td>"+ str(e.type) + "</td> <td>"+str(e.ptr)+"</td> <td>"+str(e.const)+"</td> <td>"+str(e.func)+"</td> <td>" + str(e.array) + "</td> <td>")
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
        self.ptr = 0
        self.func = False
        self.defined = False
        self.array = False
        self.params = []
        self.arrays = []

        #needed for code convertion
        self.size = s

    def typecompare(self,other):

        if other is None:
            return False

        if (isinstance(self.type,type(other.type)) and self.ptr  == other.ptr):
            return True
        else:
            return False

    def __eq__(self, other):

        #TODO: This is not so shallow

        if other is None:
            return False

        if( self.name == other.name):
            return True
        else:
            return False


    def getVarspace(self):
        if self.func:
            return 0
        elif self.array:
            tot = 1
            for i in self.arrays:
                tot *= i
            return tot
        else:
            return self.size

    def __str__(self):
        return str(self.ptr) + " " +str(self.type)


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
