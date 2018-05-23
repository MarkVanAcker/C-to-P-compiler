from src.astclasses.AST import *


class DeclarationNode(ASTNode):


    #maybe rewrite init to make it easier to process
    def handle(self, st):

        reservedKeys = ["void", "int", "void", "bool", "float", "char", "default", "do", "double" , "long" , "goto", "case", "extern", "enum", "sizeof", "struct" "if", "else", "where", "for", "break", "continue", "return", "const"]


        type = self.getchild(0)
        entr = Entry()
        constt = False

        if (type.token.type == CParser.CONST):
            constt = True
            entr.type = type.getchild(0).Typedcl
        else:
            entr.type = type.Typedcl



        if self.getchild(1).name == '=':
            node:ASTNode = self.getchild(1).getchild(0)
            entr.name = node.name
            if node.Typedcl == 'func':
                raise SemanticsError(node.token, "Can not assign to a function declaration")

        else:
            entr.name = self.getchild(1).name


        if entr.name in reservedKeys:
            raise SemanticsError(self.token, "Using keyword as variable name")


        if (st.LocalTableLookup(entr)):
            raise SemanticsError(self.token,"This variable was already declared in the local scope")
        if (st.GlobalTableLookup(entr)):
            #TODO : make general warning function that uses tokens and scope
            Warning(self.token,"Variable is hiding data")

        st.addEntry(entr)
        if self.getchild(1).name == '=':
            self.getchild(1).handle(st) #assignment visit


        entr.const = constt

        return entr