from src.astclasses.AST import *
from src.astclasses.atomictypes import TypeCheck, ConstantNode, FunctionCallNode, IDNode, ArrayCallNode, DerefNode, AddressNode



##### pretty sure this one should be refactored ####

#check if every variable that is used exists and do type checking for conversions
#also add constant folding


def fold(node1 : ASTNode,node2 : ASTNode,operant,typeval): # typecheck is already done in the expression visit returning result


        print("FOLD WITH TYPE ",typeval)

        if isinstance(typeval,CharacterType):
            raise SemanticsError(node2.getToken(),"Can not operate with char values, no usefull result")

        if isinstance(node1,ExpressionNode):
            node1.name = node1.result

        if isinstance(node2,ExpressionNode):
            node2.name = node2.result


        if operant == '*':
            if isinstance(typeval,IntegerType):
                return  int(int(node1.name) * int(node2.name))
            elif isinstance(typeval,RealType):
                return float(float(node1.name) * float(node2.name))
            else:
                raise SemanticsError(node1.getToken(),"operating with nonetypes")
        elif operant == '/':
            if isinstance(typeval, IntegerType):
                return int(int(node1.name) / int(node2.name))
            elif isinstance(typeval, RealType):
                return float(float(node1.name) / float(node2.name))
            else:
                raise SemanticsError(node1.getToken(), "operating with nonetypes")
        elif operant == '+':
            if isinstance(typeval, IntegerType):
                return int(int(node1.name) + int(node2.name))
            elif isinstance(typeval, RealType):
                return float(float(node1.name) + float(node2.name))
            else:
                print("TYPE",typeval)
                raise SemanticsError(node1.getToken(), "operating with nonetypes")
        elif operant == '-':
            if isinstance(typeval, IntegerType):
                return int(int(node1.name) - int(node2.name))
            elif isinstance(typeval, RealType):
                return float(float(node1.name) - float(node2.name))
            else:
                raise SemanticsError(node1.getToken(), "operating with nonetypes")



