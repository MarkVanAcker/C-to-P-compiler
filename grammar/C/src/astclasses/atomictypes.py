from src.astclasses.AST import *
from copy import deepcopy as dp

class IDNode(ASTNode):
    def handle(self, st, type=None):

        self.symbtable = st # symbol table link
        # typecheck

        entry = self.symbtable.getVariableEntry(self.name)


        if entry is None or entry.func:
            raise SemanticsError(self.token, "Usage of undefined variable \'" + self.name + "\'")

        if type is not None:
            TypeCheck(self, st, type)

        if entry.array == True:
            e = Entry()
            e.ptr = entry.ptr
            e.name = entry.name
            e.params = entry.params
            e.type = entry.type
            entry = e


        return entry






    def getCode(self):


        if self.symbtable is None:
            self.symbtable = self.par.symbtable

        glob = self.symbtable.isGlobal(Entry(self.name))
        entr = self.symbtable.GlobalTableLookup(Entry(self.name))

        if entr.array:
            return self.getLValue()

        scopeval = 0
        if glob:
            scopeval = 1  # global scope

        addr = self.symbtable.getLvalue(self.name)
        t = self.symbtable.getType(self.name)

        ins = InstructionList()
        ins.maxStackSpace = 1
        ins.AddInstruction(ProcedureLoadValue(t,glob,addr))
        return ins

    def getLValue(self):


        if self.symbtable is None:
            self.symbtable = self.par.symbtable

        glob = self.symbtable.isGlobal(Entry(self.name))
        scopeval = 0
        if glob:
            scopeval = 1  # global scope


        ins = InstructionList()
        ins.maxStackSpace = 1
        ins.AddInstruction(ProcedureLoadAddress(scopeval,self.symbtable.getLvalue(self.name)))
        return ins




class ConstantNode(ASTNode):


    # typecheck the node
    def handle(self,st,type=None):
        if type is not None:
            TypeCheck(self,st,type)

        e = Entry()
        e.ptr = 0
        e.type = self.Typedcl
        return e

    def getCode(self, env:SymbolTable = None):
        ins = InstructionList()
        ins.maxStackSpace = 1

        if isinstance(self.Typedcl, CharacterType):
            ins.AddInstruction(LoadConstant(self.Typedcl, ord(self.name)))
        else:
            ins.AddInstruction(LoadConstant(self.Typedcl,self.name))
        return ins





def TypeCheck(node : ASTNode, st, t):


    '''     ConstantNode
            IDNode
            ArrayCallNode
            ExpressionNode will not be called from here
            FunctionCallNode
    '''

    node.symbtable = st

    # variable
    if isinstance(node,IDNode):
        entry = st.getVariableEntry(node.name)
        if entry is None:
            raise SemanticsError(node.getToken(),"undeclared variable")
        Ltype = entry.type
        if not isinstance(Ltype, type(t)): # keeping void for what it is
            raise SemanticsError(node.getToken(),"No dynamic conversion supported")

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
            raise SemanticsError(node.getToken(), "No dynamic conversion supported")


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
        if not isinstance(t, type(node.handle(st).type)): # let array return type
            raise SemanticsError(node.getToken(), "No dynamic conversion supported")

    else:
        # should not happen
        raise SemanticsError(node.getToken(), "unknown entity")

class TypeNode(ASTNode):
    def handle(self,st):
        pass



