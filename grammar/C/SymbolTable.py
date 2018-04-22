class SymbolTable:
    def __init__(self,parent = None):
        self.entries = []
        self.children = []
        self.parent = parent

    def addEntry(self,entry):
        self.entries.append(entry)

    def findByName(self,name):
        pass

    def LocalTableLookup(self,entr):
        for entry in self.entries:
            if (entry == entr):
                return True

        return False


    def GlobalTableLookup(self,entr):
        for entry in self.entries:
            if (entry == entr):
                return True

        if (self.parent is None):
            return False
        else:
            return self.parent.GlobalTableLookup(entr)




class Entry:
    def __init__(self,n = "",t = None):
        self.name = n
        self.type = t
        self.const = False
        self.ptr = False
        self.func = False
        self.params = []
        
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
