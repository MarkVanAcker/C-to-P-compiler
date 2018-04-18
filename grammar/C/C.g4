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
    : assignment ';'
    // | definition -> FUNCTIONS
    | declaration ';'
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

//
assignment
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
    : additive_expression
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


//
definition
    : 'def'
    ;

// different types of declarations making difference between functions and varaibles (void)
declaration
    : declaration_specifier declarator  // char var en func (, ...)
    | function_declaration_specifier function_declarator // void en char func (, ...)
    ;

// defines the type of the declaration ( CONST INT x)
declaration_specifier
    : type_specifier
    | type_specifier declaration_specifier
    | type_qualifier
    | type_qualifier declaration_specifier
    ;

// defines the type of the function declaration (VOID function() )
function_declaration_specifier
    : function_type_specifier
    | function_type_specifier declaration_specifier
    | type_qualifier
    | type_qualifier declaration_specifier
    ;

// seperates pointer function declaration and no pointer declaration
function_declarator
    : pointer function_direct_declarator
    | function_direct_declarator
    ;

// seperates pointer variable declaration and no pointer declaration
declarator
    : pointer direct_declarator
    | direct_declarator
    ;

// the declarator of a function
function_direct_declarator
    : IDENTIFIER '(' parameter_list ')'
    | IDENTIFIER '(' identifier_list ')'
    | IDENTIFIER '(' ')'
    ;

// the declaration of a variable
direct_declarator
    : IDENTIFIER
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
    | function_declaration_specifier function_declarator
	| function_declaration_specifier
	;

assignment_operator
    : '='
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
    ;

// types and void for functions
function_type_specifier
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

CHAR: 'char';
FLOAT: 'float';
INT: 'int';
POINTER: '*';
CONST: 'const';
VOID: 'void';
IDENTIFIER: ('_' | 'a'..'z'| 'A'..'Z')('_' | 'a'..'z'| 'A'..'Z')*; // could be changed to max 30 length
INTEGER: (('1'..'9')('0'..'9')*  | '0');
DECIMAL: (('1'..'9')('0'..'9')*  | '0')('.')('0'..'9')+;
CHARACTER: ('\'')(.)('\'');
WS: ('\t' | '\n' | ' ' | '\r')+ -> skip; //toss out whitespace
COMMENT: ('/*' .*? '*/'  | '//' ~('\n'|'\r')*) -> skip; // toss out comments