class ParamNode(ASTNode):

    # handles declaration and definition parameters
    # 3 kinds, int , int a , const/* combination
    # return a parameter list with the types from each parameter

    def handle(self,st = None,definition = False):

        self.symbtable = st

        paramlist = []
        for param in self.children:
            if isinstance(param,EmptyNode):
                continue

            if definition == True:
                # in a definition each parameter is a declaration (int a)
                if not isinstance(param,DeclarationNode):
                    raise SemanticsError(param.getToken(), "Parameter name ommitted")



            if isinstance(param, TypeNode):
                print(param.name)
                e = None
                if (param.isconst == True):
                    print("PARAM IS CONST")
                    # const is a seperate node, take child
                    p = param.ptrog
                    param = param.getchild(0)
                    e = Entry(param.name,param.Typedcl)
                    e.const = True
                    e.ptr = p

                else:
                    # type from node
                    e = Entry(param.name,param.Typedcl)
                    e.ptr = param.ptrog
                print(param.ptrog)
                paramlist.append(e)

            else:
                # eg array
                paramlist.append(param.handle(SymbolTable()))
        return paramlist

    def getCode(self):

        for child in self.children:
            child.symbtable = self.symbtable
            child.getCode()


class FunctionCallNode(ASTNode):
    def handle(self,st,type = None):
        #
        # Look up is function is defined, later check is arguments are correct, we can not convert
        #

        self.symbtable = st

        if isinstance(self.getchild(0),AddressNode):
            raise  SemanticsError(self.getToken(), "No support for addressing on return node, also bad/useless coding")

        entry = st.getVariableEntry(self.getchild(0).name)

        self.entry = entry

        if not entry:
            raise SemanticsError(self.getToken(), "undefined reference to '"+ self.getchild(0).name + "'")

        if not entry.func:
            raise SemanticsError(self.getToken(), "Calling uncallable object")

        #functie moet niet gedefinieerd zijn om te kunnen callen
        #if not entry.defined:
        #    raise SemanticsError(self.getToken(), "Calling undefined function")

        print("FUNC PPAR", entry.params)

        self.getchild(1).handle(st,entry.params) # arguments node typechecks each parameter

        return entry


    def getCode(self):
        ins = InstructionList()
        ins.AddInstruction(MarkStack(1))
        ins.AddInstruction(self.getchild(1).getCode())
        ins.AddInstruction(CallUserProcedure(len(self.getchild(1).children),Label("function_"+str(self.entry.name))))

        return ins



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
                Deref addres
        '''

        self.symbtable = st

        if typelist is None: # nothing to check
            return


        # typelist are entries


        # if there are no parameters, no arguments will make a empty node
        if len(typelist) == 0 and not isinstance(self.getchild(0),EmptyNode):
            raise SemanticsError(self.getToken(),"Incorrect number of arguments given in functioncall")

        if len(typelist) == 0 and len(self.children) == 1 and isinstance(self.getchild(0),EmptyNode):
            return

        if len(typelist) != len(self.children):
            raise SemanticsError(self.getToken(), "Funcall has not the same number of arguments as declaration")

        index = 0
        for arg in self.children:
            arg.symbtable = st

            entry = None

            if isinstance(arg,ConstantNode) or isinstance(arg,IDNode) or isinstance(arg,FunctionCallNode) or isinstance(arg,ArrayCallNode): # constant node handle
                entry = arg.handle(st,typelist[index].type)

                # checking pointer levels
                if typelist[index].ptr != entry.ptr:
                    raise SemanticsError(self.getchild(1).getToken(), "Pointer referces not correct in variable")

            elif arg.name == "ExpressionNode" and arg.comp == True:
                raise SemanticsError(arg.getToken(), "No boolean types evaluated in funccal argument")
            elif arg.name == "ExpressionNode" and arg.comp == False and typelist[index].ptr == 0:
                arg.handle(st,typelist[index].type)
            elif arg.name == "ExpressionNode" and arg.comp == False and typelist[index].ptr != 0:
                raise SemanticsError(arg.getToken(), "Expression in funccal argument can not evaluate addresses")

            elif isinstance(arg,DerefNode) or isinstance(arg,AddressNode):
                entry = arg.handle(st, [typelist[index].type,typelist[index].ptr])


            index += 1




    def getCode(self):
        ins = InstructionList()

        for child in self.children:
            ins.AddInstruction(child.getCode())

        return ins




class DeclarationNode(ASTNode):


    #maybe rewrite init to make it easier to process
    def handle(self, st, definition = False):

        self.symbtable = st

        reservedKeys = ["void", "int", "void", "bool", "float", "char", "default", "do", "double" , "long" , "goto", "case", "extern", "enum", "sizeof", "struct" "if", "else", "where", "for", "break", "continue", "return", "const"]

        # get type and create entry
        type = self.getchild(0)
        type.symbtable = st
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
                raise SemanticsError(idnode.getToken(), "Can not assign to a function declaration")

        else:
            idnode = self.getchild(1)

        if idnode.name in reservedKeys:
            raise SemanticsError(self.getToken(),"Can not use reserved keyword for variable name")

        if idnode.Typedcl == 'func' and st.parent is not None:
            raise SemanticsError(idnode.getToken(), "Function declaration must be in global scope")


        idnode.symbtable = st
        checkdecl(idnode,entr,st) # set entry values

        addentry = True

        # do we find an entry with that name
        entryfound = st.LocalTableLookup(entr)
        if(entryfound is not None):
            if (entryfound.func == False):
                raise SemanticsError(self.getToken(),"This variable was already declared in the local scope")
            elif (entryfound.func and not entryfound.defined and definition): # allow if function is getting defined (after decl)
                entryfound.defined = True
                addentry = False
                entr = entryfound
            elif (entryfound.func and entryfound.defined and definition):
               raise SemanticsError(self.getToken(), "Redefinition of function")
            else:
               raise SemanticsError(self.getToken(), "Redeclaration of function")


        # variables in higher scopes
        # fucntions are only allowed in global
        entryfoundglobal = st.GlobalTableLookup(entr)
        if (entryfoundglobal is not None and entryfoundglobal != entryfound): # if both not none and we found an entry in global scope but not in local
            #entr = entryfoundglobal
            if (entryfoundglobal.func == False):
                Warning(idnode.getToken(),"%s is hiding variable" % entr.name)
            else:
                Warning(idnode.getToken(),"%s is hiding function" % entr.name)



        if addentry:
            st.addEntry(entr)
            if self.getchild(1).name == '=':  # can only get at this statement if it is a variable (not a func)
                self.getchild(1).handle(st)  # assignment visit before setting const
            entr.const = constt
            # if function add params
            if entr.func == True and not definition:
                self.par.children.remove(self)
                if len(idnode.children) > 0:
                    paramlist = idnode.getchild(0).handle() # different place if decl , and if defin
                    for item in paramlist:
                        entr.params.append(item)
            elif entr.func == True and definition:
                paramlist = self.par.getchild(1).handle(st,True)
                for item in paramlist:
                    entr.params.append(item)


            # add parameters to the entry, so we can check on later calls

        self.entry = entr

        return entr

    def getCode(self):

        self.symbtable.addSymbol(self.entry.name)

        #if its an assignment assign directly otherwise assign to zero
        if self.getchild(1).name == '=':
            return self.getchild(1).getCode()
        else:

            default = 0
            t = self.symbtable.getType(self.entry.name)
            addr = self.symbtable.getLvalue(self.entry.name)
            if isinstance(t,RealType):
                default = 0.0

            ins = InstructionList()
            ins.AddInstruction(LoadConstant(t,default))
            ins.AddInstruction(ProcedureStore(t,0,addr))

            return ins

def checkdecl(node : ASTNode, ent, st = None):

    if node.Typedcl == "id":
        if ent.type is None:
            raise SemanticsError(node.getToken(), "Declared variable void")
        ent.name = node.name
        ent.ptr = node.ptrog
        node.ptrcount = 0
        return

    elif node.Typedcl == "func":

        if node.name in ["scanf","printf"] and st.io:
            raise SemanticsError(node.getToken(),"Redeclaration of existing function")

        ent.func = True
        ent.name = node.name
        ent.ptr = node.ptrog


    elif node.Typedcl == "array":
        ent.array = True
        ent.name = node.name
        ent.ptr = node.ptrog + 1
        node.ptrcount = 0
        if len(node.children) > 1:
            raise SemanticsError(node.getToken(), "No support for multidimensional arrays")

        for child in reversed(node.children): # handle each ' [ x ] '
            # todo handle constant folding at compile time for expression, if not raise IDNODE?
            if child.name == "ExpressionNode" and child.comp == False:
                child.handle(node.symbtable, IntegerType())
                ent.arrays.append(child.result)
            elif child.name == "ExpressionNode" and child.comp == True:
                raise SemanticsError(child.getToken(), "Array does not support boolean evaluation for array size")
            else:
                if not isinstance(child.Typedcl,type(IntegerType())): # only constants pass here
                    raise SemanticsError(child.getToken(),"invalid array size type")
                ent.arrays.append(int(child.name))
        ent.arrays.reverse()
        return


    else:
        # not sure what this is
        checkdecl(node.getchild(0),ent)
        return


class FunctionDefinitionNode(ASTNode):
    def handle(self, st: SymbolTable):

        if st.parent is not None:
            raise SemanticsError(self.getToken(), "Definition must be in global scope")

        self.symbtable = st
        entry = self.getchild(0).handle(st, True)  # declaration visit for a definition
        # important: it is not required to check for const for the parameters, only usefull at definition, can defer in decl and def arg list

        # check return types
        node = self.getchild(0).getchild(0)
        if isinstance(node,TypeNode) and node.isconst == True:
            node = node.getchild(0)


        if str(entry.type)!= str(node.Typedcl):
            raise SemanticsError(node.getToken(), "Conflict for types: " + entry.name)
        else:
            #pointer level is correct
            print("WUT", entry.ptr, self.getchild(0).getchild(1).ptrcount)
            if entry.ptr != self.getchild(0).getchild(1).ptrcount:
                raise SemanticsError(node.getToken(), "Confict for types (pointer): " + entry.name)

        # check the entry paramlist if it matches ( only typechecking )
        paramlist = self.getchild(1).handle(st,True)
        print("curr paramlist", paramlist)
        if len(paramlist) != len(entry.params):
            raise SemanticsError(self.getToken(), "parameterlist does not match in size")
        else:
            for i in range(len(paramlist)):
                print("PP" ,paramlist, entry.params)
                if not paramlist[i].typecompare(entry.params[i]):
                    raise SemanticsError(self.getchild(1).getchild(i).getToken(), "parameterlist item does not match at index: " + str(i))

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

            print(par)
            if isinstance(par, DeclarationNode):
                par.handle(newst) # NEWST
            elif par.Typedcl == None and par.name == 'empty':
                continue
            else:
                raise SemanticsError(par.getToken(), "parameter name omitted")

        for ent in newst.entries: # codegen reasons
            ent.array = False

        self.getchild(2).handle(newst) # block traverse

        entry.defined = True




    def getCode(self):


        newst = self.getchild(2).symbtable

        newst.setEnvironment()

        self.getchild(1).symbtable = newst

        #initialize
        self.getchild(1).getCode()

        ins = InstructionList()
        ins.AddInstruction(Label("function_"+self.funcinfo.name))


        tempins = self.getchild(2).getCode()

        ins.AddInstruction(SetPointers(tempins.maxStackSpace,newst.getRequiredSpace()))

        ins.AddInstruction(tempins)

        if self.funcinfo.type is None:
            ins.AddInstruction(ReturnNoResult())

        ins.AddInstruction(Halt())


        return ins





class ReturnNode(ASTNode):
    # check if variable that is to be returned exists and matches return type
    def handle(self, st):

        self.symbtable = st

        stFunc = st.getFuncRoot()
        if stFunc.parent is None:
            raise SemanticsError(self.getToken(), "Return in a non definition block")

        stParent = stFunc.parent
        funcReturnType = stParent.getVariableEntry(stFunc.name).type # scope is under global scope, can only define in global scope

        #voor codegen
        self.fr = funcReturnType

        funcpointer = stParent.getVariableEntry(stFunc.name).ptr
        if len(self.children) == 0:
            # void return
            if funcReturnType is not None: # void is None type (0 children on return statement (empty expr)
                raise SemanticsError (self.getToken(), "Expected a non void return type but got a void type")

        else:

            print(funcpointer, "FROM FUNC RETURN", self.getchild(0).name)

            # Evaluate R-value with given l-value type
            # handle has to take into account the pointer levels and accessor node

            # do not want to do calculations with addresses
            if self.getchild(0).name == "ExpressionNode" and funcpointer > 0:
                raise SemanticsError(self.getchild(0), "Not alllowed to assign an expression to an address")
            print([funcReturnType, funcpointer])

            if isinstance(self.getchild(0), DerefNode) or isinstance(self.getchild(0), AddressNode):
                self.getchild(0).handle(st, [funcReturnType, funcpointer])
            elif isinstance(self.getchild(0), IDNode) or isinstance(self.getchild(0), ConstantNode) or isinstance(self.getchild(0), ArrayCallNode):
                # could also just be an idnode as rvalue of assignment which can be a counter (without * or &) such as int ** ptr2 = ptr -> ptr is pointer

                # checking return type and retrieve entry
                entry = self.getchild(0).handle(st, funcReturnType)

                # checking pointer levels
                if funcpointer != entry.ptr:
                    raise SemanticsError(self.getchild(0).getToken(), "Pointer referces not correct in variable")


            else:  # expression / arraycall
                self.getchild(0).handle(st, funcReturnType)


    def getCode(self):
        if len(self.children) == 0 or self.fr is None:
            return ReturnNoResult()
        else:
            ins = InstructionList()
            ins.AddInstruction(self.children[0].getCode())
            ins.AddInstruction(ProcedureStore(self.fr,0,0))
            ins.AddInstruction(ReturnResult())
            return ins


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


        if entry is None or entry.func:
            raise SemanticsError(self.getToken(),"Undefined variable called")
        if entry.ptr < 1  or entry.func:
            raise SemanticsError(self.getToken(),"Calling array operator on invalid type")




        # array calls int types ?
        currentnode = self

        # todo if you return an array its a pointer, if all args given its an type const value
        index = 1
        while True:
            currentnode.symbtable = st
            if currentnode.getchild(1).name == "ExpressionNode" and currentnode.getchild(1).comp == False:
                currentnode.getchild(1).handle(st,IntegerType()) # interger for indexing
            elif currentnode.getchild(1).name == "ExpressionNode" and currentnode.getchild(1).comp == True:
                raise SemanticsError(currentnode.getchild(1).getToken(), "Array does not evaluate boolean types as argument")

            else:
                # must be const of id (const will be fuckin annoying)
                #todo const on exp and constant values  (like 5)
                if not isinstance(currentnode.getchild(1).Typedcl, IntegerType): # if not expression
                    raise SemanticsError(currentnode.getchild(1).getToken(),"Expected integertype at arraycallindex")

            if currentnode != rootnode:
                currentnode = currentnode.getchild(0) # keep going
            if isinstance(currentnode,DerefNode) or isinstance(currentnode,AddressNode):
                currentnode.handle(st,[entry.type,entry.ptr])
                break
            else:
                break
            index +=1


        #if len(entry.arrays) < index:
        #    # doing array[4][5] and calling array[x][c][y]
        #    raise SemanticsError(self.getToken(),'Accessing undefined memory (accessing an dimension from array that was not created')

        e = Entry()
        e.ptr = entry.ptr - 1
        e.name = entry.name
        e.params = entry.params
        e.type = entry.type

        self.entry = e

        return e


    def getCode(self):

        ins = InstructionList()
        ins.maxStackSpace = 1
        if self.entry.array:
            ins.AddInstruction(self.getchild(0).getLValue())
        else:
            ins.AddInstruction(self.getchild(0).getCode())

        ins.AddInstruction(self.getchild(1).getCode())
        ins.AddInstruction(IndexComp(1))
        ins.AddInstruction(LoadIndirectly(self.entry.type))

        return ins



class DerefNode(ASTNode):

    def handle(self,st,type = None):

        self.symbtable = st
        if len(self.children) ==0 :
            # should not happen
            raise SemanticsError(self.getToken(), "deference called of non object")

        entry = None
        node = self.getchild(0)
        if not isinstance(node,IDNode) and not isinstance(node,ArrayCallNode) and not (node,FunctionCallNode):
            raise SemanticsError(node.getToken(),"Calling deref of address object")
        else:
            if node.name == 'scanf' or node.name == 'printf':
                raise SemanticsError(self.token, "Sneaky deferencing at hardcoded printf/scanf node, we do not support that")

            if isinstance(node,IDNode) or isinstance(node,ArrayCallNode) or (node,FunctionCallNode):
                node.ptrcount = -(self.ptrcount) # setting number of pointers
                print("Setting" , node.name ,node.ptrcount)
                entry = node.handle(st,type[0])
            if isinstance(node,ArrayCallNode):
                node.ptrcount = -(self.ptrcount)  # setting number of pointers
                entry = node.handle(st, type[0])


        print(type[1], entry.ptr + node.ptrcount)
        if type[1] != entry.ptr + node.ptrcount:
            raise SemanticsError(node.getToken(),"Incorrect pointer types of assignment or in expression")

        #for codegeneration
        self.entry = dp(entry)
        self.entry.ptr -= self.ptrcount

        return entry




    def getCode(self):

        entry = None
        if isinstance(self.getchild(0),ArrayCallNode) or isinstance(self.getchild(0),FunctionCallNode):
            entry = self.getchild(0).entry


        else:
            entryname = self.getchild(0).name
            entry = self.symbtable.GlobalTableLookup(Entry(entryname))

        ins = InstructionList()
        ins.AddInstruction(self.getchild(0).getCode())
        for c in range(self.ptrcount):
            if(c+1 == entry.ptr):
                ins.AddInstruction(LoadIndirectly(entry.type))
            else:
                ins.AddInstruction(LoadIndirectly(AddressType()))

        return ins


class AddressNode(ASTNode):

    def handle(self,st,type = None):
        if len(self.children) ==0 :
            # should not happen
            raise SemanticsError(self.getToken(), "Address called of non object")

        entry = None
        if not isinstance(self.getchild(0),IDNode):
            raise SemanticsError(self.getchild(0).getToken(),"Calling address of non variable")
        else:
            node = self.getchild(0)
            if isinstance(node, IDNode) or isinstance(node, ArrayCallNode):
                node.ptrcount = 1  # setting number of pointers
                print("Setting", node.name, node.ptrcount)
                entry = node.handle(st, type[0])
            if isinstance(node, ArrayCallNode):
                node.ptrcount = -(self.ptrcount)  # setting number of pointers
                entry = node.handle(st, type[0])


        print(type[1],entry.ptr + self.getchild(0).ptrcount)
        if type[1] != entry.ptr + self.getchild(0).ptrcount:
            raise SemanticsError(self.getchild(0).getToken(),"Incorrect pointer types of assignment")

        self.entry = dp(entry)
        self.entry.ptr += 1

        return entry




    def getCode(self):
        if isinstance(self.getchild(0),IDNode):
            return self.children[0].getLValue()
        elif isinstance(self.getchild(0),ArrayCallNode):
            ins = self.getchild(0).getCode()
            ins.instructionlist.pop()
            return ins