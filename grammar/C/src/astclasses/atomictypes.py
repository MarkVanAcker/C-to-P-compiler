from src.astclasses.AST import *

class IDNode(ASTNode):
    def handle(self, st, type=None):

        self.symbtable = st

        if type is not None:
            TypeCheck(self, st, type)






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


    '''     ConstantNode
            IDNode
            ArrayCallNode
            ExpressionNode will not be called from here
            FunctionCallNode
    '''

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
    elif isinstance(node,ConstantNode):
        Ltype = node.Typedcl

        if not isinstance(Ltype, type(t)): # keeping void for what it is
            Warning(node.token,"forced type conversion")
            raise SemanticsError(node.token, "No dynamic conversion supported")
            #if isinstance(t, IntegerType):
            #    Warning(node.token, "Converting to int")
            #    node.Typedcl = IntegerType()
            #    if isinstance(Ltype,CharacterType):
            #        node.name = ord(node.name)
            #        return
            #    node.name = int(node.name)
            #elif isinstance(t, RealType):
            #    Warning(node.token, "Converting to float")
            #    node.Typedcl = RealType()
            #    node.name = float(node.name)
            #elif isinstance(t, CharacterType):
            #    Warning(node.token, "Converting to char")
            #    node.Typedcl = CharacterType()
            #    node.name = str(node.name)
    elif isinstance(node,ArrayCallNode) or isinstance(node,FunctionCallNode):
        print(node.handle(st))
        if not isinstance(t, type(node.handle(st))): # let array return type
            Warning(node.token,"forced type conversion")
            print(type(t), type(node.handle(st)))
            raise SemanticsError(node.token, "No dynamic conversion supported")

    else:
        raise SemanticsError(self.token, "WEIRD NODE GIVEN AT TYPECHECK")

class TypeNode(ASTNode):
    def handle(self,st):
        pass


class ParamNode(ASTNode):
    def handle(self,st = None):
        paramlist = []
        for param in self.children:
            if isinstance(param,EmptyNode):
                continue

            if isinstance(param, TypeNode):
                if (param.isconst == True):
                    paramlist.append(param.getchild(0).Typedcl)
                else:
                    paramlist.append(param.Typedcl)

            else:
                paramlist.append(param.getchild(0).Typedcl)
        return paramlist





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



        arglist = self.getchild(1).handle(st,entry.params)


        ## optimalise this
        #arglist = self.getchild(1).handle()
        #if len(arglist) != len(entry.params):
        #    raise SemanticsError(self.token, "parameterlist does not match in size")
        #else:
        #    for i in range(len(arglist)):
        #        if str(arglist[i]) != str((entry).params[i]):
        #            print(str(arglist[i]))
        #            print(str((entry).params[i]))
        #            raise SemanticsError(self.getchild(1).getchild(i).token,"parameterlist item does not match at index: " + str(i))



class ArgumentsNode(ASTNode):
    def handle(self,st, typelist = None):
        #
        # Resolve types from each parameter and return typelist
        #

        '''     ConstantNode
                IDNode
                ArrayCallNode
                ExpressionNode
                FunctionCallNode
        '''


        if typelist is None:
            return

        if len(typelist) != len(self.children):
            raise SemanticsError(self.token,"Incorrect number of arguments given in functioncall")

        index = 0
        for arg in self.children:
            if isinstance(arg,IDNode) or isinstance(arg,ConstantNode):
                continue



        for arg in self.children:
            print(arg.__class__.__name__)
            pass



