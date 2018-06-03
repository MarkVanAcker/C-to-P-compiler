from src.astclasses.AST import *
from src.astclasses.atomictypes import *



def checknode(arg,type,pointer,st):
    entry = None

    if isinstance(arg, ConstantNode) or isinstance(arg, IDNode) or isinstance(arg, FunctionCallNode) or isinstance(arg,ArrayCallNode):  # constant node handle
        entry = arg.handle(st, type)

        # checking pointer levels
        if pointer != entry.ptr:
            raise SemanticsError(arg.getToken(), "Pointer referces not correct in variable")

    elif arg.name == "ExpressionNode" and arg.comp == True:
        raise SemanticsError(arg.getToken(), "No boolean types evaluated in funccal argument")
    elif arg.name == "ExpressionNode" and arg.comp == False and pointer == 0:
        arg.handle(st, type)
    elif arg.name == "ExpressionNode" and arg.comp == False and typelist[index].ptr != 0:
        raise SemanticsError(arg.getToken(), "Expression in funccal argument can not evaluate addresses")

    elif isinstance(arg, DerefNode) or isinstance(arg, AddressNode):
        entry = arg.handle(st, [type, pointer])

    return entry


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
                Deref, address
        '''

        if len(argnode.children) == 0:
            raise SemanticsError(self.getToken(), "Printf takes at least 1 argument")

        if not isinstance(argnode.getchild(0),ConstantNode):
            raise (argnode.getToken(), "Expected Char array as first argument of printf")

        argumentsavailable = len(argnode.children) -1
        charstring = argnode.getchild(0).name


        # all children must avulatie to const values , no addresses

        self.symbtable = st




        foundsym = False
        index = 1
        for val in charstring:

            if (val == 'd' or val == 'f' or val == 'c' or val == 's') and foundsym:

                if index > argumentsavailable:
                    raise SemanticsError(self.getToken(),"Printf argument requested which is not present")

                if val == 'd':
                    evaltype = IntegerType()
                    pointer = 0
                    checknode(argnode.getchild(index),evaltype,0,st)
                    self.printlist.append((argnode.getchild(index), evaltype,val))

                elif val == 'f':
                    evaltype = RealType()
                    pointer = 0
                    checknode(argnode.getchild(index),evaltype,0,st)
                    self.printlist.append((argnode.getchild(index), evaltype,val))

                elif val == 'c':
                    evaltype = CharacterType()
                    pointer = 0
                    checknode(argnode.getchild(index),evaltype,0,st)
                    self.printlist.append((argnode.getchild(index), evaltype,val))

                elif val == 's':

                    if isinstance(argnode.getchild(index),ConstantNode) and len(argnode.getchild(index).name) > 1:
                       for item in argnode.getchild(index).name:
                           self.printlist.append(ord(item))

                    else:
                        evaltype = CharacterType()
                        pointer = 0
                        checknode(argnode.getchild(index),evaltype,1,st)
                        self.printlist.append((argnode.getchild(index), evaltype,val))
                else:
                    pass

                index += 1
                continue
            if val == '%':
                foundsym = True
                continue
            foundsym = False
            self.printlist.append(ord(val))








class ScanfNode(ASTNode):
    def handle(self,st,type = None):

        if st.io == False:
            raise SemanticsError(self.getToken(), "Using scanf without including stdio, did you forget including the libary?")


        argnode = self.getchild(1)

        '''     ConstantNode
                IDNode
                ArrayCallNode checked on name return type
                ExpressionNode
                FunctionCallNode checked on name return type
                Deref, address
        '''

        if len(argnode.children) == 0:
            raise SemanticsError(self.getToken(), "Scanf takes at least 1 argument")

        if not isinstance(argnode.getchild(0),ConstantNode):
            raise (argnode.getToken(), "Expected Char array as first argument of scanf")

        argumentsavailable = len(argnode.children) -1
        charstring = argnode.getchild(0).name

        if argumentsavailable > 1:
            raise SemanticsError(self.getToken(), "Scanf takes exactely 2 arguments")


        # all children must avulatie to const values , no addresses

        self.symbtable = st


        if charstring[0] != "%" or len(charstring) != 2:
            raise SemanticsError(self.getToken(), "format string has wrong format in scanf")

        if charstring[1] != 'd' and charstring[1] != 's' and charstring[1] != 'f' and charstring[1] != 'c':
            raise SemanticsError(self.getToken(), "format string has wrong format (after %) in scanf")

        index = 1
        val = charstring[1]

        if val == 'd':
            evaltype = IntegerType()
            pointer = 1
            checknode(argnode.getchild(index), evaltype, 1, st)
            self.printlist.append((argnode.getchild(index), evaltype,val))

        elif val == 'f':
            evaltype = RealType()
            pointer = 1
            checknode(argnode.getchild(index), evaltype, 1, st)
            self.printlist.append((argnode.getchild(index), evaltype,val))

        elif val == 'c':
            evaltype = CharacterType()
            pointer = 1
            checknode(argnode.getchild(index), evaltype, 1, st)
            self.printlist.append((argnode.getchild(index), evaltype,val))

        elif val == 's':
                evaltype = CharacterType()
                pointer = 1
                checknode(argnode.getchild(index), evaltype, 1, st)
                self.printlist.append((argnode.getchild(index), evaltype,val))
        else:
            pass



