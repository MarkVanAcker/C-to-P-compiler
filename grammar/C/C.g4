grammar C;

// root of program
program
    : statements?
    ;

// list of all possible statements
statements
    : statement
    | statement statements
    ;

// type of statements (need to add for while if (switch))
statement
    : expression ';'
    | function_definition
    | declaration ';'
    | include_statement
    | conditional_statement
    | iteration_statement
    | return_statement
    | empty_statement
    ;

empty_statement
    : ';'
    ;

return_statement
    : 'return' expression ';'
    | 'return' ';'
    ;

include_statement
    : '#include' include
    ;

function_definition
    : definition compound_statement
;


compound_statement
    : LCURL RCURL
    | LCURL statements RCURL
    ;

definition
    : declaration
    ;

include
    : '<' filename '>'
    | CHARACTER
    ;


conditional_statement
    : IF LPAREN condition RPAREN compound_statement
    | IF LPAREN condition RPAREN  statement
    | IF LPAREN condition RPAREN compound_statement else_statement
    | IF LPAREN condition RPAREN  statement else_statement
    // | switch
    ;

condition
    :expression
    ;

else_statement
    : ELSE compound_statement
    | ELSE statement
    ;

iteration_statement
    : while_statement
    | for_statement
    ;

while_statement
    : WHILE LPAREN condition RPAREN statement
    | WHILE LPAREN condition RPAREN compound_statement
    ;

for_statement
    : FOR LPAREN expression_statement expression_statement RPAREN statement
    | FOR LPAREN expression_statement expression_statement expression RPAREN statement
    | FOR LPAREN expression_statement expression_statement RPAREN compound_statement
    | FOR LPAREN expression_statement expression_statement expression RPAREN compound_statement
    ;

expression_statement
    : expression ';'
    | ';'
    ;


// assignment expression
assignment_expression
    : declarator assignment_operator expression
    ;

primary_expression
	: value
	| pointer value
	| ADDRESS value
	| LPAREN expression RPAREN
	;

postfix_expression
	: primary_expression
	| postfix_expression LSQUARE expression RSQUARE
	| postfix_expression LPAREN RPAREN
	| postfix_expression LPAREN identifier_list RPAREN
	;


expression
    : comparison_expression
    | assignment_expression
    ;

comparison_expression
    : additive_expression
    | comparison_expression comparison_operator additive_expression
    ;


additive_expression
    : multiplicative_expression
    | additive_expression '+' multiplicative_expression
    | additive_expression '-' multiplicative_expression
    ;

multiplicative_expression
    : postfix_expression
    | multiplicative_expression '*' postfix_expression
    | multiplicative_expression '/' postfix_expression
    ;


// different types of declarations making difference between functions and varaibles (void)
declaration
    : declaration_specifier declarator_list  // char var en func (, ...)
    ;

// defines the type of the declaration ( CONST INT x)
declaration_specifier
    : type_specifier
    | type_specifier declaration_specifier
    | type_qualifier
    | type_qualifier declaration_specifier
    ;

declarator_list
    : initialise_declarator
    | declarator_list COMMA initialise_declarator
    ;

initialise_declarator
    : declarator
    | declarator assignment_operator expression
    ;


// seperates pointer variable declaration and no pointer declaration
declarator
    : pointer direct_declarator
    | direct_declarator
    ;


// the declaration of a variable
direct_declarator
    : IDENTIFIER
    | IDENTIFIER LPAREN parameter_list RPAREN
    | IDENTIFIER LPAREN RPAREN
    | direct_declarator LSQUARE expression RSQUARE
    | direct_declarator LSQUARE RSQUARE
    ;


// possible list of values given to a function
identifier_list
    : expression
    | identifier_list COMMA expression
    ;

// possible list of paramaters of a function
parameter_list
    : parameter_declaration
    | parameter_list COMMA parameter_declaration
    ;

// all possible type declarations (supporting void and passing functions as arg)
parameter_declaration
	: declaration_specifier declarator
	| declaration_specifier pointer
	| declaration_specifier
	;



assignment_operator
    : '='
    ;

filename
    : FILENAME
    ;

// integer for indexing
index
    : IDENTIFIER
    | INTEGER
    ;

// anything that refers directly to a value
value
    : IDENTIFIER
    | DECIMAL
    | INTEGER
    | CHARACTER
    ;

// types in c subset
type_specifier
    : CHAR
    | FLOAT
    | INT
    | VOID
    ;

// pointer type ('*')
pointer
    : '*'
    | '*' pointer
    ;



// qualifiers
type_qualifier
    : CONST
    ;

binary_operator
	: '*'
	| '+'
	| '-'
    | '/'
	;

comparison_operator
    : '<'
    | '>'
    | '=='
    ;


// LEXER

WHILE: 'while';
FOR: 'for';
IF: 'if';
ELSE: 'else';
CHAR: 'char';
FLOAT: 'float';
INT: 'int';
ADDRESS: '&';

FILENAME: 'stdio.h';
CONST: 'const';
VOID: 'void';
IDENTIFIER: ('_' | 'a'..'z'| 'A'..'Z')('_' | 'a'..'z'| 'A'..'Z' | '0'..'9')*;
INTEGER: (('1'..'9')('0'..'9')*  | '0');
DECIMAL: (('1'..'9')('0'..'9')*  | '0')('.')('0'..'9')+;
CHARACTER: ('"' .*? '"' | '\'' .*? '\'' );
WS: ('\t' | '\n' | ' ' | '\r')+ -> skip; //toss out whitespace
COMMENT: ('/*' .*? '*/' ) -> skip; // toss out comments
LPAREN : '(';
RPAREN : ')';
LCURL : '{' ;
RCURL : '}' ;
LSQUARE : '[';
RSQUARE : ']';
COMMA : ',';
