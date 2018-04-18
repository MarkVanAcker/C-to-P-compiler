// Generated from C.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link CParser}.
 */
public interface CListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link CParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(CParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link CParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(CParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link CParser#statements}.
	 * @param ctx the parse tree
	 */
	void enterStatements(CParser.StatementsContext ctx);
	/**
	 * Exit a parse tree produced by {@link CParser#statements}.
	 * @param ctx the parse tree
	 */
	void exitStatements(CParser.StatementsContext ctx);
	/**
	 * Enter a parse tree produced by {@link CParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(CParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(CParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(CParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link CParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(CParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link CParser#primary_expression}.
	 * @param ctx the parse tree
	 */
	void enterPrimary_expression(CParser.Primary_expressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CParser#primary_expression}.
	 * @param ctx the parse tree
	 */
	void exitPrimary_expression(CParser.Primary_expressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CParser#postfix_expression}.
	 * @param ctx the parse tree
	 */
	void enterPostfix_expression(CParser.Postfix_expressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CParser#postfix_expression}.
	 * @param ctx the parse tree
	 */
	void exitPostfix_expression(CParser.Postfix_expressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(CParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(CParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CParser#additive_expression}.
	 * @param ctx the parse tree
	 */
	void enterAdditive_expression(CParser.Additive_expressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CParser#additive_expression}.
	 * @param ctx the parse tree
	 */
	void exitAdditive_expression(CParser.Additive_expressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CParser#multiplicative_expression}.
	 * @param ctx the parse tree
	 */
	void enterMultiplicative_expression(CParser.Multiplicative_expressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CParser#multiplicative_expression}.
	 * @param ctx the parse tree
	 */
	void exitMultiplicative_expression(CParser.Multiplicative_expressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CParser#definition}.
	 * @param ctx the parse tree
	 */
	void enterDefinition(CParser.DefinitionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CParser#definition}.
	 * @param ctx the parse tree
	 */
	void exitDefinition(CParser.DefinitionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CParser#declaration}.
	 * @param ctx the parse tree
	 */
	void enterDeclaration(CParser.DeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link CParser#declaration}.
	 * @param ctx the parse tree
	 */
	void exitDeclaration(CParser.DeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link CParser#declaration_specifier}.
	 * @param ctx the parse tree
	 */
	void enterDeclaration_specifier(CParser.Declaration_specifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link CParser#declaration_specifier}.
	 * @param ctx the parse tree
	 */
	void exitDeclaration_specifier(CParser.Declaration_specifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link CParser#function_declaration_specifier}.
	 * @param ctx the parse tree
	 */
	void enterFunction_declaration_specifier(CParser.Function_declaration_specifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link CParser#function_declaration_specifier}.
	 * @param ctx the parse tree
	 */
	void exitFunction_declaration_specifier(CParser.Function_declaration_specifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link CParser#function_declarator}.
	 * @param ctx the parse tree
	 */
	void enterFunction_declarator(CParser.Function_declaratorContext ctx);
	/**
	 * Exit a parse tree produced by {@link CParser#function_declarator}.
	 * @param ctx the parse tree
	 */
	void exitFunction_declarator(CParser.Function_declaratorContext ctx);
	/**
	 * Enter a parse tree produced by {@link CParser#declarator}.
	 * @param ctx the parse tree
	 */
	void enterDeclarator(CParser.DeclaratorContext ctx);
	/**
	 * Exit a parse tree produced by {@link CParser#declarator}.
	 * @param ctx the parse tree
	 */
	void exitDeclarator(CParser.DeclaratorContext ctx);
	/**
	 * Enter a parse tree produced by {@link CParser#function_direct_declarator}.
	 * @param ctx the parse tree
	 */
	void enterFunction_direct_declarator(CParser.Function_direct_declaratorContext ctx);
	/**
	 * Exit a parse tree produced by {@link CParser#function_direct_declarator}.
	 * @param ctx the parse tree
	 */
	void exitFunction_direct_declarator(CParser.Function_direct_declaratorContext ctx);
	/**
	 * Enter a parse tree produced by {@link CParser#direct_declarator}.
	 * @param ctx the parse tree
	 */
	void enterDirect_declarator(CParser.Direct_declaratorContext ctx);
	/**
	 * Exit a parse tree produced by {@link CParser#direct_declarator}.
	 * @param ctx the parse tree
	 */
	void exitDirect_declarator(CParser.Direct_declaratorContext ctx);
	/**
	 * Enter a parse tree produced by {@link CParser#identifier_list}.
	 * @param ctx the parse tree
	 */
	void enterIdentifier_list(CParser.Identifier_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link CParser#identifier_list}.
	 * @param ctx the parse tree
	 */
	void exitIdentifier_list(CParser.Identifier_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link CParser#parameter_list}.
	 * @param ctx the parse tree
	 */
	void enterParameter_list(CParser.Parameter_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link CParser#parameter_list}.
	 * @param ctx the parse tree
	 */
	void exitParameter_list(CParser.Parameter_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link CParser#parameter_declaration}.
	 * @param ctx the parse tree
	 */
	void enterParameter_declaration(CParser.Parameter_declarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link CParser#parameter_declaration}.
	 * @param ctx the parse tree
	 */
	void exitParameter_declaration(CParser.Parameter_declarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link CParser#assignment_operator}.
	 * @param ctx the parse tree
	 */
	void enterAssignment_operator(CParser.Assignment_operatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link CParser#assignment_operator}.
	 * @param ctx the parse tree
	 */
	void exitAssignment_operator(CParser.Assignment_operatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link CParser#index}.
	 * @param ctx the parse tree
	 */
	void enterIndex(CParser.IndexContext ctx);
	/**
	 * Exit a parse tree produced by {@link CParser#index}.
	 * @param ctx the parse tree
	 */
	void exitIndex(CParser.IndexContext ctx);
	/**
	 * Enter a parse tree produced by {@link CParser#value}.
	 * @param ctx the parse tree
	 */
	void enterValue(CParser.ValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link CParser#value}.
	 * @param ctx the parse tree
	 */
	void exitValue(CParser.ValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link CParser#type_specifier}.
	 * @param ctx the parse tree
	 */
	void enterType_specifier(CParser.Type_specifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link CParser#type_specifier}.
	 * @param ctx the parse tree
	 */
	void exitType_specifier(CParser.Type_specifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link CParser#function_type_specifier}.
	 * @param ctx the parse tree
	 */
	void enterFunction_type_specifier(CParser.Function_type_specifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link CParser#function_type_specifier}.
	 * @param ctx the parse tree
	 */
	void exitFunction_type_specifier(CParser.Function_type_specifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link CParser#pointer}.
	 * @param ctx the parse tree
	 */
	void enterPointer(CParser.PointerContext ctx);
	/**
	 * Exit a parse tree produced by {@link CParser#pointer}.
	 * @param ctx the parse tree
	 */
	void exitPointer(CParser.PointerContext ctx);
	/**
	 * Enter a parse tree produced by {@link CParser#type_qualifier}.
	 * @param ctx the parse tree
	 */
	void enterType_qualifier(CParser.Type_qualifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link CParser#type_qualifier}.
	 * @param ctx the parse tree
	 */
	void exitType_qualifier(CParser.Type_qualifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link CParser#binary_operator}.
	 * @param ctx the parse tree
	 */
	void enterBinary_operator(CParser.Binary_operatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link CParser#binary_operator}.
	 * @param ctx the parse tree
	 */
	void exitBinary_operator(CParser.Binary_operatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link CParser#comparison_operator}.
	 * @param ctx the parse tree
	 */
	void enterComparison_operator(CParser.Comparison_operatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link CParser#comparison_operator}.
	 * @param ctx the parse tree
	 */
	void exitComparison_operator(CParser.Comparison_operatorContext ctx);
}