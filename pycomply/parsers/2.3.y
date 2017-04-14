// Generated by transforming |cwd:///python-grammars/bisonified-parsers/2.3.y| on 2016-11-23 at 17:31:13 +0000
%{
	int yylex (void);
	extern int yylineno;
	extern char *yytext;
	void yyerror (const char *);
%}

// 80 tokens, in alphabetical order:
%token AMPEREQUAL AMPERSAND AND ASSERT BACKQUOTE BAR BREAK CIRCUMFLEX CIRCUMFLEXEQUAL
%token CLASS COLON COMMA CONTINUE DEDENT DEF DEL DOT DOUBLESLASH DOUBLESLASHEQUAL
%token DOUBLESTAR DOUBLESTAREQUAL ELIF ELSE ENDMARKER EQEQUAL EQUAL EXCEPT
%token EXEC FINALLY FOR FROM GLOBAL GREATER GREATEREQUAL GRLT IF IMPORT
%token IN INDENT IS LAMBDA LBRACE LEFTSHIFT LEFTSHIFTEQUAL LESS LESSEQUAL
%token LPAR LSQB MINEQUAL MINUS NAME NEWLINE NOT NOTEQUAL NUMBER OR PASS
%token PERCENT PERCENTEQUAL PLUS PLUSEQUAL PRINT RAISE RBRACE RETURN RIGHTSHIFT
%token RIGHTSHIFTEQUAL RPAR RSQB SEMI SLASH SLASHEQUAL STAR STAREQUAL STRING
%token TILDE TRY VBAREQUAL WHILE YIELD

%start start

%locations

%%

start
	: file_input
	;
file_input // Used in: start
	: star_NEWLINE_stmt ENDMARKER
	;
pick_NEWLINE_stmt // Used in: star_NEWLINE_stmt
	: NEWLINE
	| stmt
	;
star_NEWLINE_stmt // Used in: file_input, star_NEWLINE_stmt
	: star_NEWLINE_stmt pick_NEWLINE_stmt
	| %empty
	;
funcdef // Used in: compound_stmt
	: DEF NAME parameters COLON suite
	;
parameters // Used in: funcdef
	: LPAR varargslist RPAR
	| LPAR RPAR
	;
varargslist // Used in: parameters, lambdef
	: star_fpdef_COMMA pick_STAR_DOUBLESTAR
	| star_fpdef_COMMA fpdef opt_EQUAL_test opt_COMMA
	;
opt_EQUAL_test // Used in: varargslist, star_fpdef_COMMA
	: EQUAL test
	| %empty
	;
star_fpdef_COMMA // Used in: varargslist, star_fpdef_COMMA
	: star_fpdef_COMMA fpdef opt_EQUAL_test COMMA
	| %empty
	;
opt_DOUBLESTAR_NAME // Used in: pick_STAR_DOUBLESTAR
	: COMMA DOUBLESTAR NAME
	| %empty
	;
pick_STAR_DOUBLESTAR // Used in: varargslist
	: STAR NAME opt_DOUBLESTAR_NAME
	| DOUBLESTAR NAME
	;
opt_COMMA // Used in: varargslist, opt_test, opt_test_2, listmaker, testlist_safe, pick_argument_short
	: COMMA
	| %empty
	;
fpdef // Used in: varargslist, star_fpdef_COMMA, fplist, star_fpdef_notest
	: NAME
	| LPAR fplist RPAR
	;
fplist // Used in: fpdef
	: fpdef star_fpdef_notest COMMA
	| fpdef star_fpdef_notest
	;
star_fpdef_notest // Used in: fplist, star_fpdef_notest
	: star_fpdef_notest COMMA fpdef
	| %empty
	;
stmt // Used in: pick_NEWLINE_stmt, plus_stmt
	: simple_stmt
	| compound_stmt
	;
simple_stmt // Used in: stmt, suite
	: small_stmt star_SEMI_small_stmt SEMI NEWLINE
	| small_stmt star_SEMI_small_stmt NEWLINE
	;
star_SEMI_small_stmt // Used in: simple_stmt, star_SEMI_small_stmt
	: star_SEMI_small_stmt SEMI small_stmt
	| %empty
	;
