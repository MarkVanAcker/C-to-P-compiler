// Generated from C.g4 by ANTLR 4.6
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link CParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface CVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link CParser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(CParser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by {@link CParser#statements}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatements(CParser.StatementsContext ctx);
	/**
	 * Visit a parse tree produced by {@link CParser#statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatement(CParser.StatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link CParser#compound_statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCompound_statement(CParser.Compound_statementContext ctx);
	/**
	 * Visit a parse tree produced by {@link CParser#definition}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDefinition(CParser.DefinitionContext ctx);
	/**
	 * Visit a parse tree produced by {@link CParser#include}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInclude(CParser.IncludeContext ctx);
	/**
	 * Visit a parse tree produced by {@link CParser#conditional_statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitConditional_statement(CParser.Conditional_statementContext ctx);
	/**
	 * Visit a parse tree produced by {@link CParser#condition}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCondition(CParser.ConditionContext ctx);
	/**
	 * Visit a parse tree produced by {@link CParser#else_statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitElse_statement(CParser.Else_statementContext ctx);
	/**
	 * Visit a parse tree produced by {@link CParser#iteration_statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIteration_statement(CParser.Iteration_statementContext ctx);
	/**
	 * Visit a parse tree produced by {@link CParser#while_statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWhile_statement(CParser.While_statementContext ctx);
	/**
	 * Visit a parse tree produced by {@link CParser#for_statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFor_statement(CParser.For_statementContext ctx);
	/**
	 * Visit a parse tree produced by {@link CParser#expression_statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression_statement(CParser.Expression_statementContext ctx);
	/**
	 * Visit a parse tree produced by {@link CParser#assignment_expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAssignment_expression(CParser.Assignment_expressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link CParser#primary_expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrimary_expression(CParser.Primary_expressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link CParser#postfix_expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPostfix_expression(CParser.Postfix_expressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link CParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression(CParser.ExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link CParser#comparison_expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitComparison_expression(CParser.Comparison_expressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link CParser#additive_expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAdditive_expression(CParser.Additive_expressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link CParser#multiplicative_expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMultiplicative_expression(CParser.Multiplicative_expressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link CParser#declaration}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDeclaration(CParser.DeclarationContext ctx);
	/**
	 * Visit a parse tree produced by {@link CParser#declaration_specifier}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDeclaration_specifier(CParser.Declaration_specifierContext ctx);
	/**
	 * Visit a parse tree produced by {@link CParser#declarator_list}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDeclarator_list(CParser.Declarator_listContext ctx);
	/**
	 * Visit a parse tree produced by {@link CParser#initialise_declarator}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInitialise_declarator(CParser.Initialise_declaratorContext ctx);
	/**
	 * Visit a parse tree produced by {@link CParser#declarator}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDeclarator(CParser.DeclaratorContext ctx);
	/**
	 * Visit a parse tree produced by {@link CParser#direct_declarator}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDirect_declarator(CParser.Direct_declaratorContext ctx);
	/**
	 * Visit a parse tree produced by {@link CParser#identifier_list}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIdentifier_list(CParser.Identifier_listContext ctx);
	/**
	 * Visit a parse tree produced by {@link CParser#parameter_list}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParameter_list(CParser.Parameter_listContext ctx);
	/**
	 * Visit a parse tree produced by {@link CParser#parameter_declaration}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParameter_declaration(CParser.Parameter_declarationContext ctx);
	/**
	 * Visit a parse tree produced by {@link CParser#assignment_operator}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAssignment_operator(CParser.Assignment_operatorContext ctx);
	/**
	 * Visit a parse tree produced by {@link CParser#filename}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFilename(CParser.FilenameContext ctx);
	/**
	 * Visit a parse tree produced by {@link CParser#index}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIndex(CParser.IndexContext ctx);
	/**
	 * Visit a parse tree produced by {@link CParser#value}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitValue(CParser.ValueContext ctx);
	/**
	 * Visit a parse tree produced by {@link CParser#type_specifier}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitType_specifier(CParser.Type_specifierContext ctx);
	/**
	 * Visit a parse tree produced by {@link CParser#pointer}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPointer(CParser.PointerContext ctx);
	/**
	 * Visit a parse tree produced by {@link CParser#type_qualifier}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitType_qualifier(CParser.Type_qualifierContext ctx);
	/**
	 * Visit a parse tree produced by {@link CParser#binary_operator}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBinary_operator(CParser.Binary_operatorContext ctx);
	/**
	 * Visit a parse tree produced by {@link CParser#comparison_operator}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitComparison_operator(CParser.Comparison_operatorContext ctx);
}