class ExpressionNode(ASTNode):

    def handle(self, st, type = None, folding = True):

        print("HERE")

        if type is BooleanType:
            raise SemanticsError(self.getToken(), "Expression does not evaluate boolean types, only numeric operants")


        if self.name == 'empty' or len(self.children) == 0:
            return None

        self.symbtable = st


        #
        # HANDLE LEFT VALUE OF THE EXPRESSION
        #


        # no L-value to assign to OR no type reference on the left side.   EG  if(3 < 5.0)
        # does not happen anymore
        node = self.getchild(0)
        node.symbtable = st


        if isinstance(node,AddressNode):
            raise SemanticsError(node.getToken(),"No addressing allowed in expression")

        node.symbtable = st
        entry = None
        temptype = None


        if isinstance(node, ConstantNode) or isinstance(node, IDNode) or isinstance(node,FunctionCallNode) or isinstance(node, ArrayCallNode):
            entry = node.handle(st,type)
            print("1 if found ", entry.type)
            temptype = entry.type

            # checking pointer levels must be 0
            print(entry.name,entry.ptr)
            if 0 != entry.ptr:
                raise SemanticsError(self.getchild(1).getToken(), "Pointer referces not correct in variable in expression")

        elif node.name == "ExpressionNode" and node.comp == True:
            raise SemanticsError(node.getToken(), "No boolean types evaluated in expression")
        elif node.name == "ExpressionNode" and node.comp == False:
            temptype = node.handle(st, type)

        elif isinstance(node, DerefNode):
            entry = node.handle(st, [type, 0])
            temptype = entry.type


        if type is None:
            type = temptype

        if len(self.children) == 1:
            return type


        print("TYPE IS NOT SET>LEFT HAND DONE ", type)
        print("I FOUND  ", temptype)


        #
        # HANDLE RIGHT VALUE OF THE EXPRESSION
        #

        node = self.getchild(1)
        node.symbtable = st


        if isinstance(node,AddressNode):
            raise SemanticsError(node.getToken(),"No addressing allowed in expression")

        entry = None

        if isinstance(node, ConstantNode) or isinstance(node, IDNode) or isinstance(node,FunctionCallNode) or isinstance(node, ArrayCallNode):
            entry = node.handle(st, type)

            # checking pointer levels must be 0
            if 0 != entry.ptr:
                raise SemanticsError(self.getchild(1).getToken(),
                                     "Pointer referces not correct in variable in expression")

        elif node.name == "ExpressionNode" and node.comp == True:
            raise SemanticsError(arg.getToken(), "No boolean types evaluated in expression")
        elif node.name == "ExpressionNode" and node.comp == False:
            node.handle(st, type)

        elif isinstance(node, DerefNode):
            entry = node.handle(st, [type, 0])



        if folding == False:
            self.type = type
            return type

        if (isinstance(self.getchild(0),ExpressionNode) and self.getchild(0).result is not None) or isinstance(self.getchild(0),ConstantNode): # compile time evalution of statement is possible
            if (isinstance(self.getchild(1),ExpressionNode) and self.getchild(1).result is not None) or isinstance(self.getchild(1),ConstantNode): # compile time evalution of statement is possible
                self.result = fold(self.getchild(0),self.getchild(1),self.operator,type)

                new = ConstantNode(self.result,self.getchild(0).token)
                new.Typedcl = type
                new.par = self.par
                self.par.children.insert(self.par.children.index(self),new)
                self.par.children.remove(self)
                self.clearchildren()

            else:

                #check null sequence
                if (self.operator == '+' and fold(self.getchild(0),ASTNode(0),self.operator,type) == 0) or (self.operator == '*' and fold(self.getchild(0),ASTNode(1),self.operator,type) == 1):
                    new = self.getchild(1)
                    new.par = self.par
                    self.par.children.insert(self.par.children.index(self), new)
                    self.par.children.remove(self)

                self.result = None
        elif (isinstance(self.getchild(1), ExpressionNode) and self.getchild(1).result is not None) or isinstance(self.getchild(1), ConstantNode):
            if (self.operator == '+' and fold(self.getchild(1), ASTNode(0), self.operator, type) == 0) or (
                    self.operator == '*' and fold(self.getchild(1), ASTNode(1), self.operator, type) == 1):
                new = self.getchild(0)
                new.par = self.par
                self.par.children.insert(self.par.children.index(self), new)
                self.par.children.remove(self)
        else:
            self.result = None

        self.type = type

        return type

    def getCode(self):
        inl = InstructionList()

        cleft = self.getchild(0).getCode()
        cright = self.getchild(1).getCode()
        inl.AddInstruction(cleft)
        inl.AddInstruction(cright)
        inl.maxStackSpace= max(cleft.maxStackSpace,1+cright.maxStackSpace)

        return inl

class ComparisonNode(ExpressionNode):

    def handle(self, st, type=None, l=[]):

        #check done at conditional statement

        #if type is not BooleanType:
        #   raise SemanticsError(self.token,"Condition statement does not evaluate to a boolean type")

        operatormap = {">" : Greater, "<" : Lesser, "==" : Equal, "<=": LesserOrEqual}

        self.symbtable = st

        if self.name == 'empty' or len(self.children) == 0:
            raise SemanticsError(self.token, "Empty conditional statement")
            # todo true ?

        if len(self.children) != 2:
            raise SemanticsError(self.token,"expected comparison of 2 nodes (no boolean support)  2 < 4 == true not possible")

        type = super().handle(st,None,False) # handle typecheck the same way as expr

        self.operator = operatormap[self.operator](type)

        return BooleanType() # we do not want boolean types in normal expressions (expect in conditional , but here comparison node must be topnode so it is ok

    def getCode(self):
        inl = super().getCode()
        inl.AddInstruction(self.operator)
        return inl



