from src.astclasses.AST import *


class ParamNode(ASTNode):
    def handle(self,st = None):
        paramlist = []
        for child in self.children:
            if(child.name == "paramdecl"):
                paramlist.append(typecast[child.getchild(0).token.type])

            else:
                paramlist.append(typecast[child.token.type])

        return paramlist




class FunctionDefinitionNode(ASTNode):
    def handle(self, st):

        # delcartion visitor should throw if name is already in use (pass redeclarations)
        # TODO: delcare and after define function
        self.getchild(0).getchild(1).addchild(self.getchild(1))
        self.getchild(0).handle(st) #declaration visit

        for param in reversed(self.getchild(1).children):
            if param.name == "empty":
                continue
            self.getchild(2).children.insert(0, param)



        newst = SymbolTable()
        newst.name = self.getchild(0).getchild(1).name

        st.addchild(newst)
        v = AstVisitor(self.getchild(2), newst)

        v.traverse()



class ReturnNode(ASTNode):
    #check if variable that is to be returned exists and matches return type
    def handle(self, st):
        stFunc = st.getFuncRoot()
        if stFunc.parent == None:
            raise SemanticsError(self.token,"Return in a non definition block")


        stParent = stFunc.parent
        returnType = ''
        funcReturnType = stParent.getVariableEntry(stFunc.name).type
        if len(self.children) == 0:
            # void return
            returnType = 4
            if funcReturnType!= 4:
                SemanticsError(self.token,"Expected void return but got another type")
        else:
            returnType = self.getchild(0).handle(st, funcReturnType) #expression statement



