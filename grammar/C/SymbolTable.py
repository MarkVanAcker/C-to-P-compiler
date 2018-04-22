class SymbolTable:
    def __init__(self,parent = None):
        self.entries = []
        self.children = []
        self.parent = parent

    def addEntry(self,entry):
        self.entries.append(entry)

    def findByName(self,name):
        pass

    def LocalTableLookup(self,name):
        pass


    def GlobalTableLookup(self,name):
        pass




class Entry:
    def __init__(self,n = "",t = None):
        self.name = n
        self.type = t
        self.const = False
        self.ptr = False
        
        
    def typecompare(self,other):
        if (self.type == other.type and self.ptr  == other.ptr):
            return True
        else:
            return False
