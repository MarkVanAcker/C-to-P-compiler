from src.astclasses.AST import *


class DeclarationNode(ASTNode):


    #maybe rewrite init to make it easier to process
    def handle(self, st):


        type = self.getchild(0)
        entr = Entry()
        constt = False

        if (type.token.type == CParser.CONST):
            constt = True
            entr.type = type.getchild(0).Typedcl
        else:
            entr.type = type.Typedcl


        if self.getchild(1).name == '=':
            idnode = self.getchild(1).getchild(0)
        else:
            idnode = self.getchild(1)

        checkdecl(idnode,entr)

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


def checkdecl(node, ent):

    if node.Typedcl == "id":
        if ent.type is None:
            raise SemanticsError(node.token, "Declared variable void")
        ent.name = node.name
        return

    elif node.Typedcl == "func":

        ent.func = True
        ent.name = node.name


    elif node.Typedcl == "array":
        ent.name = node.name
        for child in reversed(node.children):
            # TODO: typecheck child.name and see scopecheck (if child.name == var)
            ent.type = "array(" + child.name + "," + str(ent.type) + ")"
        return

    elif node.name == "pointer":
        ent.ptr += 1
        checkdecl(node.getchild(0),ent)
        return


    else:
        checkdecl(node.getchild(0),ent)
        return