class DeclarationNode(ASTNode):


    #maybe rewrite init to make it easier to process
    def handle(self, st, definition = False):

        reservedKeys = ["void", "int", "void", "bool", "float", "char", "default", "do", "double" , "long" , "goto", "case", "extern", "enum", "sizeof", "struct" "if", "else", "where", "for", "break", "continue", "return", "const"]


        type = self.getchild(0)
        entr = Entry()
        constt = False

        if (type.token.type == CParser.CONST):
            constt = True
            entr.type = type.getchild(0).Typedcl
        else:
            entr.type = type.Typedcl


        idnode = None

        if self.getchild(1).name == '=':
            idnode = self.getchild(1).getchild(0)
            if idnode.Typedcl == 'func':
                raise SemanticsError(idnode.token, "Can not assign to a function declaration")

        else:
            idnode = self.getchild(1)

        if idnode.name in reservedKeys:
            raise SemanticsError(self.token,"Can not use reserved keyword for variable name")

        checkdecl(idnode,entr)

        entryfound = st.LocalTableLookup(entr)
        if(entryfound is not None):
            if (entryfound.func == False):
                raise SemanticsError(self.token,"This variable was already declared in the local scope")
            elif (entryfound.func and not entryfound.defined and definition):
                entryfound.defined = True
            elif (entryfound.func and entryfound.defined and definition):
               raise SemanticsError(self.token, "Redefinition of function")
            else:
               raise SemanticsError(self.token, "Redeclaration of function")



        addentry = True
        entryfound = st.GlobalTableLookup(entr)
        if (entryfound is not None):
            if (entryfound.func == False):
                Warning(self.token,"%s is hiding variable" % entr.name)
            else:
                Warning(self.token,"%s is hiding function" % entr.name)






        if addentry:
            st.addEntry(entr)
            if self.getchild(1).name == '=':  # can only get at this statement if it is a variable (not a func)
                self.getchild(1).handle(st)  # assignment visit
            entr.const = constt
            # if function add params
            if entr.func == True and not definition:
                paramlist = idnode.getchild(0).handle()
                for item in paramlist:
                    entr.params.append(item)
                    print("adding: ", str(item))
            elif entr.func == True and definition:
                print(self.par.getchild(1).__class__.__name__)
                paramlist = self.par.getchild(1).handle()
                for item in paramlist:
                    entr.params.append(item)



        return entr






def checkdecl(node, ent):

    if node.Typedcl == "id":
        if ent.type is None:
            raise SemanticsError(node.token, "Declared variable void")
        ent.name = node.name
        return

    elif node.Typedcl == "func":

        ent.func = True
        ent.name = node.name


    elif node.Typedcl == "array":
        ent.array = True
        ent.name = node.name
        for child in reversed(node.children):
            # todo handle constant folding at compile time for expression, if not raise
            ent.arrays.append(child.name)
        return

    elif node.name == "pointer":
        ent.ptr += 1
        checkdecl(node.getchild(0),ent)
        return


    else:
        checkdecl(node.getchild(0),ent)
        return


class FunctionDefinitionNode(ASTNode):
    def handle(self, st: SymbolTable):

        entry = self.getchild(0).handle(st, True)  # declaration visit

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
                    raise SemanticsError(self.getchild(1).getchild(i).token,
                                         "parameterlist item does not match at index: " + str(i))

        newst = SymbolTable()
        newst.name = entry.name
        newst.return_type = entry.type
        newst.is_function = True
        st.addchild(newst)

        # checking if all declarations and adding into symbol table
        for par in self.getchild(1).children:

            if isinstance(par, DeclarationNode):
                par.handle(newst)
            elif par.Typedcl == None and par.name == 'empty':
                continue
            else:
                raise SemanticsError(self.token, "parameter name omitted")

        self.getchild(2).handle(newst)


class ReturnNode(ASTNode):
    # check if variable that is to be returned exists and matches return type
    def handle(self, st):
        stFunc = st.getFuncRoot()
        if stFunc.parent is None:
            raise SemanticsError(self.token, "Return in a non definition block")

        stParent = stFunc.parent
        returnType = ''
        funcReturnType = stParent.getVariableEntry(stFunc.name).type
        if len(self.children) == 0:
            # void return
            returnType = 4
            if funcReturnType != 4:
                SemanticsError(self.token, "Expected void return but got another type")
        else:
            self.getchild(0).handle(st, funcReturnType)  # evaluate expression statement






class EmptyNode(ASTNode):
    def handle(self,st):
        pass


class ArrayCallNode(ASTNode):
    def handle(self,st, type = None):
        entry = st.getVariableEntry(self.getchild(0).name)

        if not entry:
            SemanticsError(self.token,"Undifined array called")

        return entry.type

