#Datatypes

class PType:
    def getType(self):
        pass

    def __str__(self):
        return self.getType()

class AddressType(PType):

    def getType(self):
        return 'a'


class CharacterType(PType):

    def getType(self):
        return 'c'

class BooleanType(PType):

    def getType(self):
        return 'b'

# Numeric type for extra assertion
class NumericType(PType):

    def getType(self):
        pass

class IntegerType(NumericType):


    def getType(self):
        return 'i'


class RealType(NumericType):

    def getType(self):
        return 'r'

class AnyType(PType):
    def getType(self):
        return 'any'