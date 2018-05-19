from src.astclasses.AST import *



class ConditionNode(ASTNode):
    #typecheck condition and validity
    def handle(self,st):
        return self.getchild(0).handle(st,BooleanType) #expression visit

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
