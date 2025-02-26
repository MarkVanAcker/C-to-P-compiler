from src.astclasses.AST import *
from src.astclasses.block import EmptyNode
from src.astclasses.expression import ComparisonNode


class LabelFactory():


    def getIfendLabel(self):
        return Label("endif")

    def getIffalseLabel(self):
        return Label("falseif")

    def getWhilebeginLabel(self):
        return Label("beginwhile")

    def getWhileendLabel(self):
        return Label("endwhile")


class ConditionNode(ASTNode):
    #typecheck condition and validity
    def handle(self,st):

        self.symbtable = st
        self.getchild(0).symbtable = st

        if isinstance(self.getchild(0) ,EmptyNode):
            raise SemanticsError(self.getToken(),"Empty conditional statement not supported")

        # make sure it is a boolean exp if so expr visit it
        if not isinstance(self.getchild(0) ,ComparisonNode):
            raise SemanticsError(self.getToken(), "Expected comparison conditional statement which results in a boolean evaluation")

        save = self.getchild(0).handle(st) #comp expression visit


    def getCode(self):
        return self.children[0].getCode()

class ConditionalNode(ASTNode):
    #typecheck condition and validity
    def handle(self,st):
        self.getchild(0).handle(st) #condition

        self.symbtable = st

        for i in range(1,len(self.children)): # create a new st (block for if - else)
            newst = SymbolTable()
            newst.name = "condition"
            st.addchild(newst)
            self.getchild(i).handle(newst)

    def getCode(self):

        self.iffalse = LabelFactory().getIffalseLabel()
        self.ifend = None


        ins = InstructionList()

        ins.AddInstruction(self.children[0].getCode())
        ins.AddInstruction(ConditionalJump(self.iffalse))
        self.children[1].symbtable.setEnvironment()
        ins.AddInstruction(self.children[1].getCode())
        s1 = self.children[1].symbtable.getRequiredSpace()
        s2 = 0

        if(len(self.children) == 3):
            self.ifend = LabelFactory().getIfendLabel()
            ins.AddInstruction(UnconditionalJump(self.ifend))
        ins.AddInstruction(self.iffalse)
        if (len(self.children) == 3):
            self.children[2].symbtable.setEnvironment()
            ins.AddInstruction(self.children[2].getCode())
            ins.AddInstruction(self.ifend)
            s2 = self.children[2].symbtable.getRequiredSpace()

        if(self.symbtable.getRequiredSpace() < max(s1,s2)):
            self.symbtable.maxvariablestacksize = max(s1,s2)


        return ins


class WhileNode(ASTNode):

    #typecheck condition and validity
    def handle(self, st):
        #
        #  - validate condition
        #  - create new table and traverse block
        #

        self.symbtable = st

        # condition vist will validate and detect possible dead block code
        #TODO check if functionallity can be added
        if not self.getchild(0).handle(st): #conditionvisit
            pass

        # block traverse
        newst = SymbolTable()
        newst.name = "iteration"
        st.addchild(newst)
        self.getchild(1).handle(newst)


    def getCode(self):

        ins = InstructionList()

        self.beginlabel = LabelFactory().getWhilebeginLabel()
        self.endlabel = LabelFactory().getWhileendLabel()

        ins.AddInstruction(self.beginlabel)
        ins.AddInstruction(self.children[0].getCode())
        ins.AddInstruction(ConditionalJump(self.endlabel))
        self.children[1].symbtable.setEnvironment()
        ins.AddInstruction(self.children[1].getCode())
        s = self.children[1].symbtable.getRequiredSpace()
        ins.AddInstruction(UnconditionalJump(self.beginlabel))
        ins.AddInstruction(self.endlabel)
        if self.symbtable.getRequiredSpace() < s:
            self.symbtable.maxvariablestacksize = s

        return ins


