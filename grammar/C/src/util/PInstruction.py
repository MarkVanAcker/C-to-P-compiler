from src.parser.astclasses import *
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