small_stmt // Used in: simple_stmt, star_SEMI_small_stmt
	: expr_stmt
	| print_stmt
	| del_stmt
	| pass_stmt
	| flow_stmt
	| import_stmt
	| global_stmt
	| exec_stmt
	| assert_stmt
	;
expr_stmt // Used in: small_stmt
	: testlist augassign testlist
	| testlist star_EQUAL_testlist
	;
star_EQUAL_testlist // Used in: expr_stmt, star_EQUAL_testlist
	: star_EQUAL_testlist EQUAL testlist
	| %empty
	;
augassign // Used in: expr_stmt
	: PLUSEQUAL
	| MINEQUAL
	| STAREQUAL
	| SLASHEQUAL
	| PERCENTEQUAL
	| AMPEREQUAL
	| VBAREQUAL
	| CIRCUMFLEXEQUAL
	| LEFTSHIFTEQUAL
	| RIGHTSHIFTEQUAL
	| DOUBLESTAREQUAL
	| DOUBLESLASHEQUAL
	;
print_stmt // Used in: small_stmt
	: PRINT opt_test
	| PRINT RIGHTSHIFT test opt_test_2
	;
star_COMMA_test // Used in: star_COMMA_test, opt_test, listmaker, testlist
	: star_COMMA_test COMMA test
	| %empty
	;
opt_test // Used in: print_stmt
	: test star_COMMA_test opt_COMMA
	| %empty
	;
plus_COMMA_test // Used in: plus_COMMA_test, opt_test_2, testlist_safe
	: plus_COMMA_test COMMA test
	| COMMA test
	;
opt_test_2 // Used in: print_stmt
	: plus_COMMA_test opt_COMMA
	| %empty
	;
del_stmt // Used in: small_stmt
	: DEL exprlist
	;
pass_stmt // Used in: small_stmt
	: PASS
	;
flow_stmt // Used in: small_stmt
	: break_stmt
	| continue_stmt
	| return_stmt
	| raise_stmt
	| yield_stmt
	;
break_stmt // Used in: flow_stmt
	: BREAK
	;
continue_stmt // Used in: flow_stmt
	: CONTINUE
	;
return_stmt // Used in: flow_stmt
	: RETURN testlist
	| RETURN
	;
yield_stmt // Used in: flow_stmt
	: YIELD testlist
	;
raise_stmt // Used in: flow_stmt
	: RAISE test opt_test_3
	| RAISE
	;
opt_COMMA_test // Used in: opt_test_3, exec_stmt, except_clause
	: COMMA test
	| %empty
	;
opt_test_3 // Used in: raise_stmt
	: COMMA test opt_COMMA_test
	| %empty
	;
import_stmt // Used in: small_stmt
	: IMPORT dotted_as_name star_COMMA_dotted_as_name
	| FROM dotted_name IMPORT pick_STAR_import_as_name
	;
star_COMMA_dotted_as_name // Used in: import_stmt, star_COMMA_dotted_as_name
	: star_COMMA_dotted_as_name COMMA dotted_as_name
	| %empty
	;
star_COMMA_import_as_name // Used in: star_COMMA_import_as_name, pick_STAR_import_as_name
	: star_COMMA_import_as_name COMMA import_as_name
	| %empty
	;
pick_STAR_import_as_name // Used in: import_stmt
	: STAR
	| import_as_name star_COMMA_import_as_name
	;
import_as_name // Used in: star_COMMA_import_as_name, pick_STAR_import_as_name
	: NAME NAME NAME
	| NAME
	;
dotted_as_name // Used in: import_stmt, star_COMMA_dotted_as_name
	: dotted_name NAME NAME
	| dotted_name
	;
dotted_name // Used in: import_stmt, dotted_as_name, dotted_name
	: NAME
	| dotted_name DOT NAME
	;
global_stmt // Used in: small_stmt
	: GLOBAL NAME star_COMMA_NAME
	;
star_COMMA_NAME // Used in: global_stmt, star_COMMA_NAME
	: star_COMMA_NAME COMMA NAME
	| %empty
	;
exec_stmt // Used in: small_stmt
	: EXEC expr IN test opt_COMMA_test
	| EXEC expr
	;
assert_stmt // Used in: small_stmt
	: ASSERT test COMMA test
	| ASSERT test
	;
compound_stmt // Used in: stmt
	: if_stmt
	| while_stmt
	| for_stmt
	| try_stmt
	| funcdef
	| classdef
	;
