from src.astclasses.AST import *


class IDNode(ASTNode):
    def handle(self, entr, type=None,):

        if type is not None:
            TypeCheck(self,entr,type)
            return


        if self.Typedcl == "id":
            if entr.type == 4:
                raise SemanticsError(self.token,"Declared variable void")
            entr.name = self.name
            return

        elif self.Typedcl == "func":

            entr.func = True
            entr.name = self.name
            if(len(self.children) == 0):
                entr.params = []

            else:
                entr.params = self.getchild(0).handle()

        elif self.Typedcl == "array":
            entr.name = self.name
            for child in reversed(self.children):
                #TODO: typecheck child.name and see scopecheck (if child.name == var)
                entr.type = "array("+child.name +","+ str(entr.type) + ")"
            return

        elif self.name == "pointer":
            entr.ptr = True
            self.getchild(0).handle(entr)
            return


        else:
            self.getchild(0).handle(entr)
            return


    def getCode(self, env:SymbolTable):

        inl = InstructionList()

        inl.AddInstruction(self.getLValue(env))
        inl.AddInstruction(LoadIndirectly(env.getType(self.name)))

        return inl

    def getLValue(self, env:SymbolTable):
        return LoadConstant(AddressType(),env.getLvalue(self.name))




class ConstantNode(ASTNode):


    def handle(self,st,type=None):
        if type is not None:
            TypeCheck(self,st,type)

    def getCode(self, env:SymbolTable = None):
        return LoadConstant(self.Typedcl,self.name)