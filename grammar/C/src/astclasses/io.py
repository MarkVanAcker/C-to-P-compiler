from src.astclasses.AST import *
#from src.astclasses.atomictypes import ConstantNode


class PrintfNode(ASTNode):
    def handle(self,st : SymbolTable,type = None):

        if st.io == False:
            raise SemanticsError(self.getToken(), "Using printf without including stdio, did you forget including the libary?")


        argnode = self.getchild(1)

        '''     ConstantNode
                IDNode
                ArrayCallNode checked on name return type
                ExpressionNode
                FunctionCallNode checked on name return type
        '''

        if len(argnode.children) == 0:
            raise SemanticsError(self.getToken(), "Printf takes at least 1 argument")

        print(argnode.getchild(0))
        if not isinstance(argnode.getchild(0),ConstantNode):
            raise (argnode.getToken(), "Expected Char array as first argument of printf")

        argumentsavailable = len(argnode.children) -1
        print("AV ", argumentsavailable)
        charstring = argnode.getchild(0).name
        print("String ", charstring)


        # all children must avulatie to const values , no addresses

        self.symbtable = st


        #index = 0
        #for arg in self.children:
        #    arg.symbtable = st
        #    if isinstance(arg, ConstantNode):  # constant node handle
        #        if not isinstance(arg.Typedcl, type(typelist[index].type)):
        #            raise SemanticsError(arg.getToken(), "Do not support type conversion at funccal argument")
        #    elif isinstance(arg, IDNode):  # IDnode handle
        #        entry = st.getVariableEntry(arg.name)
        #        if entry is None:
        #            raise SemanticsError(arg.getToken(), "Unknown variable")
        #        if not isinstance(entry.type, type(typelist[index].type)):
        #            raise SemanticsError(arg.getToken(), "Do not support type conversion at funccal argument")
        #    elif isinstance(arg, ArrayCallNode) or isinstance(arg,
        #                                                      FunctionCallNode) or arg.name == "ExpressionNode":  # other node handles that have children to call upon
        #        returntype = arg.handle(st)
        #        if not isinstance(returntype, type(typelist[index].type)):
        #            raise SemanticsError(arg.getToken(), "Do not support type conversion at funccal argument")

        #    index += 1



        foundsym = False
        for val in charstring:

            if (val == 'd' or val == 'f' or val == 'c') and foundsym:
                self.printlist.append((argumentsavailable,val))
                continue
            if val == '%':
                foundsym = True
                continue
            foundsym = False
            self.printlist.append(val)


        print("PR LIST", self.printlist)








class ScanfNode(ASTNode):
    def handle(self,st,type = None):

        if st.io == False:
            raise SemanticsError(self.getToken(), "Using scanf without including stdio, did you forget including the libary?")