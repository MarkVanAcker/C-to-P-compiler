from src.astclasses.AST import *
from src.astclasses.atomictypes import TypeNode



class ParamNode(ASTNode):
    def handle(self,st = None):
        print("paramNode11")
        print("paramNode")
        print("paramNode22")
        paramlist = []
        for param in self.children:
            if param.name == "empty":
                continue

            if isinstance(param, TypeNode):
                paramlist.append(param.Typedcl)
            else:
                paramlist.append(param.getchild(0).Typedcl)
        return paramlist


class FunctionDefinitionNode(ASTNode):
    def handle(self, st:SymbolTable):

        entry = self.getchild(0).handle(st,True) #declaration visit


        newst = SymbolTable()
        newst.name = entry.name
        newst.return_type = entry.type
        newst.is_function = True
        st.addchild(newst)
        
        
        #or param in reversed(self.getchild(1).children):
        #   if param.name == "empty":
        #       continue

        #   print("adding param")
        #   paramentry = param.handle(newst)
        #   entry.params.append(paramentry.type)
        #   #might not want to insert because of declaration resetting to default value
        #   #self.getchild(2).children.insert(0, param)

        
        
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
        pass


class ArgumentsNode(ASTNode):
    def handle(self,st, type = None):
        pass
