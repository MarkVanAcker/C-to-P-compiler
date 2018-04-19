# Generated from C.g4 by ANTLR 4.6
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CParser import CParser
else:
    from CParser import CParser

# This class defines a complete listener for a parse tree produced by CParser.
class CListener(ParseTreeListener):

    # Enter a parse tree produced by CParser#program.
    def enterProgram(self, ctx:CParser.ProgramContext):
        pass

    # Exit a parse tree produced by CParser#program.
    def exitProgram(self, ctx:CParser.ProgramContext):
        pass


    # Enter a parse tree produced by CParser#statements.
    def enterStatements(self, ctx:CParser.StatementsContext):
        pass

    # Exit a parse tree produced by CParser#statements.
    def exitStatements(self, ctx:CParser.StatementsContext):
        pass


    # Enter a parse tree produced by CParser#statement.
    def enterStatement(self, ctx:CParser.StatementContext):
        pass

    # Exit a parse tree produced by CParser#statement.
    def exitStatement(self, ctx:CParser.StatementContext):
        pass


    # Enter a parse tree produced by CParser#compound_statement.
    def enterCompound_statement(self, ctx:CParser.Compound_statementContext):
        pass

    # Exit a parse tree produced by CParser#compound_statement.
    def exitCompound_statement(self, ctx:CParser.Compound_statementContext):
        pass


    # Enter a parse tree produced by CParser#definition.
    def enterDefinition(self, ctx:CParser.DefinitionContext):
        pass

    # Exit a parse tree produced by CParser#definition.
    def exitDefinition(self, ctx:CParser.DefinitionContext):
        pass


    # Enter a parse tree produced by CParser#include.
    def enterInclude(self, ctx:CParser.IncludeContext):
        pass

    # Exit a parse tree produced by CParser#include.
    def exitInclude(self, ctx:CParser.IncludeContext):
        pass


    # Enter a parse tree produced by CParser#conditional_statement.
    def enterConditional_statement(self, ctx:CParser.Conditional_statementContext):
        pass

    # Exit a parse tree produced by CParser#conditional_statement.
    def exitConditional_statement(self, ctx:CParser.Conditional_statementContext):
        pass


    # Enter a parse tree produced by CParser#condition.
    def enterCondition(self, ctx:CParser.ConditionContext):
        pass

    # Exit a parse tree produced by CParser#condition.
    def exitCondition(self, ctx:CParser.ConditionContext):
        pass


    # Enter a parse tree produced by CParser#else_statement.
    def enterElse_statement(self, ctx:CParser.Else_statementContext):
        pass

    # Exit a parse tree produced by CParser#else_statement.
    def exitElse_statement(self, ctx:CParser.Else_statementContext):
        pass


    # Enter a parse tree produced by CParser#iteration_statement.
    def enterIteration_statement(self, ctx:CParser.Iteration_statementContext):
        pass

    # Exit a parse tree produced by CParser#iteration_statement.
    def exitIteration_statement(self, ctx:CParser.Iteration_statementContext):
        pass


    # Enter a parse tree produced by CParser#while_statement.
    def enterWhile_statement(self, ctx:CParser.While_statementContext):
        pass

    # Exit a parse tree produced by CParser#while_statement.
    def exitWhile_statement(self, ctx:CParser.While_statementContext):
        pass


    # Enter a parse tree produced by CParser#for_statement.
    def enterFor_statement(self, ctx:CParser.For_statementContext):
        pass

    # Exit a parse tree produced by CParser#for_statement.
    def exitFor_statement(self, ctx:CParser.For_statementContext):
        pass


    # Enter a parse tree produced by CParser#expression_statement.
    def enterExpression_statement(self, ctx:CParser.Expression_statementContext):
        pass

    # Exit a parse tree produced by CParser#expression_statement.
    def exitExpression_statement(self, ctx:CParser.Expression_statementContext):
        pass


    # Enter a parse tree produced by CParser#assignment_expression.
    def enterAssignment_expression(self, ctx:CParser.Assignment_expressionContext):
        pass

    # Exit a parse tree produced by CParser#assignment_expression.
    def exitAssignment_expression(self, ctx:CParser.Assignment_expressionContext):
        pass


    # Enter a parse tree produced by CParser#primary_expression.
    def enterPrimary_expression(self, ctx:CParser.Primary_expressionContext):
        pass

    # Exit a parse tree produced by CParser#primary_expression.
    def exitPrimary_expression(self, ctx:CParser.Primary_expressionContext):
        pass


    # Enter a parse tree produced by CParser#postfix_expression.
    def enterPostfix_expression(self, ctx:CParser.Postfix_expressionContext):
        pass

    # Exit a parse tree produced by CParser#postfix_expression.
    def exitPostfix_expression(self, ctx:CParser.Postfix_expressionContext):
        pass


    # Enter a parse tree produced by CParser#expression.
    def enterExpression(self, ctx:CParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CParser#expression.
    def exitExpression(self, ctx:CParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CParser#comparison_expression.
    def enterComparison_expression(self, ctx:CParser.Comparison_expressionContext):
        pass

    # Exit a parse tree produced by CParser#comparison_expression.
    def exitComparison_expression(self, ctx:CParser.Comparison_expressionContext):
        pass


    # Enter a parse tree produced by CParser#additive_expression.
    def enterAdditive_expression(self, ctx:CParser.Additive_expressionContext):
        pass

    # Exit a parse tree produced by CParser#additive_expression.
    def exitAdditive_expression(self, ctx:CParser.Additive_expressionContext):
        pass


    # Enter a parse tree produced by CParser#multiplicative_expression.
    def enterMultiplicative_expression(self, ctx:CParser.Multiplicative_expressionContext):
        pass

    # Exit a parse tree produced by CParser#multiplicative_expression.
    def exitMultiplicative_expression(self, ctx:CParser.Multiplicative_expressionContext):
        pass


    # Enter a parse tree produced by CParser#declaration.
    def enterDeclaration(self, ctx:CParser.DeclarationContext):
        pass

    # Exit a parse tree produced by CParser#declaration.
    def exitDeclaration(self, ctx:CParser.DeclarationContext):
        pass


    # Enter a parse tree produced by CParser#declaration_specifier.
    def enterDeclaration_specifier(self, ctx:CParser.Declaration_specifierContext):
        pass

    # Exit a parse tree produced by CParser#declaration_specifier.
    def exitDeclaration_specifier(self, ctx:CParser.Declaration_specifierContext):
        pass


    # Enter a parse tree produced by CParser#declarator_list.
    def enterDeclarator_list(self, ctx:CParser.Declarator_listContext):
        pass

    # Exit a parse tree produced by CParser#declarator_list.
    def exitDeclarator_list(self, ctx:CParser.Declarator_listContext):
        pass


    # Enter a parse tree produced by CParser#initialise_declarator.
    def enterInitialise_declarator(self, ctx:CParser.Initialise_declaratorContext):
        pass

    # Exit a parse tree produced by CParser#initialise_declarator.
    def exitInitialise_declarator(self, ctx:CParser.Initialise_declaratorContext):
        pass


    # Enter a parse tree produced by CParser#declarator.
    def enterDeclarator(self, ctx:CParser.DeclaratorContext):
        pass

    # Exit a parse tree produced by CParser#declarator.
    def exitDeclarator(self, ctx:CParser.DeclaratorContext):
        pass


    # Enter a parse tree produced by CParser#direct_declarator.
    def enterDirect_declarator(self, ctx:CParser.Direct_declaratorContext):
        pass

    # Exit a parse tree produced by CParser#direct_declarator.
    def exitDirect_declarator(self, ctx:CParser.Direct_declaratorContext):
        pass


    # Enter a parse tree produced by CParser#identifier_list.
    def enterIdentifier_list(self, ctx:CParser.Identifier_listContext):
        pass

    # Exit a parse tree produced by CParser#identifier_list.
    def exitIdentifier_list(self, ctx:CParser.Identifier_listContext):
        pass


    # Enter a parse tree produced by CParser#parameter_list.
    def enterParameter_list(self, ctx:CParser.Parameter_listContext):
        pass

    # Exit a parse tree produced by CParser#parameter_list.
    def exitParameter_list(self, ctx:CParser.Parameter_listContext):
        pass


    # Enter a parse tree produced by CParser#parameter_declaration.
    def enterParameter_declaration(self, ctx:CParser.Parameter_declarationContext):
        pass

    # Exit a parse tree produced by CParser#parameter_declaration.
    def exitParameter_declaration(self, ctx:CParser.Parameter_declarationContext):
        pass


    # Enter a parse tree produced by CParser#assignment_operator.
    def enterAssignment_operator(self, ctx:CParser.Assignment_operatorContext):
        pass

    # Exit a parse tree produced by CParser#assignment_operator.
    def exitAssignment_operator(self, ctx:CParser.Assignment_operatorContext):
        pass


    # Enter a parse tree produced by CParser#filename.
    def enterFilename(self, ctx:CParser.FilenameContext):
        pass

    # Exit a parse tree produced by CParser#filename.
    def exitFilename(self, ctx:CParser.FilenameContext):
        pass


    # Enter a parse tree produced by CParser#index.
    def enterIndex(self, ctx:CParser.IndexContext):
        pass

    # Exit a parse tree produced by CParser#index.
    def exitIndex(self, ctx:CParser.IndexContext):
        pass


    # Enter a parse tree produced by CParser#value.
    def enterValue(self, ctx:CParser.ValueContext):
        pass

    # Exit a parse tree produced by CParser#value.
    def exitValue(self, ctx:CParser.ValueContext):
        pass


    # Enter a parse tree produced by CParser#type_specifier.
    def enterType_specifier(self, ctx:CParser.Type_specifierContext):
        pass

    # Exit a parse tree produced by CParser#type_specifier.
    def exitType_specifier(self, ctx:CParser.Type_specifierContext):
        pass


    # Enter a parse tree produced by CParser#pointer.
    def enterPointer(self, ctx:CParser.PointerContext):
        pass

    # Exit a parse tree produced by CParser#pointer.
    def exitPointer(self, ctx:CParser.PointerContext):
        pass


    # Enter a parse tree produced by CParser#type_qualifier.
    def enterType_qualifier(self, ctx:CParser.Type_qualifierContext):
        pass

    # Exit a parse tree produced by CParser#type_qualifier.
    def exitType_qualifier(self, ctx:CParser.Type_qualifierContext):
        pass


    # Enter a parse tree produced by CParser#binary_operator.
    def enterBinary_operator(self, ctx:CParser.Binary_operatorContext):
        pass

    # Exit a parse tree produced by CParser#binary_operator.
    def exitBinary_operator(self, ctx:CParser.Binary_operatorContext):
        pass


    # Enter a parse tree produced by CParser#comparison_operator.
    def enterComparison_operator(self, ctx:CParser.Comparison_operatorContext):
        pass

    # Exit a parse tree produced by CParser#comparison_operator.
    def exitComparison_operator(self, ctx:CParser.Comparison_operatorContext):
        pass


