class SymbolTable:
    def __init__(self,parent = None):
        self.entries = []
        self.children = []
        self.parent = parent

    def addEntry(self,entry):
        self.entries.append(entry)

    def findByName(self,name):
        pass






class Entry:
    def __init__(self,n,t):
        self.name = n
        self.type = t
