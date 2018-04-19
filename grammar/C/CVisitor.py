# Generated from C.g4 by ANTLR 4.6
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CParser import CParser
else:
    from CParser import CParser

# This class defines a complete generic visitor for a parse tree produced by CParser.

class CVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CParser#program.
    def visitProgram(self, ctx:CParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#statements.
    def visitStatements(self, ctx:CParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#statement.
    def visitStatement(self, ctx:CParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#compound_statement.
    def visitCompound_statement(self, ctx:CParser.Compound_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#definition.
    def visitDefinition(self, ctx:CParser.DefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#include.
    def visitInclude(self, ctx:CParser.IncludeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#conditional_statement.
    def visitConditional_statement(self, ctx:CParser.Conditional_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#condition.
    def visitCondition(self, ctx:CParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#else_statement.
    def visitElse_statement(self, ctx:CParser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#iteration_statement.
    def visitIteration_statement(self, ctx:CParser.Iteration_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#while_statement.
    def visitWhile_statement(self, ctx:CParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#for_statement.
    def visitFor_statement(self, ctx:CParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#expression_statement.
    def visitExpression_statement(self, ctx:CParser.Expression_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#assignment_expression.
    def visitAssignment_expression(self, ctx:CParser.Assignment_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#primary_expression.
    def visitPrimary_expression(self, ctx:CParser.Primary_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#postfix_expression.
    def visitPostfix_expression(self, ctx:CParser.Postfix_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#expression.
    def visitExpression(self, ctx:CParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#comparison_expression.
    def visitComparison_expression(self, ctx:CParser.Comparison_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#additive_expression.
    def visitAdditive_expression(self, ctx:CParser.Additive_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#multiplicative_expression.
    def visitMultiplicative_expression(self, ctx:CParser.Multiplicative_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#declaration.
    def visitDeclaration(self, ctx:CParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#declaration_specifier.
    def visitDeclaration_specifier(self, ctx:CParser.Declaration_specifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#declarator_list.
    def visitDeclarator_list(self, ctx:CParser.Declarator_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#initialise_declarator.
    def visitInitialise_declarator(self, ctx:CParser.Initialise_declaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#declarator.
    def visitDeclarator(self, ctx:CParser.DeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#direct_declarator.
    def visitDirect_declarator(self, ctx:CParser.Direct_declaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#identifier_list.
    def visitIdentifier_list(self, ctx:CParser.Identifier_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#parameter_list.
    def visitParameter_list(self, ctx:CParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#parameter_declaration.
    def visitParameter_declaration(self, ctx:CParser.Parameter_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#assignment_operator.
    def visitAssignment_operator(self, ctx:CParser.Assignment_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#filename.
    def visitFilename(self, ctx:CParser.FilenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#index.
    def visitIndex(self, ctx:CParser.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#value.
    def visitValue(self, ctx:CParser.ValueContext):
        return self.visitChildren(ctx)


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



del CParser