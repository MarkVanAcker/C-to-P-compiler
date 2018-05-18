from src.astclasses.AST import *


class DeclarationNode(ASTNode):


    #maybe rewrite init to make it easier to process
    def handle(self, st):


        type = self.getchild(0)
        entr = Entry()

        if (type.token.type == CParser.CONST):
            entr.const = True
            entr.type = typecast[type.getchild(0).token.type]
        else:
            entr.type = typecast[type.token.type]


        if self.getchild(1).name == '=':
            entr.name = self.getchild(1).getchild(0).name
        else:
            entr.name = self.getchild(1).name


        if (st.LocalTableLookup(entr)):
            raise SemanticsError(self.token,"This variable was already declared in the local scope")
        if (st.GlobalTableLookup(entr)):
            #TODO : make general warning function that uses tokens and scope
            Warning(self.token,"Variable is hiding data")

        st.addEntry(entr)
        if self.getchild(1).name == '=':
            self.getchild(1).handle(st) #assignment visit


        return entr