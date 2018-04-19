grammar C;

// root of program
program
    : statements
    ;

// list of all possible statements
statements
    : statement
    | statement statements
    ;

// type of statements (need to add for while if (switch))
statement
    : expression ';'
    | definition compound_statement
    | declaration ';'
    |  '#include' include
    | conditional_statement
    | iteration_statement
    | 'return' expression ';'
    | ';'
    ;

compound_statement
    : '{' '}'
    | '{' statements '}'
    ;

definition
    : declaration
    ;

include
    : '\'' filename '\''
    | '<' filename '>'
    ;


conditional_statement
    : IF '(' condition ')' compound_statement
    | IF '(' condition ')'  statement
    | IF '(' condition ')' compound_statement else_statement
    | IF '(' condition ')'  statement else_statement
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
    : WHILE '(' expression ')' statement
    | WHILE '(' expression ')' compound_statement
    ;

for_statement
    : FOR '(' expression_statement expression_statement ')' statement
    | FOR '(' expression_statement expression_statement expression ')' statement
    | FOR '(' expression_statement expression_statement ')' compound_statement
    | FOR '(' expression_statement expression_statement expression ')' compound_statement
    ;

expression_statement
    : expression ';'
    | ';'
    ;

//declaration_list
//    : declaration
//    | declaration ',' declarator_list
//    ;

//declarator_list
//    : declarator
//    | function_declarator
//    | declarator_list ',' declarator
//    | declarator_list ',' function_declarator
//    ;

// assignment expression
assignment_expression
    : declaration assignment_operator expression
    | declarator assignment_operator expression
    ;

primary_expression
	: value
	| '(' expression ')'
	;

postfix_expression
	: primary_expression
	| postfix_expression '[' expression ']'
	| postfix_expression '(' ')'
	| postfix_expression '(' identifier_list ')'
	;


expression
    : comparison_expression
    | postfix_expression assignment_operator expression
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
    | declarator_list ',' initialise_declarator
    ;

initialise_declarator
    : declarator
    | declarator '=' expression
    ;


// seperates pointer variable declaration and no pointer declaration
declarator
    : pointer direct_declarator
    | direct_declarator
    ;


// the declaration of a variable
direct_declarator
    : IDENTIFIER
    | IDENTIFIER '(' parameter_list ')'
    | IDENTIFIER '(' identifier_list ')'
    | IDENTIFIER '(' ')'
    | direct_declarator '[' expression ']'
    | direct_declarator '[' ']'
    ;


// possible list of values given to a function
identifier_list
    : value
    | identifier_list ',' value
    ;

// possible list of paramaters of a function
parameter_list
    : parameter_declaration
    | parameter_list ',' parameter_declaration
    ;

// all possible type declarations (supporting void and passing functions as arg)
parameter_declaration
	: declaration_specifier declarator
	| declaration_specifier
	;

assignment_operator
    : '='
    ;

filename
    : FILENAME
    | IDENTIFIER '.' IDENTIFIER
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
    : POINTER
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
POINTER: '*';
FILENAME: 'stdio.h';
CONST: 'const';
VOID: 'void';
IDENTIFIER: ('_' | 'a'..'z'| 'A'..'Z')('_' | 'a'..'z'| 'A'..'Z')*; // could be changed to max 30 length
INTEGER: (('1'..'9')('0'..'9')*  | '0');
DECIMAL: (('1'..'9')('0'..'9')*  | '0')('.')('0'..'9')+;
CHARACTER: ('\'')(.)('\'');
WS: ('\t' | '\n' | ' ' | '\r')+ -> skip; //toss out whitespace
COMMENT: ('/*' .*? '*/'  | '//' ~('\n'|'\r')*) -> skip; // toss out comments
