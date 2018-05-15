from src.parser.SymbolTable import *
from copy import copy
from src.util.PType import *

typeconversion = {1 : IntegerType, 2: RealType, 3: CharacterType}



class Environment:

    def __init__(self,sl:dict):

        #map from symbol to adress
        self.symbollist = copy(sl)


    def getLvalue(self,symbol:str):
        return self.symbollist[symbol][1]

    def getType(self,symbol:str):
        return self.symbollist[symbol][0]

    def getChildEnvironment(self,st:SymbolTable):
        env = Environment(self.symbollist)
        return Environment

    def readSymbolTable(self,st:SymbolTable,baseAddr:int):

        currentAddr = baseAddr + 5
        for i in st.entries:
            if not i.func:
                if i.ptr:
                    self.symbollist[i.name] = (AddressType(),currentAddr)
                else:
                    self.symbollist[i.name] = (typeconversion[i.type],currentAddr)


                currentAddr += i.size
