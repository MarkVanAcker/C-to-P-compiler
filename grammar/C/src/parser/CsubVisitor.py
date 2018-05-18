from build.CVisitor import CVisitor
from build.CParser import CParser
from src.astclasses import *

class CsubVisitor(CVisitor):


    def __init__(self,name="Program"):
        self.DOT = False
        self.AST = ASTNode(name)


    def todot(self,node,child):


        if(child.getChildCount() == 0):
            self.file.write("\tNODE" + str(id(child)) + "[label=\"" + child.getText()+ "\"];\n")
        else:
            self.file.write("\tNODE" + str(id(child)) + "[label=\"" + CParser.ruleNames[child.getRuleIndex()]+ "\"];\n")
        self.file.write("\tNODE"+str(id(node))+"->NODE"+str(id(child))+"\n")





    def todot_visit(self, tree):


        self.DOT = True
        self.file = open("CST.dot", "w")

        self.file.write('''digraph G
        {
            nodesep = 0.4;
            ranksep = 0.5;
        ''')

        self.file.write("\tNODE" + str(id(tree)) + "[label=\"" + CParser.ruleNames[tree.getRuleIndex()] + "\"];\n")

        tree.accept(self)

        self.file.write('}')

        self.file.close()

    def myDeepCopy(self,n):

        node = ASTNode(n.name,n.token)
        node.Typedcl = n.Typedcl
        if n.hasChild():
            for m in n.children:
                node.addchild(self.myDeepCopy(m))

        return node




    def aggregateResult(self, aggregate, nextResult):
        if nextResult is None or aggregate is None:
            return None
        else:
            return nextResult


    def visitTerminal(self, node):
        return self.tokenHandler(node.getText(),node.getSymbol())



    def defaultResult(self):
        return ""




    # Visit a parse tree produced by CParser#program.
    def visitProgram(self, ctx:CParser.ProgramContext):

        if ctx.getChildCount() == 0:
            self.AST.addchildren([ASTNode("empty")])
            return self.AST
        c = ctx.getChild(0).accept(self)
        self.AST.addchildren(c)
        return self.AST

    # Visit a parse tree produced by CParser#statements.
    def visitStatements(self, ctx:CParser.StatementsContext):
        childlist = []
        n = ctx.getChildCount()
        for i in range(n):
            c = ctx.getChild(i)
            childResult = c.accept(self)
            try:
                childlist.extend(childResult)
            except TypeError:
                childlist.append(childResult)

        return childlist


    # Visit a parse tree produced by CParser#statement.
    def visitStatement(self, ctx:CParser.StatementContext):
        c = ctx.getChild(0)
        childResult = c.accept(self)
        return childResult


    # Visit a parse tree produced by CParser#empty_statement.
    def visitEmpty_statement(self, ctx:CParser.Empty_statementContext):
        return ASTNode("empty statement")


    # Visit a parse tree produced by CParser#return_statement.
    def visitReturn_statement(self, ctx:CParser.Return_statementContext):
        node = ReturnNode("return")
        if ctx.getChildCount() == 2:
            return node
        node.addchild(ctx.getChild(1).accept(self))
        return node



    # Visit a parse tree produced by CParser#include_statement.
    def visitInclude_statement(self, ctx:CParser.Include_statementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#function_definition.
    def visitFunction_definition(self, ctx:CParser.Function_definitionContext):

        decl = ctx.getChild(0).accept(self) # TYPE + FUNCTION NAME AND PARAMETERS
        # MAKE SURE TYPE IS FUNCTION

        if (len(decl) > 1):
            self.errorHandler("expected ‘,’, ‘;' before ‘{’ token", decl[1])

        node = FunctionDefinitionNode("function definition")
        initnode = decl[0]

        node.addchild(initnode) # type

        if initnode.getchild(1).hasChild():
            paramnode = initnode.getchild(1).getchild(0)
            initnode.getchild(1).clearchildren()
            node.addchild(paramnode)

        else:
            nodepara = ASTNode("paramlist")
            nodeempty = ASTNode("empty")
            nodepara.addchild(nodeempty)
            node.addchild(nodepara)

        comp_state = ctx.getChild(1).accept(self)

        node.addchild(comp_state) # block

        return node


    # Visit a parse tree produced by CParser#compound_statement.
    def visitCompound_statement(self, ctx:CParser.Compound_statementContext):
        node = ASTNode("block")
        if ctx.getChildCount() == 2: # emtpy 2 curly brackets only
            return node

        statements = ctx.getChild(1).accept(self)
        for i in statements:
            node.addchild(i)


        return node


    # Visit a parse tree produced by CParser#definition.
    def visitDefinition(self, ctx:CParser.DefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#include.
    def visitInclude(self, ctx:CParser.IncludeContext):

        node1 = ASTNode("include") # making it ez because it is ... (in our case)
        node2 = ASTNode("stdio.h")
        node1.addchild(node2)


        return [node1]


    # Visit a parse tree produced by CParser#conditional_statement.
    def visitConditional_statement(self, ctx:CParser.Conditional_statementContext):
        node = ConditionNode("if")
        node2 = ASTNode("condition")
        condition_st = ctx.getChild(2).accept(self)
        node2.addchild(condition_st)
        node.addchild(node2)
        state = ctx.getChild(4)
        if isinstance(state, CParser.Compound_statementContext):
            node.addchild(state.accept(self)) # returns a block

        if isinstance(state, CParser.StatementContext):
            nodeblock = ASTNode("block") # make block
            templist = []
            templist.append(state.accept(self))  # state could be node or list of nodes
            for i in templist:
                nodeblock.addchild(i)
            node.addchild(nodeblock)
        if ctx.getChildCount() == 6: # else alternative
            node.addchild(ctx.getChild(5).accept(self)) # else block

        return node


    # Visit a parse tree produced by CParser#condition.
    def visitCondition(self, ctx:CParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#else_statement.
    def visitElse_statement(self, ctx:CParser.Else_statementContext):

        state = ctx.getChild(1)

        if isinstance(state, CParser.Compound_statementContext):
            state = state.accept(self)
            return state # returns a block

        if isinstance(state, CParser.StatementContext):
            nodeblock = ASTNode("block") # make block
            templist = []
            templist.append(state.accept(self))  # state could be node or list of nodes
            for i in templist:
                nodeblock.addchild(i)
            #node.addchild(nodeblock)

            return nodeblock


    # Visit a parse tree produced by CParser#iteration_statement.
    def visitIteration_statement(self, ctx:CParser.Iteration_statementContext):
        return ctx.getChild(0).accept(self)


    # Visit a parse tree produced by CParser#while_statement.
    def visitWhile_statement(self, ctx:CParser.While_statementContext):

        node = WhileNode("while")
        node2 = ASTNode("condition")
        condition_st = ctx.getChild(2).accept(self)
        node2.addchild(condition_st)
        node.addchild(node2)
        state = ctx.getChild(4)
        if isinstance(state, CParser.Compound_statementContext):
            node.addchild(state.accept(self)) # returns a block

        if isinstance(state, CParser.StatementContext):
            nodeblock = ASTNode("block") # make block
            templist = []
            templist.extend(state.accept(self))  # state could be node or list of nodes
            for i in templist:
                nodeblock.addchild(i)
            node.addchild(nodeblock)

        return [node]




    # Visit a parse tree produced by CParser#for_statement.

    #TODO : refactor thise with while

    def visitFor_statement(self, ctx:CParser.For_statementContext):

        returnlist = []
        prenode = ctx.getChild(2).accept(self)

        if (prenode.name != "empty"):
            returnlist.append(prenode)


        node = ASTNode("while")
        node2 = ASTNode("condition")
        condition_st = ctx.getChild(3).accept(self)
        node2.addchild(condition_st)
        node.addchild(node2)
        state = "def"
        if ctx.getChildCount() == 6:
            state = ctx.getChild(5)
        if ctx.getChildCount() == 7:
            state = ctx.getChild(6)

        if isinstance(state, CParser.Compound_statementContext):
            nodeblock = state.accept(self)
            if ctx.getChildCount() == 7:
                nodeafter = ctx.getChild(4).accept(self)
                nodeblock.addchild(nodeafter)
            node.addchild(nodeblock) # returns a block


        if isinstance(state, CParser.StatementContext):
            nodeblock = ASTNode("block") # make block
            templist = []
            templist.extend(state.accept(self))  # state could be node or list of nodes
            for i in templist:
                nodeblock.addchild(i)
            if ctx.getChildCount() == 7:
                nodeafter = ctx.getChild(4).accept(self)
                nodeblock.addchild(nodeafter)
            node.addchild(nodeblock)

        returnlist.append(node)


        return returnlist





    # Visit a parse tree produced by CParser#expression_statement.
    def visitExpression_statement(self, ctx:CParser.Expression_statementContext):
        if ctx.getChildCount() == 2:
            return ctx.getChild(0).accept(self)
        if ctx.getChildCount() == 1:
            return ASTNode("empty")




    # Visit a parse tree produced by CParser#assignment_expression.
    def visitAssignment_expression(self, ctx:CParser.Assignment_expressionContext):
        return self.exprHandler(ctx)


    # Visit a parse tree produced by CParser#primary_expression.
    def visitPrimary_expression(self, ctx:CParser.Primary_expressionContext):

        if (ctx.getChildCount() == 1):
            return self.visitChildren(ctx)

        else:
            return ctx.getChild(1).accept(self)


    # Visit a parse tree produced by CParser#postfix_expression.
    def visitPostfix_expression(self, ctx:CParser.Postfix_expressionContext):

        if (ctx.getChildCount() == 1):
            return self.visitChildren(ctx)

        node = ctx.getChild(1).accept(self)
        if (node.token.type == CParser.LPAREN):

            tempnode = ASTNode("funccall")
            paramnode = ASTNode("paramlist")
            if(ctx.getChildCount() == 3):
                tempnode.addchild(ctx.getChild(0).accept(self))
                tempnode.addchild(paramnode)
                paramnode.addchild(ASTNode("empty")) #TODO: maybe remove

            else:
                tempnode.addchild(ctx.getChild(0).accept(self))
                tempnode.addchild(paramnode)
                paramnode.addchildren(ctx.getChild(2).accept(self))

            return tempnode




        elif(node.token.type == CParser.LSQUARE):
            tempnode = ASTNode("access")
            tempnode.addchild(ctx.getChild(0).accept(self))
            tempnode.addchild(ctx.getChild(2).accept(self))

            return tempnode



    # Visit a parse tree produced by CParser#expression.
    def visitExpression(self, ctx:CParser.ExpressionContext):
        return self.exprHandler(ctx)


    # Visit a parse tree produced by CParser#comparison_expression.
    def visitComparison_expression(self, ctx:CParser.Comparison_expressionContext):
        return self.exprHandler(ctx)


    # Visit a parse tree produced by CParser#additive_expression.
    def visitAdditive_expression(self, ctx:CParser.Additive_expressionContext):
        return self.exprHandler(ctx)


    # Visit a parse tree produced by CParser#multiplicative_expression.
    def visitMultiplicative_expression(self, ctx:CParser.Multiplicative_expressionContext):
        return self.exprHandler(ctx)


    # Visit a parse tree produced by CParser#declaration.
    def visitDeclaration(self, ctx:CParser.DeclarationContext):



        n = ctx.getChild(0).accept(self)


        typenode = self.TypeCheck(n)

        decllist = ctx.getChild(1).accept(self)

        resultlist = []
        for i in decllist:
            node = DeclarationNode("declaration")


            node.addchild(self.myDeepCopy(typenode))
            node.addchild(i)
            resultlist.append(node)

        return resultlist






    # Visit a parse tree produced by CParser#declaration_specifier.
    def visitDeclaration_specifier(self, ctx:CParser.Declaration_specifierContext):



        if ctx.getChildCount() == 1:
            return [ctx.getChild(0).accept(self)]

        nodelist = [ctx.getChild(0).accept(self)]
        nodelist.extend(ctx.getChild(1).accept(self))

        return nodelist



    # Visit a parse tree produced by CParser#declarator_list.
    def visitDeclarator_list(self, ctx:CParser.Declarator_listContext):

        if ctx.getChildCount() == 1:
            return [ctx.getChild(0).accept(self)]

        else:
            n = ctx.getChild(0).accept(self)
            n.append(ctx.getChild(2).accept(self))

            return n


    # Visit a parse tree produced by CParser#initialise_declarator.
    def visitInitialise_declarator(self, ctx:CParser.Initialise_declaratorContext):
        return self.exprHandler(ctx)


    # Visit a parse tree produced by CParser#declarator.
    def visitDeclarator(self, ctx:CParser.DeclaratorContext):
        n = ctx.getChild(0)

        if isinstance(n, CParser.PointerContext):
            r = ASTNode("pointer")
            r.addchild(ctx.getChild(1).accept(self))
            return r
        else:
            return n.accept(self)

    # Visit a parse tree produced by CParser#direct_declarator.
    def visitDirect_declarator(self, ctx:CParser.Direct_declaratorContext):


        childlist = []
        n = ctx.getChildCount()

        if(n == 1):
            return self.visitChildren(ctx)


        #refactor
        node = ctx.getChild(1).accept(self)
        if( n == 3):
            if (node.token.type == CParser.LPAREN):
                tempnode = ctx.getChild(0).accept(self)
                tempnode.Typedcl = "func"
                return tempnode
            elif (node.token.type == CParser.LSQUARE):
                tempnode = ctx.getChild(0).accept(self)
                tempnode.Typedcl = "array"
                return tempnode

        if (n == 4):
            if (node.token.type == CParser.LPAREN):
                tempnode = ctx.getChild(0).accept(self)
                tempnode.Typedcl = "func"



                paramnode = ASTNode("paramlist")

                paramdecs = ctx.getChild(2).accept(self)

                paramnode.addchildren(paramdecs)


                tempnode.addchild(paramnode)

                return tempnode
            elif (node.token.type == CParser.LSQUARE):
                tempnode = ctx.getChild(0).accept(self)
                tempnode.Typedcl = "array"

                paramnode = ctx.getChild(2).accept(self)

                tempnode.addchild(paramnode)

                return tempnode



        for i in range(n):
            c = ctx.getChild(i)
            childResult = c.accept(self)
            if isinstance(c, CParser.StatementsContext):
                childlist.extend(childResult)
            else:
                childlist.append(childResult)

        return childlist

        #n = self.visitChildren(ctx)
        #if n.token.type == CParser.IDENTIFIER:
        #    n.Typedcl = "id"
        #elif n.token.type == CParser.INTEGER:
        #    n.Typedcl = "intconst"
        #elif n.token.type == CParser.DECIMAL:
        #    n.Typedcl = "floatconst"
        #return n

    # Visit a parse tree produced by CParser#identifier_list.
    def visitIdentifier_list(self, ctx:CParser.Identifier_listContext):

        if(ctx.getChildCount() == 1):
            return [ctx.getChild(0).accept(self)]


        else:
            templist = ctx.getChild(0).accept(self)

            templist.append(ctx.getChild(2).accept(self))

            return templist




    # Visit a parse tree produced by CParser#parameter_list.
    def visitParameter_list(self, ctx:CParser.Parameter_listContext):

        if(ctx.getChildCount() == 1):
            return [ctx.getChild(0).accept(self)]


        else:
            templist = ctx.getChild(0).accept(self)

            templist.append(ctx.getChild(2).accept(self))

            return templist


    # Visit a parse tree produced by CParser#parameter_declaration.
    def visitParameter_declaration(self, ctx:CParser.Parameter_declarationContext):


        if(ctx.getChildCount() == 1):
            typenode = self.TypeCheck(ctx.getChild(0).accept(self))
            return typenode

        else:
            tempnode = DeclarationNode("paramdecl")
            typenode = self.TypeCheck(ctx.getChild(0).accept(self))
            tempnode.addchild(typenode)
            tempnode.addchild(ctx.getChild(1).accept(self))
            return tempnode


    # Visit a parse tree produced by CParser#assignment_operator.
    def visitAssignment_operator(self, ctx:CParser.Assignment_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#filename.
    def visitFilename(self, ctx:CParser.FilenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#index.
    #def visitIndex(self, ctx:CParser.IndexContext):
        #return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#value.
    def visitValue(self, ctx:CParser.ValueContext):
        n = self.visitChildren(ctx)
        return n


    # Visit a parse tree produced by CParser#type_specifier.
    def visitType_specifier(self, ctx:CParser.Type_specifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#pointer.
    def visitPointer(self, ctx:CParser.PointerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#type_qualifier.
    def visitType_qualifier(self, ctx:CParser.Type_qualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#binary_operator.
    def visitBinary_operator(self, ctx:CParser.Binary_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#comparison_operator.
    def visitComparison_operator(self, ctx:CParser.Comparison_operatorContext):
        return self.visitChildren(ctx)







    #General function


    def exprHandler(self,ctx):
        if ctx.getChildCount() == 1:
            return ctx.getChild(0).accept(self)

        else:
            name = ctx.getChild(1).accept(self).name
            if ctx.getChild(1).accept(self).name == '<':
                name = 'lt'
            if ctx.getChild(1).accept(self).name == '>':
                name = 'gt'
            exprnode = ExpressionNode(name)
            if(name == "="):
                exprnode = AssignmentNode(name)
            exprnode.addchild(ctx.getChild(0).accept(self))
            exprnode.addchild(ctx.getChild(2).accept(self))
            return exprnode




    def tokenHandler(self,name,token):
        if token.type == CParser.IDENTIFIER:
            n = IDNode(name,token)
            n.Typedcl = "id"
        else:
            n = ConstantNode(name, token)
            if token.type == CParser.INTEGER:
                n.Typedcl = IntegerType()
            elif token.type == CParser.DECIMAL:
                n.Typedcl = RealType()
            elif token.type == CParser.CHARACTER:
                n.Typedcl = CharacterType()
        return n


    def warningprint(self,w,i):
        print("Warning: ",w)


    def errorHandler(self,e,i):
        raise Exception(e)


    #add tokeninfo
    def TypeCheck(self,n):
        quant = None
        constbool = False
        type = None

        for i in n:
            if(i.token.type == CParser.CONST):
                if constbool:
                    self.warningprint("duplicate ‘const’",i)
                    continue

                else:
                    constbool = True
                    quant = i
                    continue

            if type is None:
                type = i
            else:
                self.errorHandler("two or more data types in declaration specifiers",i)

        if type is None:
            self.errorHandler("no data type was given", n[0])

        if quant is None:
            return type
        else:

            quant.addchild(type)
            return quant
