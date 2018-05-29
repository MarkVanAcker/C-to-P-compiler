from src.astclasses.AST import *

class IDNode(ASTNode):
    def handle(self, st, type=None):

        self.symbtable = st # symbol table link

        # typecheck
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


    # typecheck the node
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
    if isinstance(node,IDNode):
        entry = st.getVariableEntry(node.name)
        if entry is None:
            raise SemanticsError(node.token,"undeclared variable")
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

    # constant value
    elif isinstance(node,ConstantNode):
        Ltype = node.Typedcl

        if not isinstance(Ltype, type(t)): # keeping void for what it is
            print("ERROR CONV", Ltype.__class__.__name__, type(t))
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

    # other callable types, arrays and functioncalls
    elif isinstance(node,ArrayCallNode) or isinstance(node,FunctionCallNode):
        if not isinstance(t, type(node.handle(st))): # let array return type
            Warning(node.token,"forced type conversion")
            raise SemanticsError(node.token, "No dynamic conversion supported")

    else:
        # should not happen
        raise SemanticsError(node.token, "unknown entity")

class TypeNode(ASTNode):
    def handle(self,st):
        pass


class ParamNode(ASTNode):

    # handles declaration and definition parameters
    # 3 kinds, int , int a , const/* combination
    # return a parameter list with the types from each parameter

    def handle(self,st = None,definition = False):

        paramlist = []
        for param in self.children:
            if isinstance(param,EmptyNode):
                continue

            if definition == True:
                # in a definition each parameter is a declaration (int a)
                param = param.getchild(0)


            if isinstance(param, TypeNode):
                if (param.isconst == True):
                    # const is a seperate node, take child
                    paramlist.append(param.getchild(0).Typedcl)
                else:
                    # type from node
                    paramlist.append(param.Typedcl)

            else:
                # eg array
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

        if not entry.defined:
            raise SemanticsError(self.token, "Calling undefined function")

        self.getchild(1).handle(st,entry.params) # arguments node typechecks each parameter

        return entry.type



class ArgumentsNode(ASTNode):
    def handle(self,st, typelist = None):
        #
        # Resolve types from each argument and compare with tyeplist from definition
        #

        '''     ConstantNode
                IDNode
                ArrayCallNode checked on name return type
                ExpressionNode
                FunctionCallNode checked on name return type
        '''


        if typelist is None: # nothing to check
            return


        # if there are no parameters, no arguments will make a empty node
        if len(typelist) == 0 and not isinstance(self.getchild(0),EmptyNode):
            raise SemanticsError(self.token,"Incorrect number of arguments given in functioncall")

        index = 0
        for arg in self.children:
            if isinstance(arg,ConstantNode): # constant node handle
                if not isinstance(arg.Typedcl, type(typelist[index])):
                    raise (arg.token,"Do not support type conversion at funccal argument")
            elif isinstance(arg,IDNode): # IDnode handle
                entry = st.getVariableEntry(arg.name)
                if entry is None:
                    raise SemanticsError(arg.token, "Unknown variable")
                if not isinstance(entry.type, type(typelist[index])):
                    raise (arg.token, "Do not support type conversion at funccal argument")
            elif isinstance(arg, ArrayCallNode) or isinstance(arg, FunctionCallNode) or arg.name == "ExpressionNode": # other node handles that have children to call upon
                returntype = arg.handle(st)
                if not isinstance(returntype,type(typelist[index])):
                    raise (arg.token, "Do not support type conversion at funccal argument")

            index += 1




class DeclarationNode(ASTNode):


    #maybe rewrite init to make it easier to process
    def handle(self, st, definition = False):

        reservedKeys = ["void", "int", "void", "bool", "float", "char", "default", "do", "double" , "long" , "goto", "case", "extern", "enum", "sizeof", "struct" "if", "else", "where", "for", "break", "continue", "return", "const"]

        # get type and create entry
        type = self.getchild(0)
        entr = Entry()
        constt = False # we can assign a value and lock it after

        # const has extra node so take childs type
        if (type.token.type == CParser.CONST):
            constt = True
            entr.type = type.getchild(0).Typedcl
        else:
            entr.type = type.Typedcl


        idnode = None

        # assignment
        if self.getchild(1).name == '=':
            idnode = self.getchild(1).getchild(0)
            if idnode.Typedcl == 'func':
                raise SemanticsError(idnode.token, "Can not assign to a function declaration")

        else:
            idnode = self.getchild(1)

        if idnode.name in reservedKeys:
            raise SemanticsError(self.token,"Can not use reserved keyword for variable name")

        if idnode.Typedcl == 'func' and st.parent is not None:
            raise SemanticsError(idnode.token, "Function declararion must be in global scope")

        idnode.symbtable = st
        checkdecl(idnode,entr) # set entry values


        # do we find an entry with that name
        entryfound = st.LocalTableLookup(entr)
        if(entryfound is not None):
            if (entryfound.func == False):
                raise SemanticsError(self.token,"This variable was already declared in the local scope")
            elif (entryfound.func and not entryfound.defined and definition): # allow if function is getting defined (after decl)
                entryfound.defined = True
            elif (entryfound.func and entryfound.defined and definition):
               raise SemanticsError(self.token, "Redefinition of function")
            else:
               raise SemanticsError(self.token, "Redeclaration of function")



        addentry = True
        entryfound = st.GlobalTableLookup(entr)
        if (entryfound is not None):
            addentry = False # entry found no need to add one
            entr = entryfound
            if (entryfound.func == False):
                Warning(self.token,"%s is hiding variable" % entr.name)
            else:
                Warning(self.token,"%s is hiding function" % entr.name)






        if addentry:

            st.addEntry(entr)
            if self.getchild(1).name == '=':  # can only get at this statement if it is a variable (not a func)
                self.getchild(1).handle(st)  # assignment visit before setting const
            entr.const = constt
            # if function add params
            if entr.func == True and not definition:
                paramlist = idnode.getchild(0).handle() # different place if decl , and if defin
                for item in paramlist:
                    entr.params.append(item)
            elif entr.func == True and definition:
                paramlist = self.par.getchild(1).handle(st,True)
                for item in paramlist:
                    entr.params.append(item)
            # add parameters to the entry, so we can check on later calls

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
        for child in reversed(node.children): # handle each ' [ x ] '
            # todo handle constant folding at compile time for expression, if not raise IDNODE?
            if child.name == "ExpressionNode":
                child.handle(node.symbtable, IntegerType())
                ent.arrays.append(child.result)
            else:
                if not isinstance(child.Typedcl,type(IntegerType())): # only constants pass here
                    raise SemanticsError(child.token,"array argument not of integertype")
                ent.arrays.append(int(child.name))
        ent.arrays.reverse()
        print(ent.arrays)
        return

    elif node.name == "pointer":
        ent.ptr += 1
        checkdecl(node.getchild(0),ent)
        return


    else:
        # not sure what this is
        checkdecl(node.getchild(0),ent)
        return