class AdditionNode(ExpressionNode):

    def handle(self,st, type = None):
        return super(AdditionNode, self).handle(st,type)

    def getCode(self):

        inl = super().getCode()
        inl.AddInstruction(Add(self.type))

        return inl


class SubtractionNode(ExpressionNode):

    def handle(self,st, type = None):
        return super(SubtractionNode, self).handle(st, type)

    def getCode(self):

        inl = super().getCode()

        inl.AddInstruction(Subtract(self.type))

        return inl


class MultiplyNode(ExpressionNode):

    def handle(self,st, type = None):
        return super(MultiplyNode, self).handle(st, type)

    def getCode(self):

        inl = super().getCode()

        inl.AddInstruction(Multiply(self.type))

        return inl


class DivideNode(ExpressionNode):

    def handle(self,st, type = None):
        return super(DivideNode, self).handle(st, type)


    def getCode(self):

        inl = super().getCode()

        inl.AddInstruction(Divide(self.type))

        return inl







class AssignmentNode(ASTNode):
    #check if L-value and R-value are ok
    def handle(self, st,type = None):
        print("ASSIGNMENT")

        self.symbtable = st
        # left side must be l-value
        # is l-value memory allocatable variable only (array included)
        self.getchild(0).symbtable = st
        self.getchild(1).symbtable = st
        entry = st.getVariableEntry(self.getchild(0).name)
        if entry is None:
            raise SemanticsError(self.getchild(0).getToken() ,"undeclared variable (first use in this function)")
        returnType = entry.type

        if entry.const:
            raise SemanticsError(self.getchild(0).getToken(), "trying to assign to const variable \'" + self.getchild(0).name+"\'")

        if entry.func:
            raise SemanticsError(self.getchild(0).getToken(), "trying to assign to function \'" + self.getchild(0).name+"\'")

        #for codegen
        self.entry = entry


        pointer = self.getchild(0).pointerlevel(st)  # get the pointer level is   >= 0
        print(pointer, "FROM ", self.getchild(0).name)

        # Evaluate R-value with given l-value type
        # handle has to take into account the pointer levels and accessor node

        # do not want to do calculations with addresses
        if isinstance(self.getchild(1),ExpressionNode) and pointer > 0:
            raise SemanticsError(self.getchild(1), "Not alllowed to assign an expression to an address")
        print([returnType,pointer])

        if isinstance(self.getchild(1),DerefNode) or isinstance(self.getchild(1),AddressNode):
            self.getchild(1).handle(st, [returnType,pointer])
        elif isinstance(self.getchild(1),IDNode) or isinstance(self.getchild(1),ConstantNode) or isinstance(self.getchild(1),ArrayCallNode) or isinstance(self.getchild(1),FunctionCallNode) :
            # could also just be an idnode as rvalue of assignment which can be a counter (without * or &) such as int ** ptr2 = ptr -> ptr is pointer

            # checking return type and retrieve entry
            ent = self.getchild(1).handle(st, returnType)

            #checking pointer levels
            if pointer != ent.ptr:
                raise SemanticsError(self.getchild(1).getToken(), "Pointer referces not correct in variable")


        elif isinstance(self.getchild(1),ExpressionNode) : # expression
            self.getchild(1).handle(st, returnType)

        # useless code elimination
        if isinstance(self.getchild(1),IDNode):
            if(self.getchild(1).name == entry.name):
                print("ELEMINATION")
                self.par.children.remove(self)





    def getCode(self):

        inl = InstructionList()

        glob = self.symbtable.isGlobal(self.entry)
        scopeval = 0
        if glob:
            scopeval = 1 #global scope

        addr = self.symbtable.getLvalue(self.entry.name)
        t = self.symbtable.getType(self.entry.name)

        inl.AddInstruction(self.getchild(1).getCode())

        inl.AddInstruction(ProcedureStore(t, scopeval, addr))

        return inl



















