from src.astclasses.AST import *
from src.astclasses.atomictypes import TypeNode
from src.astclasses.declaration import DeclarationNode


class ParamNode(ASTNode):
    def handle(self,st = None):
        paramlist = []
        for param in self.children:
            if param.name == "empty":
                continue

            if isinstance(param, TypeNode):
                if (param.isconst == True):
                    paramlist.append(param.getchild(0).Typedcl)
                else:
                    paramlist.append(param.Typedcl)

            else:
                paramlist.append(param.getchild(0).Typedcl)
        return paramlist


class FunctionDefinitionNode(ASTNode):
    def handle(self, st:SymbolTable):

        entry = self.getchild(0).handle(st,True) #declaration visit


        # important: it is not required to check for const for the parameters, only usefull at definition, can defer in decl and def arg list


        # check the entry paramlist if it matches ( only typechecking )
        paramlist = self.getchild(1).handle()
        if len(paramlist) != len(entry.params):
            raise SemanticsError(self.token, "parameterlist does not match in size")
        else:
            for i in range(len(paramlist)):
                if str(paramlist[i]) != str((entry).params[i]):
                    print(str(paramlist[i]))
                    print(str((entry).params[i]))
                    raise SemanticsError(self.getchild(1).getchild(i).token, "parameterlist item does not match at index: " + str(i))

        newst = SymbolTable()
        newst.name = entry.name
        newst.return_type = entry.type
        newst.is_function = True
        st.addchild(newst)

        # checking if all declarations and adding into symbol table
        for par in self.getchild(1).children:

            if isinstance(par,DeclarationNode):
                par.handle(newst)
            elif par.Typedcl == None and par.name == 'empty':
                continue
            else:
                raise SemanticsError(self.token, "parameter name omitted")




        
        
        self.getchild(2).handle(newst)




class ReturnNode(ASTNode):
    #check if variable that is to be returned exists and matches return type
    def handle(self, st):
        stFunc = st.getFuncRoot()
        if stFunc.parent is None:
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
            self.getchild(0).handle(st, funcReturnType) # evaluate expression statement





class FunctionCallNode(ASTNode):
    def handle(self,st,type = None):
        #
        # Look up is function is defined, later check is arguments are correct, we can not convert
        #
        entry = st.getVariableEntry(self.getchild(0).name)
        if not entry:
            raise SemanticsError(self.token, "undefined reference to '"+ self.getchild(0).name + "'")

        if not entry.func:
            raise SemanticsError(self.token, "Calling uncallable object")



        # optimalise this
        arglist = self.getchild(1).handle()
        if len(arglist) != len(entry.params):
            raise SemanticsError(self.token, "parameterlist does not match in size")
        else:
            for i in range(len(arglist)):
                if str(arglist[i]) != str((entry).params[i]):
                    print(str(arglist[i]))
                    print(str((entry).params[i]))
                    raise SemanticsError(self.getchild(1).getchild(i).token,"parameterlist item does not match at index: " + str(i))



class ArgumentsNode(ASTNode):
    def handle(self,st, type = None):
        #
        # Resolve types from each parameter and return typelist
        #
        pass
