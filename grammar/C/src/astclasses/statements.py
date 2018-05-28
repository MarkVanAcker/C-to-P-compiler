from src.astclasses.AST import *
from src.astclasses.block import EmptyNode
from src.astclasses.expression import ComparisonNode



class ConditionNode(ASTNode):
    #typecheck condition and validity
    def handle(self,st):
        print (self.getchild(0).__class__.__name__)
        if isinstance(self.getchild(0) ,EmptyNode):
            raise SemanticsError(self.token,"Empty conditional statement not supported")

        # make sure it is a boolean exp if so expr visit it
        if not isinstance(self.getchild(0) ,ComparisonNode):
            raise SemanticsError(self.token, "Expected comparison conditional statement which results in a boolean evaluation")

        return self.getchild(0).handle(st) #comp expression visit

class ConditionalNode(ASTNode):
    #typecheck condition and validity
    def handle(self,st):
        self.getchild(0).handle(st) #condition

        for i in range(1,len(self.children)): # create a new st (block for if - else)
            newst = SymbolTable()
            newst.name = "condition"
            st.addchild(newst)
            self.getchild(i).handle(newst)

class WhileNode(ASTNode):

    #typecheck condition and validity
    def handle(self, st):
        #
        #  - validate condition
        #  - create new table and traverse block
        #

        # condition vist will validate and detect possible dead block code
        #TODO check if functionallity can be added
        if not self.getchild(0).handle(st): #conditionvisit
            pass

        # block traverse
        newst = SymbolTable()
        newst.name = "iteration"
        st.addchild(newst)
        self.getchild(1).handle(newst)
