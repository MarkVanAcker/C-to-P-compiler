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


    # Enter a parse tree produced by CParser#assignment.
    def enterAssignment(self, ctx:CParser.AssignmentContext):
        pass

    # Exit a parse tree produced by CParser#assignment.
    def exitAssignment(self, ctx:CParser.AssignmentContext):
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


    # Enter a parse tree produced by CParser#definition.
    def enterDefinition(self, ctx:CParser.DefinitionContext):
        pass

    # Exit a parse tree produced by CParser#definition.
    def exitDefinition(self, ctx:CParser.DefinitionContext):
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


    # Enter a parse tree produced by CParser#function_declaration_specifier.
    def enterFunction_declaration_specifier(self, ctx:CParser.Function_declaration_specifierContext):
        pass

    # Exit a parse tree produced by CParser#function_declaration_specifier.
    def exitFunction_declaration_specifier(self, ctx:CParser.Function_declaration_specifierContext):
        pass


    # Enter a parse tree produced by CParser#function_declarator.
    def enterFunction_declarator(self, ctx:CParser.Function_declaratorContext):
        pass

    # Exit a parse tree produced by CParser#function_declarator.
    def exitFunction_declarator(self, ctx:CParser.Function_declaratorContext):
        pass


    # Enter a parse tree produced by CParser#declarator.
    def enterDeclarator(self, ctx:CParser.DeclaratorContext):
        pass

    # Exit a parse tree produced by CParser#declarator.
    def exitDeclarator(self, ctx:CParser.DeclaratorContext):
        pass


    # Enter a parse tree produced by CParser#function_direct_declarator.
    def enterFunction_direct_declarator(self, ctx:CParser.Function_direct_declaratorContext):
        pass

    # Exit a parse tree produced by CParser#function_direct_declarator.
    def exitFunction_direct_declarator(self, ctx:CParser.Function_direct_declaratorContext):
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


    # Enter a parse tree produced by CParser#function_type_specifier.
    def enterFunction_type_specifier(self, ctx:CParser.Function_type_specifierContext):
        pass

    # Exit a parse tree produced by CParser#function_type_specifier.
    def exitFunction_type_specifier(self, ctx:CParser.Function_type_specifierContext):
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


