from src.util.PInstruction import *
from src.util.PType import *
from src.util.Instructionlist import *
from src.code_generation.environment import *

#Compilation schemes from the compendium


class BaseNode:

    def getCode(self,env:Environment):
        pass

    def getL(self,env:Environment):
        pass


#node for a constant value needs type and value
class ConstantNode(BaseNode):

    def __init__(self,t:PType,val):

        self.type = t
        self.value = val

    def getCode(self,env:Environment):
        return LoadConstant(self.type,self.value)

#node for a variable in memory needs variable name only
class VariableNode(BaseNode):

    def __init__(self,s:str):
        self.symbol = s

    def getCode(self,env:Environment):

        inl = InstructionList()

        inl.AddInstruction(self.getL(env))
        inl.AddInstruction(LoadIndirectly(env.getType(self.symbol)))

        return inl


    def getL(self,env:Environment):
        return LoadConstant(AddressType(),env.getLvalue(self.symbol))

#node for an assignment expression only needs left and right part of the node
class AssignmentNode(BaseNode):

    def __init__(self,l,r):
        self.leftside = l
        self.rightside = r

    def getCode(self,env:Environment):

        inl = InstructionList()

        inl.AddInstruction(self.leftside.getL(env))

        inl.AddInstruction(self.rightside.getCode(env))

        return inl

#node for every binary operation - made this to avoid code duplication

class BinaryNode(BaseNode):

    def __init__(self,op:PInstruction,l,r):
        self.operation = op #Not sure if the type of the operator can be known beforehand
        self.leftside = l
        self.rightside = r

    def getCode(self,env:Environment):

        inl = InstructionList()

        inl.AddInstruction(self.leftside.getCode(env))
        inl.AddInstruction(self.rightside.getCode(env))

        inl.AddInstruction(self.operation)

        return inl