if_stmt // Used in: compound_stmt
	: IF test COLON suite star_ELIF ELSE COLON suite
	| IF test COLON suite star_ELIF
	;
star_ELIF // Used in: if_stmt, star_ELIF
	: star_ELIF ELIF test COLON suite
	| %empty
	;
while_stmt // Used in: compound_stmt
	: WHILE test COLON suite ELSE COLON suite
	| WHILE test COLON suite
	;
for_stmt // Used in: compound_stmt
	: FOR exprlist IN testlist COLON suite ELSE COLON suite
	| FOR exprlist IN testlist COLON suite
	;
try_stmt // Used in: compound_stmt
	: TRY COLON suite plus_except opt_ELSE
	| TRY COLON suite FINALLY COLON suite
	;
plus_except // Used in: try_stmt, plus_except
	: plus_except except_clause COLON suite
	| except_clause COLON suite
	;
opt_ELSE // Used in: try_stmt
	: ELSE COLON suite
	| %empty
	;
except_clause // Used in: plus_except
	: EXCEPT test opt_COMMA_test
	| EXCEPT
	;
suite // Used in: funcdef, if_stmt, star_ELIF, while_stmt, for_stmt, try_stmt, plus_except, opt_ELSE, classdef
	: simple_stmt
	| NEWLINE INDENT plus_stmt DEDENT
	;
plus_stmt // Used in: suite, plus_stmt
	: plus_stmt stmt
	| stmt
	;
test // Used in: opt_EQUAL_test, print_stmt, star_COMMA_test, opt_test, plus_COMMA_test, raise_stmt, opt_COMMA_test, opt_test_3, exec_stmt, assert_stmt, if_stmt, star_ELIF, while_stmt, except_clause, listmaker, lambdef, subscript, opt_test_only, sliceop, testlist, testlist_safe, dictmaker, star_test_COLON_test, opt_DOUBLESTAR_test, pick_argument_short, argument, list_if, testlist1
	: and_test star_OR_and_test
	| lambdef
	;
star_OR_and_test // Used in: test, star_OR_and_test
	: star_OR_and_test OR and_test
	| %empty
	;
and_test // Used in: test, star_OR_and_test, and_test
	: not_test
	| and_test AND not_test
	;
not_test // Used in: and_test, not_test
	: NOT not_test
	| comparison
	;
comparison // Used in: not_test, comparison
	: expr
	| comparison comp_op expr
	;
comp_op // Used in: comparison
	: LESS
	| GREATER
	| EQEQUAL
	| GREATEREQUAL
	| LESSEQUAL
	| GRLT
	| NOTEQUAL
	| IN
	| NOT IN
	| IS
	| IS NOT
	;
expr // Used in: exec_stmt, comparison, expr, exprlist, star_COMMA_expr
	: xor_expr
	| expr BAR xor_expr
	;
xor_expr // Used in: expr, xor_expr
	: and_expr
	| xor_expr CIRCUMFLEX and_expr
	;
and_expr // Used in: xor_expr, and_expr
	: shift_expr
	| and_expr AMPERSAND shift_expr
	;
shift_expr // Used in: and_expr, shift_expr
	: arith_expr
	| shift_expr pick_LEFTSHIFT_RIGHTSHIFT arith_expr
	;
pick_LEFTSHIFT_RIGHTSHIFT // Used in: shift_expr
	: LEFTSHIFT
	| RIGHTSHIFT
	;
arith_expr // Used in: shift_expr, arith_expr
	: term
	| arith_expr pick_PLUS_MINUS term
	;
pick_PLUS_MINUS // Used in: arith_expr
	: PLUS
	| MINUS
	;
term // Used in: arith_expr, term
	: factor
	| term pick_multop factor
	;
pick_multop // Used in: term
	: STAR
	| SLASH
	| PERCENT
	| DOUBLESLASH
	;
factor // Used in: term, factor, power
	: pick_unop factor
	| power
	;
pick_unop // Used in: factor
	: PLUS
	| MINUS
	| TILDE
	;
power // Used in: factor
	: atom star_trailer DOUBLESTAR factor
	| atom star_trailer
	;
star_trailer // Used in: power, star_trailer
	: star_trailer trailer
	| %empty
	;
