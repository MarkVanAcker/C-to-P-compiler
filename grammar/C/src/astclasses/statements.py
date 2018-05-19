from src.astclasses.AST import *
from src.astclasses.block import EmptyNode



class ConditionNode(ASTNode):
    #typecheck condition and validity
    def handle(self,st):
        print (self.getchild(0).__class__.__name__)
        if isinstance(self.getchild(0) ,EmptyNode):
            raise SemanticsError(self.token,"Empty conditional statement not supported")

        return self.getchild(0).handle(st,BooleanType) #expression visit

class ConditionalNode(ASTNode):
    #typecheck condition and validity
    def handle(self,st):
        return self.getchild(0).handle(st) #condition

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


        newst = SymbolTable()
        newst.name = "iteration"
        st.addchild(newst)
        self.getchild(1).handle(newst)
