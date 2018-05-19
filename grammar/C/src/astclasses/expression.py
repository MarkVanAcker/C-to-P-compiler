from src.astclasses.AST import *


class AdditionNode(ASTNode):

    def handle(self,st):
        #Jesse
        pass

    def getCode(self, env:SymbolTable):

        inl = InstructionList()

        inl.AddInstruction(self.getchild(0).getCode(env))
        inl.AddInstruction(self.getchild(1).getCode(env))

        inl.AddInstruction(Add(self.getchild(0).Typedcl))

        return inl


class SubtractionNode(ASTNode):

    def handle(self,st):
        #Jesse
        pass

    def getCode(self, env:SymbolTable):

        inl = InstructionList()

        inl.AddInstruction(self.getchild(0).getCode(env))
        inl.AddInstruction(self.getchild(1).getCode(env))

        inl.AddInstruction(Subtract(self.getchild(0).Typedcl))

        return inl


class MultiplyNode(ASTNode):

    def handle(self,st):
        #Jesse
        pass

    def getCode(self, env:SymbolTable):

        inl = InstructionList()

        inl.AddInstruction(self.getchild(0).getCode(env))
        inl.AddInstruction(self.getchild(1).getCode(env))

        inl.AddInstruction(Multiply(self.getchild(0).Typedcl))

        return inl


class DivideNode(ASTNode):

    def handle(self,st):
        #Jesse
        pass

    def getCode(self, env:SymbolTable):

        inl = InstructionList()

        inl.AddInstruction(self.getchild(0).getCode(env))
        inl.AddInstruction(self.getchild(1).getCode(env))

        inl.AddInstruction(Divide(self.getchild(0).Typedcl))

        return inl







class AssignmentNode(ASTNode):
    #check if L-value and R-value are ok
    def handle(self, st):
        # left side must be l-value
        # is l-value memory allocatable variable only (array included)
        entry = st.getVariableEntry(self.getchild(0).name)
        if entry is None:
            raise Exception("Error: undeclared varaible (first use in this function)")
        returnType = entry.type

        # Evaluate R-value with given l-value type
        self.getchild(1).handle(st, returnType) #expression visit



    def getCode(self, env:SymbolTable):

        inl = InstructionList()

        inl.AddInstruction(self.getchild(0).getL(env))

        inl.AddInstruction(self.getchild(1).getCode(env))

        inl.AddInstruction(StoreStack(self.getchild(0).Typedcl))

        return inl



















##### pretty sure this one should be refactored ####

#check if every variable that is used exists and do type checking for conversions
#also add constant folding

class ExpressionNode(ASTNode):

    def handle(self, st, type = None):

        if self.name == 'empty' or len(self.children) == 0:
            return 4


        #
        # HANDLE LEFT VALUE OF THE EXPRESSION
        #


        # no L-value to assign to OR no type reference on the left side.   EG  if(3 < 5.0)
        node = self.getchild(0)
        if type == None:
            # variable
            if node.Typedcl == 'id':
                entry = st.getVariableEntry(node.name)
                if entry == False:
                    raise Exception("Error: undeclared varaible (first use in this function)")
                type = entry.type

            # constant value (right?)
            else:
                type = typecast[node.token.type]

        # supertype given for the expression.    EG int var = 1 + 5;
        # typecheck left operant
        else:
            if node.Typedcl == 'id' or node.Typedcl == 'intconst' or node.Typedcl == 'floatconst' or node.Typedcl == 'charconst':
                print("22")
                TypeCheck(node, st, type)
            else:
                node.handle(st, type)  # expression visit


        if len(self.children) == 1:
            return type

        #
        # HANDLE RIGHT VALUE OF THE EXPRESSION
        #

        node = self.getchild(1)
        if node.Typedcl == 'id' or node.Typedcl == 'intconst' or node.Typedcl == 'floatconst' or node.Typedcl == 'charconst':
            print("22")
            TypeCheck(node,st,type)
        else:
            node.handle(st,type) #expression visit

        return type