atom // Used in: power
	: LPAR opt_testlist RPAR
	| LSQB opt_listmaker RSQB
	| LBRACE opt_dictmaker RBRACE
	| BACKQUOTE testlist1 BACKQUOTE
	| NAME
	| NUMBER
	| plus_STRING
	;
opt_testlist // Used in: atom
	: testlist
	| %empty
	;
opt_listmaker // Used in: atom
	: listmaker
	| %empty
	;
opt_dictmaker // Used in: atom
	: dictmaker
	| %empty
	;
plus_STRING // Used in: atom, plus_STRING
	: plus_STRING STRING
	| STRING
	;
listmaker // Used in: opt_listmaker
	: test list_for
	| test star_COMMA_test opt_COMMA
	;
lambdef // Used in: test
	: LAMBDA varargslist COLON test
	| LAMBDA COLON test
	;
trailer // Used in: star_trailer
	: LPAR opt_arglist RPAR
	| LSQB subscriptlist RSQB
	| DOT NAME
	;
opt_arglist // Used in: trailer
	: arglist
	| %empty
	;
subscriptlist // Used in: trailer
	: subscript star_COMMA_subscript COMMA
	| subscript star_COMMA_subscript
	;
star_COMMA_subscript // Used in: subscriptlist, star_COMMA_subscript
	: star_COMMA_subscript COMMA subscript
	| %empty
	;
subscript // Used in: subscriptlist, star_COMMA_subscript
	: DOT DOT DOT
	| test
	| opt_test_only COLON opt_test_only opt_sliceop
	;
opt_test_only // Used in: subscript
	: test
	| %empty
	;
opt_sliceop // Used in: subscript
	: sliceop
	| %empty
	;
sliceop // Used in: opt_sliceop
	: COLON test
	| COLON
	;
exprlist // Used in: del_stmt, for_stmt, list_for
	: expr star_COMMA_expr COMMA
	| expr star_COMMA_expr
	;
star_COMMA_expr // Used in: exprlist, star_COMMA_expr
	: star_COMMA_expr COMMA expr
	| %empty
	;
testlist // Used in: expr_stmt, star_EQUAL_testlist, return_stmt, yield_stmt, for_stmt, opt_testlist, classdef
	: test star_COMMA_test COMMA
	| test star_COMMA_test
	;
testlist_safe // Used in: list_for
	: test plus_COMMA_test opt_COMMA
	| test
	;
dictmaker // Used in: opt_dictmaker
	: test COLON test star_test_COLON_test COMMA
	| test COLON test star_test_COLON_test
	;
star_test_COLON_test // Used in: dictmaker, star_test_COLON_test
	: star_test_COLON_test COMMA test COLON test
	| %empty
	;
classdef // Used in: compound_stmt
	: CLASS NAME LPAR testlist RPAR COLON suite
	| CLASS NAME COLON suite
	;
arglist // Used in: opt_arglist
	: star_argument_COMMA pick_argument_short
	;
star_argument_COMMA // Used in: arglist, star_argument_COMMA
	: star_argument_COMMA argument COMMA
	| %empty
	;
opt_DOUBLESTAR_test // Used in: pick_argument_short
	: COMMA DOUBLESTAR test
	| %empty
	;
pick_argument_short // Used in: arglist
	: argument opt_COMMA
	| STAR test opt_DOUBLESTAR_test
	| DOUBLESTAR test
	;
argument // Used in: star_argument_COMMA, pick_argument_short
	: test EQUAL test
	| test
	;
list_iter // Used in: list_for, list_if
	: list_for
	| list_if
	;
list_for // Used in: listmaker, list_iter
	: FOR exprlist IN testlist_safe list_iter
	| FOR exprlist IN testlist_safe
	;
list_if // Used in: list_iter
	: IF test list_iter
	| IF test
	;
testlist1 // Used in: atom, testlist1
	: test
	| testlist1 COMMA test
	;

%%

#include <stdio.h>
void yyerror (const char *s)
{
    if(yylloc.first_line > 0)	{
        fprintf (stderr, "%d.%d-%d.%d:", yylloc.first_line, yylloc.first_column,
	                                     yylloc.last_line,  yylloc.last_column);
    }
    fprintf(stderr, " %s with [%s]\n", s, yytext);
}