class FunctionDefinitionNode(ASTNode):
    def handle(self, st: SymbolTable):


        if st.parent is not None:
            raise SemanticsError(self.token, "Definition must be in global scope")

        self.symbtable = st
        entry = self.getchild(0).handle(st, True)  # declaration visit for a definition

        # important: it is not required to check for const for the parameters, only usefull at definition, can defer in decl and def arg list

        # check the entry paramlist if it matches ( only typechecking )
        paramlist = self.getchild(1).handle(st,True)
        print("curr paramlist", paramlist)
        if len(paramlist) != len(entry.params):
            raise SemanticsError(self.token, "parameterlist does not match in size")
        else:
            for i in range(len(paramlist)):
                if str(paramlist[i]) != str((entry).params[i]): # could do it other way, works fine
                    raise SemanticsError(self.getchild(1).getchild(i).token, "parameterlist item does not match at index: " + str(i))

        # create new scope and traverse it
        newst = SymbolTable()
        newst.name = entry.name
        newst.return_type = entry.type
        newst.is_function = True
        st.addchild(newst)

        #for code generation
        self.funcinfo = entry

        # checking if all declarations and adding into symbol table of the new scope!
        for par in self.getchild(1).children:

            if isinstance(par, DeclarationNode):
                par.handle(newst) # NEWST
            elif par.Typedcl == None and par.name == 'empty':
                continue
            else:
                raise SemanticsError(self.token, "parameter name omitted")

        self.getchild(2).handle(newst) # block traverse

        entry.defined = True


    def getCode(self):
        maxstacksize = 0
        maxvarsize = 5

        maxvarsize += len(self.funcinfo.params)

        ins = InstructionList()
        ins.AddInstruction(Label("function_"+self.funcinfo.name))

        self.getchild(2).symbtable.variablestacksize = maxvarsize

        tempins = self.getchild(2).getCode()

        ins.AddInstruction(SetPointers(tempins.maxStackSpace,self.getchild(2).symbtable.variablestacksize))

        ins.AddInstruction(tempins)


        return ins





class ReturnNode(ASTNode):
    # check if variable that is to be returned exists and matches return type
    def handle(self, st):
        stFunc = st.getFuncRoot()
        if stFunc.parent is None:
            raise SemanticsError(self.token, "Return in a non definition block")

        stParent = stFunc.parent
        returnType = ''
        funcReturnType = stParent.getVariableEntry(stFunc.name).type # scope is under global scope, can only define in global scope
        if len(self.children) == 0:
            # void return
            if funcReturnType is not None: # void is None type (0 children on return statement (empty expr)
                raise SemanticsError (self.token, "Expected void return but got a type")
        else:
            self.getchild(0).handle(st, funcReturnType)  # evaluate expression statement


class EmptyNode(ASTNode):
    def handle(self,st):
        pass



class ArrayCallNode(ASTNode):
    def handle(self,st, type = None):

        #refactor node into 1 arraycall node leftmostchild id other child accessors

        rootnode = self
        while True:
            if not isinstance(rootnode.getchild(0), IDNode):
                rootnode = rootnode.getchild(0)
            else:
                break

        # leftbalanced tree with leftmost node having id
        entry = st.getVariableEntry(rootnode.getchild(0).name)

        if not entry:
            SemanticsError(self.token,"Undifined array called")


        # array calls int types ?
        currentnode = self

        # todo if you return an array its a pointer, if all args given its an type const value
        index = 1;
        while True:
            if currentnode.getchild(1).name == "ExpressionNode":
                currentnode.getchild(1).handle(st,IntegerType()) # interger for indexing
            else:
                # must be const of id (const will be fuckin annoying)
                #todo const on exp and constant values  (like 5)
                if not isinstance(currentnode.getchild(1).Typedcl, IntegerType): # if not expression
                    raise SemanticsError(currentnode.getchild(1).token,"Expected integertype at arraycallindex")

            if currentnode != rootnode:
                currentnode = currentnode.getchild(0) # keep going
            else:
                break
            index +=1

        if len(entry.arrays) < index:
            # doing array[4][5] and calling array[x][c][y]
            raise SemanticsError(self.token,'Accessing undefined memory (accessing an dimension from array that was not created')

        return entry.type

