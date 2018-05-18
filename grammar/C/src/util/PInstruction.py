from src.util.PType import *

#TODO: Document + maybe split up in different modules?

class PInstruction:

    def write(self):
        pass



########## Arithmetic instructions  #######


class Add(PInstruction):

    def __init__(self, t:NumericType):
        self.type = t

    def write(self):
        return 'add %s' % self.type.getType()


class Subtract(PInstruction):

    def __init__(self, t:NumericType):
        self.type = t

    def write(self):
        return 'sub %s' % self.type.getType()

class Multiply(PInstruction):

    def __init__(self, t:NumericType):
        self.type = t

    def write(self):
        return 'mul %s' % self.type.getType()

class Divide(PInstruction):

    def __init__(self, t:NumericType):
        self.type = t

    def write(self):
        return 'div %s' % self.type.getType()

class Invert(PInstruction):

    def __init__(self, t:NumericType):
        self.type = t

    def write(self):
        return 'neg %s' % self.type.getType()


########## Logical instruction  #######


class And(PInstruction):

    def write(self):
        return 'and'


class Or(PInstruction):

    def write(self):
        return 'or'

class Not(PInstruction):

    def write(self):
        return 'not'

########## Comparison instructions  #######

class Equal(PInstruction):

    def __init__(self,t:PType):
        self.type = t

    def write(self):
        return 'equ %s' + self.type.getType()


class GreaterOrEqual(PInstruction):

    def __init__(self, t: PType):
        self.type = t

    def write(self):
        return 'geq %s' + self.type.getType()


class LesserOrEqual(PInstruction):

    def __init__(self, t: PType):
        self.type = t

    def write(self):
        return 'leq %s' + self.type.getType()

class Lesser(PInstruction):

    def __init__(self, t: PType):
        self.type = t

    def write(self):
        return 'les %s' + self.type.getType()

class Greater(PInstruction):

    def __init__(self, t: PType):
        self.type = t

    def write(self):
        return 'grt %s' + self.type.getType()

class NotEqual(PInstruction):

    def __init__(self, t: PType):
        self.type = t

    def write(self):
        return 'neq %s' + self.type.getType()



########## Store and load instructions  #######

class LoadLocation(PInstruction):

    def __init__(self,t:PType, q:int):
        self.type = t
        self.address = q

    def write(self):
        return 'ldo %s %i' % (self.type.getType() , self.address)

class LoadConstant(PInstruction):

    def __init__(self,t:PType, q):
        self.type = t
        self.value = str(q)

    def write(self):
        return 'ldc %s %s' % (self.type.getType() , self.value)

class LoadIndirectly(PInstruction):

    def __init__(self,t:PType):
        self.type = t

    def write(self):
        return 'ind %s' % self.type.getType()

class StoreAbsolute(PInstruction):

    def __init__(self,t:PType, q:int):
        self.type = t
        self.address = q

    def write(self):
        return 'sro %s %i' % (self.type.getType(), self.address)


class StoreStack(PInstruction):

    def __init__(self,t:PType):
        self.type = t

    def write(self):
        return 'sto %s' % self.type.getType()



########## Conditional,unconditional and indexed branches  #######

class UnconditionalJump(PInstruction):

    def __init__(self,l:str):
        self.label = l

    def write(self):
        return 'ujp %s' % self.label


class ConditionalJump(PInstruction):

    def __init__(self,l:str):
        self.label = l

    def write(self):
        return 'fjp %s' % self.label

class IndexedJump(PInstruction):

    def __init__(self,l:str):
        self.label = l

    def write(self):
        return 'ixj %s' % self.label

#computation of indexed address
class IndexComp(PInstruction):

    def __init__(self,q:int):
        self.index = q

    def write(self):
        return 'ixa %i' % self.index


########## Increment and decrement  #######

class Increment(PInstruction):

    def __init__(self, t:PType, q:int):
        self.type = t
        self.i = q

    def write(self):
        return 'inc %s %i' % (self.type,self.i)


class Decrement(PInstruction):

    def __init__(self, t: PType, q: int):
        self.type = t
        self.i = q

    def write(self):
        return 'dec %s %i' % (self.type, self.i)


########## Boundary check  #######

class BoundaryCheck(PInstruction):

    def __init__(self, p: int, q: int):
        self.i1 = p
        self.i2 = q

    def write(self):
        return 'chk %i %i' % (self.i1, self.i2)


####SKIPPED DYNAMIC ARRAYS



########## Loading and storing for difference in nesting depths   #######


class ProcedureLoadType(PInstruction):

    def __init__(self, t: PType,p: int, q: int):
        self.type = t
        self.depth = p
        self.address = q

    def write(self):
        return 'lod %s %i %i' % (self.type, self.depth,self.address)

class ProcedureLoadAddress(PInstruction):

    def __init__(self,p: int, q: int):
        self.depth = p
        self.address = q

    def write(self):
        return 'lda %i %i' % ( self.depth,self.address)

class ProcedureStoreType(PInstruction):

    def __init__(self, t: PType,p: int, q: int):
        self.type = t
        self.depth = p
        self.address = q

    def write(self):
        return 'str %s %i %i' % (self.type, self.depth,self.address)


########## Instructions for calling,entering and returning procedures    #######

class MarkStack(PInstruction):

    def __init__(self,p:int):
        self.depth = p

    def write(self):
        return 'mst %i' % self.depth

class CallUserProcedure(PInstruction):

    def __init__(self,p: int, q: str):
        self.storage = p
        self.label = q

    def write(self):
        return 'cup %i %s' % ( self.storage,self.label)

class SetStackPointer(PInstruction):

    def __init__(self,p:int):
        self.value = p

    def write(self):
        return 'ssp %i' % self.value

class SetExtremePointer(PInstruction):

    def __init__(self,p:int):
        self.value = p

    def write(self):
        return 'sep %i' % self.value

class SetPointers(PInstruction):

    def __init__(self,p:int,q:int):
        self.stackvalue = p
        self.extremevalue = q

    def write(self):
        return 'ent %i %i' % (self.stackvalue,self.extremevalue)

class ReturnResult(PInstruction):

    def write(self):
        return 'retf'

class ReturnNoResult(PInstruction):

    def write(self):
        return 'retp'



########## Block copy instruction    #######

class MoveBlockLoad(PInstruction):

    def __init__(self,q:int):
        self.size = q

    def write(self):
        return 'movs %i' % self.size


#Not sure what this does :TODO
class MoveBlockStore(PInstruction):

    def __init__(self,q:int):
        self.size = q

    def write(self):
        return 'movd %i' % self.size

#Skipped bonus instructions because didn't see the use


########## Halt instruction    #######

class Halt(PInstruction):

    def write(self):
        return 'hlt'

########## Input/Output instructions   #######

class InInteger(PInstruction):

    def write(self):
        return 'in i'


class InReal(PInstruction):

    def write(self):
        return 'in r'

class InCharacter(PInstruction):

    def write(self):
        return 'in c'

class InBoolean(PInstruction):

    def write(self):
        return 'in b'


class OutInteger(PInstruction):

    def write(self):
        return 'out i'


class OutReal(PInstruction):

    def write(self):
        return 'out r'


class OutCharacter(PInstruction):

    def write(self):
        return 'out c'


class OutBoolean(PInstruction):

    def write(self):
        return 'out b'

class OutRealPrecision(PInstruction):

    def write(self):
        return 'out r i'


########## Conversion instruction   #######

class Conversion(PInstruction):

    def __init__(self, t1: PType,t2:PType):
        self.type1 = t1
        self.depth2 = t2

    def write(self):
        return 'conv %s %s' % (self.type1, self.type2)