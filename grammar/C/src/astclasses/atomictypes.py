from src.astclasses.AST import *


class IDNode(ASTNode):
    def handle(self, st, type=None):

        self.symbtable = st

        if type is not None:
            TypeCheck(self, st, type)
            return





    def getCode(self):

        inl = InstructionList()

        inl.AddInstruction(self.getLValue())
        inl.AddInstruction(LoadIndirectly(self.symbtable.getType(self.name)))

        return inl

    def getLValue(self):
        return LoadConstant(AddressType(),self.symbtable.getLvalue(self.name))




class ConstantNode(ASTNode):


    def handle(self,st,type=None):
        if type is not None:
            TypeCheck(self,st,type)

    def getCode(self, env:SymbolTable = None):
        return LoadConstant(self.Typedcl,self.name)





def TypeCheck(node, st, t):

    # variable
    #node = node.getchild(0)
    if isinstance(node,IDNode):
        entry = st.getVariableEntry(node.name)
        if entry is None:
            raise SemanticsError(node.token,"undeclared varaible (first use in this function)")
        Ltype = entry.type
        if not isinstance(Ltype, type(t)): # keeping void for what it is
            raise SemanticsError(node.token,"No dynamic conversion supported")

            #TY to Jesse for this nice tip for multiline commenting ty
            #if type == 1: # void ?
            #    Warning(node.token,"Converting to int")
            #    entry.type = 1
            #elif type == 2:
            #    Warning(node.token,"Converting to float")
            #   entry.type = 2
            #elif type == 3:
            #    Warning(node.token,"Converting to char")
            #    entry.type = 3

    # constant value (right?)
    else:
        Ltype = node.Typedcl

        if not isinstance(Ltype, type(t)): # keeping void for what it is
            Warning(node.token,"forced type conversion")
            if isinstance(t, IntegerType):
                Warning(node.token, "Converting to int")
                node.Typedcl = IntegerType()
                if isinstance(Ltype,CharacterType):
                    node.name = ord(node.name)
                    return
                node.name = int(node.name)
            elif isinstance(t, RealType):
                Warning(node.token, "Converting to float")
                node.Typedcl = RealType()
                node.name = float(node.name)
            elif isinstance(t, CharacterType):
                Warning(node.token, "Converting to char")
                node.Typedcl = CharacterType()
                node.name = str(node.name)


class TypeNode(ASTNode):

    def handle(self,st):
        pass