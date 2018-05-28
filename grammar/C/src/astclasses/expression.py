from src.astclasses.AST import *
from src.astclasses.atomictypes import TypeCheck, ConstantNode, FunctionCallNode, IDNode, ArrayCallNode



##### pretty sure this one should be refactored ####

#check if every variable that is used exists and do type checking for conversions
#also add constant folding

class ExpressionNode(ASTNode):

    def handle(self, st, type = None):

        if type is BooleanType:
            raise SemanticsError(self.token, "Expression does not evaluate boolean types, only numeric operants")


        if self.name == 'empty' or len(self.children) == 0:
            return 4


        #
        # HANDLE LEFT VALUE OF THE EXPRESSION
        #


        # no L-value to assign to OR no type reference on the left side.   EG  if(3 < 5.0)
        # does not happen anymore
        node = self.getchild(0)
        if type == None:
            # variable
            if node.Typedcl == 'id':
                entry = st.getVariableEntry(node.name)
                if entry is None:
                    raise Exception("Error: undeclared variable (first use in this function)")
                type = entry.type

            # constant value (right?)
            else:
                type = node.Typedcl



        else:
            if isinstance(node,IDNode) or isinstance(node,ConstantNode) or isinstance(node,ArrayCallNode)or isinstance(node,FunctionCallNode):
                TypeCheck(node, st, type)
            else:
                node.handle(st, type)  # expression visit


        if len(self.children) == 1:
            return type

        #
        # HANDLE RIGHT VALUE OF THE EXPRESSION
        #

        node = self.getchild(1)
        if isinstance(node,IDNode) or isinstance(node,ConstantNode) or isinstance(node,ArrayCallNode)or isinstance(node,FunctionCallNode):
            TypeCheck(node,st,type)
        else:
            node.handle(st,type) #expression visit

        return type



class ComparisonNode(ExpressionNode):

    def handle(self, st, type=None):

        #check done at conditional statement

        #if type is not BooleanType:
        #   raise SemanticsError(self.token,"Condition statement does not evaluate to a boolean type")

        if self.name == 'empty' or len(self.children) == 0:
            raise SemanticsError(self.token, "Empty conditional statement")
            # todo true ?

        if len(self.children) != 2:
            raise SemanticsError(self.token,"expected comparison of 2 nodes (no boolean support)  2 < 4 == true not possible")

        return super(ComparisonNode, self).handle(st) # handle typecheck the same way as expr



class AdditionNode(ExpressionNode):

    def handle(self,st, type = None):
        return super(AdditionNode, self).handle(st,type)

    def getCode(self):

        inl = InstructionList()

        inl.AddInstruction(self.getchild(0).getCode(self.symbtable))
        inl.AddInstruction(self.getchild(1).getCode(self.symbtable))

        inl.AddInstruction(Add(self.getchild(0).Typedcl))

        return inl


class SubtractionNode(ExpressionNode):

    def handle(self,st, type = None):
        return super(SubtractionNode, self).handle(st, type)

    def getCode(self):

        inl = InstructionList()

        inl.AddInstruction(self.getchild(0).getCode(self.symbtable))
        inl.AddInstruction(self.getchild(1).getCode(self.symbtable))

        inl.AddInstruction(Subtract(self.getchild(0).Typedcl))

        return inl


class MultiplyNode(ExpressionNode):

    def handle(self,st, type = None):
        return super(MultiplyNode, self).handle(st, type)

    def getCode(self):

        inl = InstructionList()

        inl.AddInstruction(self.getchild(0).getCode(self.symbtable))
        inl.AddInstruction(self.getchild(1).getCode(self.symbtable))

        inl.AddInstruction(Multiply(self.getchild(0).Typedcl))

        return inl


class DivideNode(ExpressionNode):

    def handle(self,st, type = None):
        return super(DivideNode, self).handle(st, type)

    def getCode(self):

        inl = InstructionList()

        inl.AddInstruction(self.getchild(0).getCode(self.symbtable))
        inl.AddInstruction(self.getchild(1).getCode(self.symbtable))

        inl.AddInstruction(Divide(self.getchild(0).Typedcl))

        return inl







class AssignmentNode(ASTNode):
    #check if L-value and R-value are ok
    def handle(self, st):

        self.symbtable = st
        # left side must be l-value
        # is l-value memory allocatable variable only (array included)
        entry = st.getVariableEntry(self.getchild(0).name)
        if entry is None:
            raise Exception("Error: undeclared varaible (first use in this function)")
        returnType = entry.type

        # Evaluate R-value with given l-value type

        if  isinstance(self.getchild(1),ExpressionNode):
            self.getchild(1).handle(st, returnType) #expression visit
        else:
            TypeCheck(self.getchild(1),st,returnType)



    def getCode(self):

        inl = InstructionList()

        inl.AddInstruction(self.getchild(0).getL(self.symbtable))

        inl.AddInstruction(self.getchild(1).getCode(self.symbtable))

        inl.AddInstruction(StoreStack(self.getchild(0).Typedcl))

        return inl



















