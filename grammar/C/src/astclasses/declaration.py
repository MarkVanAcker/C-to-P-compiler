from src.astclasses.AST import *
from src.astclasses.atomictypes import TypeNode


class DeclarationNode(ASTNode):


    #maybe rewrite init to make it easier to process
    def handle(self, st, definition = False):

        reservedKeys = ["void", "int", "void", "bool", "float", "char", "default", "do", "double" , "long" , "goto", "case", "extern", "enum", "sizeof", "struct" "if", "else", "where", "for", "break", "continue", "return", "const"]


        type = self.getchild(0)
        entr = Entry()
        constt = False

        if (type.token.type == CParser.CONST):
            constt = True
            entr.type = type.getchild(0).Typedcl
        else:
            entr.type = type.Typedcl


        idnode = None

        if self.getchild(1).name == '=':
            idnode = self.getchild(1).getchild(0)
            if idnode.Typedcl == 'func':
                raise SemanticsError(idnode.token, "Can not assign to a function declaration")

        else:
            idnode = self.getchild(1)

        if idnode.name in reservedKeys:
            raise SemanticsError(self.token,"Can not use reserved keyword for variable name")

        checkdecl(idnode,entr)

        entryfound = st.LocalTableLookup(entr)
        if(entryfound):
            if (entryfound.func == False):
                raise SemanticsError(self.token,"This variable was already declared in the local scope")
           #elif (entryfound.func == True && entryfound.defined == False && definition == True):
           #    entryfound.defined = True
           #elif (entryfound.func == True && entryfound.defined == True && definition == True):
           #    raise SemanticsError(self.token, "Redefinition of function")
           #else:
           #    raise SemanticsError(self.token, "Redeclaration of function")



        addentry = True;

        if (st.GlobalTableLookup(entr)):
            if (entryfound.func == False):
                #TODO : make general warning function that uses tokens and scope
                Warning(self.token,"Variable is hiding data")
            elif (entryfound.func == True and entryfound.defined == False and definition == True):
                if constt != entryfound.const:
                    raise SemanticsError(self.token, "conflicting types for '" + entryfound.name +"'")
                entryfound.defined = True
                addentry = False
                entr = entryfound
            elif (entryfound.func == True and entryfound.defined == True and definition == True):
                raise SemanticsError(self.token, "Redefinition of function")
            else:
                raise SemanticsError(self.token, "Redeclaration of function")





        if addentry:
            st.addEntry(entr)
            if self.getchild(1).name == '=':  # can only get at this statement if it is a variable (not a func)
                self.getchild(1).handle(st)  # assignment visit
            entr.const = constt
            # if function add params
            if entr.func == True and not definition:
                paramlist = idnode.getchild(0).handle()
                for item in paramlist:
                    entr.params.append(item)
                    print("adding: ", str(item))
            elif entr.func == True and definition:
                print(self.par.getchild(1).__class__.__name__)
                paramlist = self.par.getchild(1).handle()
                for item in paramlist:
                    entr.params.append(item)



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
            ent.type = "array(" + str(child.name) + "," + str(ent.type) + ")"
        return

    elif node.name == "pointer":
        ent.ptr += 1
        checkdecl(node.getchild(0),ent)
        return


    else:
        checkdecl(node.getchild(0),ent)
        return