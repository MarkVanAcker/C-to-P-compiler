class SymbolTable:
    def __init__(self):
        self.entries = []

    def addEntry(self,entry):
        self.entries.append(entry)






class Entry:
    def __init__(self,n,t,s):
        self.name = n
        self.type = t
        self.scope = s