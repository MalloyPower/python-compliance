/* A Bison parser, made by GNU Bison 3.0.4.  */

/* Bison implementation for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015 Free Software Foundation, Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* C LALR(1) parser skeleton written by Richard Stallman, by
   simplifying the original so-called "semantic" parser.  */

/* All symbols defined below should begin with yy or YY, to avoid
   infringing on user name space.  This should be done even for local
   variables, as they might otherwise be expanded by user macros.
   There are some unavoidable exceptions within include files to
   define necessary library symbols; they are noted "INFRINGES ON
   USER NAME SPACE" below.  */

/* Identify Bison output.  */
#define YYBISON 1

/* Bison version.  */
#define YYBISON_VERSION "3.0.4"

/* Skeleton name.  */
#define YYSKELETON_NAME "yacc.c"

/* Pure parsers.  */
#define YYPURE 0

/* Push parsers.  */
#define YYPUSH 0

/* Pull parsers.  */
#define YYPULL 1




/* Copy the first part of user declarations.  */
#line 2 "parse.y" /* yacc.c:339  */

	int yylex (void);
	extern int yylineno;
	extern char *yytext;
	void yyerror (const char *);

#line 73 "parse.tab.c" /* yacc.c:339  */

# ifndef YY_NULLPTR
#  if defined __cplusplus && 201103L <= __cplusplus
#   define YY_NULLPTR nullptr
#  else
#   define YY_NULLPTR 0
#  endif
# endif

/* Enabling verbose error messages.  */
#ifdef YYERROR_VERBOSE
# undef YYERROR_VERBOSE
# define YYERROR_VERBOSE 1
#else
# define YYERROR_VERBOSE 0
#endif

/* In a future release of Bison, this section will be replaced
   by #include "parse.tab.h".  */
#ifndef YY_YY_PARSE_TAB_H_INCLUDED
# define YY_YY_PARSE_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 1
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token type.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    AMPEREQUAL = 258,
    AMPERSAND = 259,
    AND = 260,
    ARROW = 261,
    AS = 262,
    ASSERT = 263,
    AT = 264,
    BAR = 265,
    BREAK = 266,
    CIRCUMFLEX = 267,
    CIRCUMFLEXEQUAL = 268,
    CLASS = 269,
    COLON = 270,
    COMMA = 271,
    CONTINUE = 272,
    DEDENT = 273,
    DEF = 274,
    DEL = 275,
    DOT = 276,
    DOUBLESLASH = 277,
    DOUBLESLASHEQUAL = 278,
    DOUBLESTAR = 279,
    DOUBLESTAREQUAL = 280,
    ELIF = 281,
    ELSE = 282,
    ENDMARKER = 283,
    EQEQUAL = 284,
    EQUAL = 285,
    EXCEPT = 286,
    FALSE = 287,
    FINALLY = 288,
    FOR = 289,
    FROM = 290,
    GLOBAL = 291,
    GREATER = 292,
    GREATEREQUAL = 293,
    GRLT = 294,
    IF = 295,
    IMPORT = 296,
    IN = 297,
    INDENT = 298,
    IS = 299,
    LAMBDA = 300,
    LBRACE = 301,
    LEFTSHIFT = 302,
    LEFTSHIFTEQUAL = 303,
    LESS = 304,
    LESSEQUAL = 305,
    LPAR = 306,
    LSQB = 307,
    MINEQUAL = 308,
    MINUS = 309,
    NAME = 310,
    NEWLINE = 311,
    NONE = 312,
    NONLOCAL = 313,
    NOT = 314,
    NOTEQUAL = 315,
    NUMBER = 316,
    OR = 317,
    PASS = 318,
    PERCENT = 319,
    PERCENTEQUAL = 320,
    PLUS = 321,
    PLUSEQUAL = 322,
    RAISE = 323,
    RBRACE = 324,
    RETURN = 325,
    RIGHTSHIFT = 326,
    RIGHTSHIFTEQUAL = 327,
    RPAR = 328,
    RSQB = 329,
    SEMI = 330,
    SLASH = 331,
    SLASHEQUAL = 332,
    STAR = 333,
    STAREQUAL = 334,
    STRING = 335,
    THREE_DOTS = 336,
    TILDE = 337,
    TRUE = 338,
    TRY = 339,
    VBAREQUAL = 340,
    WHILE = 341,
    WITH = 342,
    YIELD = 343
  };
#endif

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif

/* Location type.  */
#if ! defined YYLTYPE && ! defined YYLTYPE_IS_DECLARED
typedef struct YYLTYPE YYLTYPE;
struct YYLTYPE
{
  int first_line;
  int first_column;
  int last_line;
  int last_column;
};
# define YYLTYPE_IS_DECLARED 1
# define YYLTYPE_IS_TRIVIAL 1
#endif


extern YYSTYPE yylval;
extern YYLTYPE yylloc;
int yyparse (void);

#endif /* !YY_YY_PARSE_TAB_H_INCLUDED  */

/* Copy the second part of user declarations.  */

#line 227 "parse.tab.c" /* yacc.c:358  */

#ifdef short
# undef short
#endif

#ifdef YYTYPE_UINT8
typedef YYTYPE_UINT8 yytype_uint8;
#else
typedef unsigned char yytype_uint8;
#endif

#ifdef YYTYPE_INT8
typedef YYTYPE_INT8 yytype_int8;
#else
typedef signed char yytype_int8;
#endif

#ifdef YYTYPE_UINT16
typedef YYTYPE_UINT16 yytype_uint16;
#else
typedef unsigned short int yytype_uint16;
#endif

#ifdef YYTYPE_INT16
typedef YYTYPE_INT16 yytype_int16;
#else
typedef short int yytype_int16;
#endif

#ifndef YYSIZE_T
# ifdef __SIZE_TYPE__
#  define YYSIZE_T __SIZE_TYPE__
# elif defined size_t
#  define YYSIZE_T size_t
# elif ! defined YYSIZE_T
#  include <stddef.h> /* INFRINGES ON USER NAME SPACE */
#  define YYSIZE_T size_t
# else
#  define YYSIZE_T unsigned int
# endif
#endif

#define YYSIZE_MAXIMUM ((YYSIZE_T) -1)

#ifndef YY_
# if defined YYENABLE_NLS && YYENABLE_NLS
#  if ENABLE_NLS
#   include <libintl.h> /* INFRINGES ON USER NAME SPACE */
#   define YY_(Msgid) dgettext ("bison-runtime", Msgid)
#  endif
# endif
# ifndef YY_
#  define YY_(Msgid) Msgid
# endif
#endif

#ifndef YY_ATTRIBUTE
# if (defined __GNUC__                                               \
      && (2 < __GNUC__ || (__GNUC__ == 2 && 96 <= __GNUC_MINOR__)))  \
     || defined __SUNPRO_C && 0x5110 <= __SUNPRO_C
#  define YY_ATTRIBUTE(Spec) __attribute__(Spec)
# else
#  define YY_ATTRIBUTE(Spec) /* empty */
# endif
#endif

#ifndef YY_ATTRIBUTE_PURE
# define YY_ATTRIBUTE_PURE   YY_ATTRIBUTE ((__pure__))
#endif

#ifndef YY_ATTRIBUTE_UNUSED
# define YY_ATTRIBUTE_UNUSED YY_ATTRIBUTE ((__unused__))
#endif

#if !defined _Noreturn \
     && (!defined __STDC_VERSION__ || __STDC_VERSION__ < 201112)
# if defined _MSC_VER && 1200 <= _MSC_VER
#  define _Noreturn __declspec (noreturn)
# else
#  define _Noreturn YY_ATTRIBUTE ((__noreturn__))
# endif
#endif

/* Suppress unused-variable warnings by "using" E.  */
#if ! defined lint || defined __GNUC__
# define YYUSE(E) ((void) (E))
#else
# define YYUSE(E) /* empty */
#endif

#if defined __GNUC__ && 407 <= __GNUC__ * 100 + __GNUC_MINOR__
/* Suppress an incorrect diagnostic about yylval being uninitialized.  */
# define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN \
    _Pragma ("GCC diagnostic push") \
    _Pragma ("GCC diagnostic ignored \"-Wuninitialized\"")\
    _Pragma ("GCC diagnostic ignored \"-Wmaybe-uninitialized\"")
# define YY_IGNORE_MAYBE_UNINITIALIZED_END \
    _Pragma ("GCC diagnostic pop")
#else
# define YY_INITIAL_VALUE(Value) Value
#endif
#ifndef YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_END
#endif
#ifndef YY_INITIAL_VALUE
# define YY_INITIAL_VALUE(Value) /* Nothing. */
#endif


#if ! defined yyoverflow || YYERROR_VERBOSE

/* The parser invokes alloca or malloc; define the necessary symbols.  */

# ifdef YYSTACK_USE_ALLOCA
#  if YYSTACK_USE_ALLOCA
#   ifdef __GNUC__
#    define YYSTACK_ALLOC __builtin_alloca
#   elif defined __BUILTIN_VA_ARG_INCR
#    include <alloca.h> /* INFRINGES ON USER NAME SPACE */
#   elif defined _AIX
#    define YYSTACK_ALLOC __alloca
#   elif defined _MSC_VER
#    include <malloc.h> /* INFRINGES ON USER NAME SPACE */
#    define alloca _alloca
#   else
#    define YYSTACK_ALLOC alloca
#    if ! defined _ALLOCA_H && ! defined EXIT_SUCCESS
#     include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
      /* Use EXIT_SUCCESS as a witness for stdlib.h.  */
#     ifndef EXIT_SUCCESS
#      define EXIT_SUCCESS 0
#     endif
#    endif
#   endif
#  endif
# endif

# ifdef YYSTACK_ALLOC
   /* Pacify GCC's 'empty if-body' warning.  */
#  define YYSTACK_FREE(Ptr) do { /* empty */; } while (0)
#  ifndef YYSTACK_ALLOC_MAXIMUM
    /* The OS might guarantee only one guard page at the bottom of the stack,
       and a page size can be as small as 4096 bytes.  So we cannot safely
       invoke alloca (N) if N exceeds 4096.  Use a slightly smaller number
       to allow for a few compiler-allocated temporary stack slots.  */
#   define YYSTACK_ALLOC_MAXIMUM 4032 /* reasonable circa 2006 */
#  endif
# else
#  define YYSTACK_ALLOC YYMALLOC
#  define YYSTACK_FREE YYFREE
#  ifndef YYSTACK_ALLOC_MAXIMUM
#   define YYSTACK_ALLOC_MAXIMUM YYSIZE_MAXIMUM
#  endif
#  if (defined __cplusplus && ! defined EXIT_SUCCESS \
       && ! ((defined YYMALLOC || defined malloc) \
             && (defined YYFREE || defined free)))
#   include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
#   ifndef EXIT_SUCCESS
#    define EXIT_SUCCESS 0
#   endif
#  endif
#  ifndef YYMALLOC
#   define YYMALLOC malloc
#   if ! defined malloc && ! defined EXIT_SUCCESS
void *malloc (YYSIZE_T); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
#  ifndef YYFREE
#   define YYFREE free
#   if ! defined free && ! defined EXIT_SUCCESS
void free (void *); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
# endif
#endif /* ! defined yyoverflow || YYERROR_VERBOSE */


#if (! defined yyoverflow \
     && (! defined __cplusplus \
         || (defined YYLTYPE_IS_TRIVIAL && YYLTYPE_IS_TRIVIAL \
             && defined YYSTYPE_IS_TRIVIAL && YYSTYPE_IS_TRIVIAL)))

/* A type that is properly aligned for any stack member.  */
union yyalloc
{
  yytype_int16 yyss_alloc;
  YYSTYPE yyvs_alloc;
  YYLTYPE yyls_alloc;
};

/* The size of the maximum gap between one aligned stack and the next.  */
# define YYSTACK_GAP_MAXIMUM (sizeof (union yyalloc) - 1)

/* The size of an array large to enough to hold all stacks, each with
   N elements.  */
# define YYSTACK_BYTES(N) \
     ((N) * (sizeof (yytype_int16) + sizeof (YYSTYPE) + sizeof (YYLTYPE)) \
      + 2 * YYSTACK_GAP_MAXIMUM)

# define YYCOPY_NEEDED 1

/* Relocate STACK from its old location to the new one.  The
   local variables YYSIZE and YYSTACKSIZE give the old and new number of
   elements in the stack, and YYPTR gives the new location of the
   stack.  Advance YYPTR to a properly aligned location for the next
   stack.  */
# define YYSTACK_RELOCATE(Stack_alloc, Stack)                           \
    do                                                                  \
      {                                                                 \
        YYSIZE_T yynewbytes;                                            \
        YYCOPY (&yyptr->Stack_alloc, Stack, yysize);                    \
        Stack = &yyptr->Stack_alloc;                                    \
        yynewbytes = yystacksize * sizeof (*Stack) + YYSTACK_GAP_MAXIMUM; \
        yyptr += yynewbytes / sizeof (*yyptr);                          \
      }                                                                 \
    while (0)

#endif

#if defined YYCOPY_NEEDED && YYCOPY_NEEDED
/* Copy COUNT objects from SRC to DST.  The source and destination do
   not overlap.  */
# ifndef YYCOPY
#  if defined __GNUC__ && 1 < __GNUC__
#   define YYCOPY(Dst, Src, Count) \
      __builtin_memcpy (Dst, Src, (Count) * sizeof (*(Src)))
#  else
#   define YYCOPY(Dst, Src, Count)              \
      do                                        \
        {                                       \
          YYSIZE_T yyi;                         \
          for (yyi = 0; yyi < (Count); yyi++)   \
            (Dst)[yyi] = (Src)[yyi];            \
        }                                       \
      while (0)
#  endif
# endif
#endif /* !YYCOPY_NEEDED */

/* YYFINAL -- State number of the termination state.  */
#define YYFINAL  4
/* YYLAST -- Last index in YYTABLE.  */
#define YYLAST   974

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  89
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  135
/* YYNRULES -- Number of rules.  */
#define YYNRULES  303
/* YYNSTATES -- Number of states.  */
#define YYNSTATES  455

/* YYTRANSLATE[YYX] -- Symbol number corresponding to YYX as returned
   by yylex, with out-of-bounds checking.  */
#define YYUNDEFTOK  2
#define YYMAXUTOK   343

#define YYTRANSLATE(YYX)                                                \
  ((unsigned int) (YYX) <= YYMAXUTOK ? yytranslate[YYX] : YYUNDEFTOK)

/* YYTRANSLATE[TOKEN-NUM] -- Symbol number corresponding to TOKEN-NUM
   as returned by yylex, without out-of-bounds checking.  */
static const yytype_uint8 yytranslate[] =
{
       0,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     1,     2,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16,    17,    18,    19,    20,    21,    22,    23,    24,
      25,    26,    27,    28,    29,    30,    31,    32,    33,    34,
      35,    36,    37,    38,    39,    40,    41,    42,    43,    44,
      45,    46,    47,    48,    49,    50,    51,    52,    53,    54,
      55,    56,    57,    58,    59,    60,    61,    62,    63,    64,
      65,    66,    67,    68,    69,    70,    71,    72,    73,    74,
      75,    76,    77,    78,    79,    80,    81,    82,    83,    84,
      85,    86,    87,    88
};

#if YYDEBUG
  /* YYRLINE[YYN] -- Source line where rule number YYN was defined.  */
static const yytype_uint16 yyrline[] =
{
       0,    28,    28,    31,    34,    35,    38,    39,    42,    43,
      46,    47,    50,    51,    54,    55,    58,    59,    62,    63,
      66,    67,    70,    71,    74,    75,    78,    79,    82,    83,
      86,    87,    90,    91,    94,    95,    98,    99,   102,   103,
     106,   107,   110,   111,   114,   115,   118,   121,   122,   125,
     126,   129,   130,   133,   134,   135,   136,   137,   138,   139,
     140,   143,   144,   147,   148,   151,   152,   155,   156,   157,
     158,   159,   160,   161,   162,   163,   164,   165,   166,   169,
     172,   175,   176,   177,   178,   179,   182,   185,   188,   189,
     192,   195,   196,   199,   200,   203,   204,   207,   210,   213,
     214,   217,   218,   221,   222,   223,   226,   227,   230,   231,
     234,   235,   238,   239,   242,   243,   246,   247,   250,   253,
     254,   257,   260,   261,   264,   265,   266,   267,   268,   269,
     270,   271,   274,   275,   278,   279,   282,   283,   286,   287,
     290,   291,   294,   295,   298,   299,   302,   303,   306,   309,
     310,   313,   314,   317,   318,   321,   322,   325,   326,   329,
     330,   333,   334,   337,   338,   341,   342,   345,   346,   349,
     350,   353,   354,   357,   358,   361,   362,   365,   366,   369,
     370,   371,   372,   373,   374,   375,   376,   377,   378,   379,
     382,   383,   386,   387,   390,   391,   394,   395,   398,   399,
     402,   403,   406,   407,   410,   411,   414,   415,   418,   419,
     420,   421,   424,   425,   428,   429,   430,   433,   434,   437,
     438,   441,   442,   443,   444,   445,   446,   447,   448,   449,
     450,   453,   454,   457,   458,   461,   462,   465,   466,   469,
     470,   473,   474,   477,   478,   481,   482,   483,   486,   487,
     490,   491,   494,   495,   498,   499,   502,   503,   506,   507,
     510,   511,   514,   515,   518,   519,   522,   523,   526,   527,
     530,   531,   534,   535,   538,   539,   542,   545,   546,   549,
     550,   553,   554,   557,   558,   559,   562,   563,   566,   567,
     570,   571,   574,   575,   578,   579,   582,   583,   586,   587,
     590,   591,   594,   595
};
#endif

#if YYDEBUG || YYERROR_VERBOSE || 0
/* YYTNAME[SYMBOL-NUM] -- String name of the symbol SYMBOL-NUM.
   First, the terminals, then, starting at YYNTOKENS, nonterminals.  */
static const char *const yytname[] =
{
  "$end", "error", "$undefined", "AMPEREQUAL", "AMPERSAND", "AND",
  "ARROW", "AS", "ASSERT", "AT", "BAR", "BREAK", "CIRCUMFLEX",
  "CIRCUMFLEXEQUAL", "CLASS", "COLON", "COMMA", "CONTINUE", "DEDENT",
  "DEF", "DEL", "DOT", "DOUBLESLASH", "DOUBLESLASHEQUAL", "DOUBLESTAR",
  "DOUBLESTAREQUAL", "ELIF", "ELSE", "ENDMARKER", "EQEQUAL", "EQUAL",
  "EXCEPT", "FALSE", "FINALLY", "FOR", "FROM", "GLOBAL", "GREATER",
  "GREATEREQUAL", "GRLT", "IF", "IMPORT", "IN", "INDENT", "IS", "LAMBDA",
  "LBRACE", "LEFTSHIFT", "LEFTSHIFTEQUAL", "LESS", "LESSEQUAL", "LPAR",
  "LSQB", "MINEQUAL", "MINUS", "NAME", "NEWLINE", "NONE", "NONLOCAL",
  "NOT", "NOTEQUAL", "NUMBER", "OR", "PASS", "PERCENT", "PERCENTEQUAL",
  "PLUS", "PLUSEQUAL", "RAISE", "RBRACE", "RETURN", "RIGHTSHIFT",
  "RIGHTSHIFTEQUAL", "RPAR", "RSQB", "SEMI", "SLASH", "SLASHEQUAL", "STAR",
  "STAREQUAL", "STRING", "THREE_DOTS", "TILDE", "TRUE", "TRY", "VBAREQUAL",
  "WHILE", "WITH", "YIELD", "$accept", "start", "file_input",
  "pick_NEWLINE_stmt", "star_NEWLINE_stmt", "decorator", "opt_arglist",
  "decorators", "decorated", "funcdef", "parameters", "typedargslist",
  "opt_EQUAL_test", "opt_tfpdef", "star_COMMA_tfpdef",
  "opt_DOUBLESTAR_tfpdef", "pick_STAR_DOUBLESTAR_tfpdef", "opt_COMMA",
  "tfpdef", "varargslist", "opt_vfpdef", "star_COMMA_vfpdef",
  "opt_DOUBLESTAR_vfpdef", "pick_STAR_DOUBLESTAR_vfpdef", "vfpdef", "stmt",
  "simple_stmt", "star_SEMI_small_stmt", "small_stmt", "expr_stmt",
  "pick_yield_expr_testlist", "star_EQUAL", "augassign", "del_stmt",
  "pass_stmt", "flow_stmt", "break_stmt", "continue_stmt", "return_stmt",
  "yield_stmt", "raise_stmt", "opt_FROM_test", "import_stmt",
  "import_name", "import_from", "pick_DOT_THREE_DOTS", "pick_dotted_name",
  "pick_STAR_import", "import_as_name", "dotted_as_name",
  "import_as_names", "star_COMMA_import_as_name", "dotted_as_names",
  "dotted_name", "global_stmt", "star_COMMA_NAME", "nonlocal_stmt",
  "assert_stmt", "compound_stmt", "if_stmt", "star_ELIF", "while_stmt",
  "for_stmt", "try_stmt", "plus_except", "opt_ELSE", "opt_FINALLY",
  "with_stmt", "star_COMMA_with_item", "with_item", "except_clause",
  "opt_AS_NAME", "suite", "plus_stmt", "test", "opt_IF_ELSE",
  "test_nocond", "lambdef", "lambdef_nocond", "or_test", "and_test",
  "not_test", "comparison", "comp_op", "star_expr", "expr", "xor_expr",
  "and_expr", "shift_expr", "pick_LEFTSHIFT_RIGHTSHIFT", "arith_expr",
  "pick_PLUS_MINUS", "term", "pick_multop", "factor", "pick_unop", "power",
  "star_trailer", "atom", "pick_yield_expr_testlist_comp",
  "opt_yield_test", "opt_testlist_comp", "opt_dictorsetmaker",
  "plus_STRING", "testlist_comp", "star_COMMA_test", "trailer",
  "subscriptlist", "star_COMMA_subscript", "subscript", "opt_test_only",
  "opt_sliceop", "sliceop", "exprlist", "star_COMMA_star_expr", "testlist",
  "dictorsetmaker", "star_test_COLON_test", "pick_for_test_test",
  "pick_for_test", "classdef", "arglist", "star_argument_COMMA",
  "star_COMMA_argument", "opt_DOUBLESTAR_test", "pick_argument",
  "argument", "opt_comp_for", "comp_iter", "comp_for", "comp_if",
  "yield_expr", "star_tfpdef_COMMA", "star_vfpdef_COMMA", "star_DOT", YY_NULLPTR
};
#endif

# ifdef YYPRINT
/* YYTOKNUM[NUM] -- (External) token number corresponding to the
   (internal) symbol number NUM (which must be that of a token).  */
static const yytype_uint16 yytoknum[] =
{
       0,   256,   257,   258,   259,   260,   261,   262,   263,   264,
     265,   266,   267,   268,   269,   270,   271,   272,   273,   274,
     275,   276,   277,   278,   279,   280,   281,   282,   283,   284,
     285,   286,   287,   288,   289,   290,   291,   292,   293,   294,
     295,   296,   297,   298,   299,   300,   301,   302,   303,   304,
     305,   306,   307,   308,   309,   310,   311,   312,   313,   314,
     315,   316,   317,   318,   319,   320,   321,   322,   323,   324,
     325,   326,   327,   328,   329,   330,   331,   332,   333,   334,
     335,   336,   337,   338,   339,   340,   341,   342,   343
};
# endif

#define YYPACT_NINF -398

#define yypact_value_is_default(Yystate) \
  (!!((Yystate) == (-398)))

#define YYTABLE_NINF -256

#define yytable_value_is_error(Yytable_value) \
  0

  /* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
     STATE-NUM.  */
static const yytype_int16 yypact[] =
{
    -398,    53,  -398,   385,  -398,   779,    23,  -398,    46,  -398,
      71,   853,  -398,  -398,   853,  -398,    72,   779,    23,   113,
     779,   740,   779,  -398,  -398,  -398,  -398,    75,   835,  -398,
    -398,  -398,   779,   779,   891,  -398,  -398,  -398,  -398,   114,
     779,   779,   779,  -398,  -398,    91,  -398,  -398,  -398,  -398,
    -398,  -398,  -398,  -398,  -398,  -398,  -398,  -398,  -398,  -398,
    -398,  -398,  -398,  -398,  -398,  -398,  -398,  -398,  -398,  -398,
    -398,  -398,  -398,  -398,    22,   126,  -398,    96,  -398,   127,
     131,   143,   -10,    25,     7,  -398,   891,  -398,  -398,    69,
      27,  -398,  -398,   134,  -398,    12,    16,   100,  -398,  -398,
     110,   112,     5,  -398,   139,  -398,   141,    36,   779,   145,
      15,    30,    89,  -398,   128,  -398,    90,  -398,  -398,    94,
    -398,  -398,  -398,   129,  -398,   127,   628,   155,  -398,   164,
    -398,  -398,  -398,  -398,     2,   156,   835,   835,  -398,   835,
    -398,  -398,  -398,  -398,  -398,   115,  -398,  -398,   133,  -398,
     853,   891,   891,   891,  -398,  -398,   891,  -398,  -398,   891,
    -398,  -398,  -398,  -398,   891,  -398,    45,  -398,  -398,  -398,
    -398,  -398,  -398,  -398,  -398,  -398,  -398,  -398,  -398,  -398,
     148,   740,   779,   118,   106,  -398,   628,   106,   107,    92,
     166,   779,    -4,  -398,  -398,   144,   163,   170,   628,    23,
     132,  -398,   779,   135,  -398,   135,  -398,   158,   779,   853,
     176,  -398,  -398,  -398,   176,  -398,  -398,  -398,   170,   779,
    -398,   150,  -398,    78,   628,   102,   891,  -398,   682,   779,
      19,   126,  -398,  -398,  -398,  -398,   131,   143,   -10,    25,
       7,  -398,   140,   891,   106,   779,  -398,   740,  -398,  -398,
    -398,  -398,  -398,   121,  -398,   300,  -398,   125,  -398,   137,
      17,   779,   628,   853,   184,   146,   195,  -398,  -398,  -398,
    -398,   152,  -398,  -398,  -398,  -398,  -398,  -398,  -398,   779,
     189,   128,   171,   779,  -398,  -398,  -398,   547,   779,   200,
      28,   201,   190,   628,   779,   127,  -398,  -398,  -398,   779,
    -398,  -398,   147,   203,   149,  -398,   204,  -398,   172,   779,
     779,    86,  -398,   206,   212,  -398,   174,   215,   174,  -398,
     158,   216,  -398,  -398,   628,   159,   179,   219,  -398,    97,
     221,  -398,   223,  -398,   225,  -398,  -398,   835,  -398,   466,
     232,   628,   227,   210,   229,   628,   230,  -398,  -398,  -398,
    -398,  -398,   233,   779,  -398,  -398,  -398,   127,   779,  -398,
    -398,   173,  -398,   628,  -398,   779,  -398,  -398,   237,   628,
     228,  -398,  -398,   146,   779,   242,    10,  -398,   779,  -398,
      14,  -398,  -398,   197,  -398,  -398,   628,   243,  -398,   628,
    -398,   628,   236,  -398,   244,   245,  -398,  -398,  -398,   246,
     173,  -398,  -398,   248,  -398,   249,   628,   135,   158,   250,
     797,  -398,  -398,  -398,  -398,  -398,   628,  -398,  -398,  -398,
     779,  -398,  -398,   722,  -398,    18,  -398,   628,   628,  -398,
    -398,  -398,   779,   251,    74,  -398,   198,  -398,  -398,   779,
    -398,   174,   158,  -398,  -398,  -398,   797,   252,  -398,  -398,
    -398,  -398,  -398,   797,  -398
};

  /* YYDEFACT[STATE-NUM] -- Default reduction number in state STATE-NUM.
     Performed when YYTABLE does not specify something else to do.  Zero
     means the default is an error.  */
static const yytype_uint16 yydefact[] =
{
       7,     0,     2,     0,     1,     0,     0,    86,     0,    87,
       0,     0,     3,   230,     0,   303,     0,     0,     0,   301,
     238,   234,   236,   215,   224,     4,   228,     0,     0,   225,
      80,   214,    92,    89,     0,   240,   227,   216,   229,     0,
       0,     0,   297,     6,    13,     0,   131,   129,     5,    47,
      52,    53,    54,    55,    56,    81,    82,    83,    85,    84,
      57,    95,    96,    58,    59,    60,    48,   124,   125,   126,
     127,   128,   244,   162,   164,   171,   173,   176,   177,   191,
     192,   194,   196,   198,   202,   206,     0,   213,   220,   226,
      66,   130,    90,   123,   116,     0,     0,     0,   263,    79,
       0,     0,     0,   120,     0,   114,    97,   109,     0,     0,
       0,   244,     0,   237,   244,   233,     0,   232,   231,     0,
     235,   120,   175,    94,    88,   190,     0,     0,   150,   152,
     296,    12,    15,    14,     0,   265,     0,     0,   161,     0,
     181,   180,   182,   184,   186,   188,   179,   183,     0,   185,
       0,     0,     0,     0,   200,   201,     0,   205,   204,     0,
     211,   210,   209,   208,     0,   212,   218,   239,    72,    74,
      78,    77,    75,    68,    71,    67,    76,    70,    69,    73,
      62,     0,     0,     0,   278,     9,     0,   278,   299,     0,
     261,     0,     0,    99,   100,   302,   101,   118,     0,     0,
       0,   168,     0,     0,    46,    39,    36,    23,     0,     0,
      33,   267,   272,   223,    33,   241,   221,   222,   121,     0,
      91,     0,   157,     0,     0,     0,     0,    50,     0,   264,
       0,   172,   174,   189,   187,   178,   193,   195,   197,   199,
     203,   207,     0,     0,   278,   255,   219,     0,    61,    64,
      63,   122,   117,     0,    10,     0,   275,     0,    19,     0,
       0,     0,     0,   260,     0,     0,   107,   103,    98,   113,
     105,     0,   135,   115,   108,   167,    45,    41,    38,     0,
      33,   269,     0,    32,   273,   242,    93,     0,   154,     0,
     145,     0,   137,     0,     0,   151,    49,    51,   243,     0,
     247,   217,     0,   252,     0,   251,     0,    65,     0,     0,
       0,   289,   276,    33,     0,    18,     0,    35,    25,    20,
      23,     0,    17,   262,     0,     0,     0,   111,   119,   133,
      43,    22,   300,    37,    33,   266,   270,     0,   160,     0,
     156,     0,     0,   147,     0,     0,     0,   148,   149,   163,
     245,   246,   249,   255,     8,   285,   280,   190,     0,   286,
     288,   277,   283,     0,    31,     0,    27,    24,    33,     0,
     139,   104,   106,   110,     0,     0,     0,    44,    32,   271,
     293,   158,   159,     0,   153,   141,     0,     0,   140,     0,
     143,     0,   248,   254,   257,   282,   287,   274,    34,    29,
     298,    21,    16,     0,   112,     0,     0,     0,    23,     0,
       0,   292,   290,   291,   155,   144,     0,   142,   136,   250,
     259,   253,   256,     0,   284,     0,    30,     0,     0,   132,
      42,    40,     0,   301,   295,   166,   165,   146,   258,     0,
     279,     0,    23,   138,   134,   268,     0,     0,   294,   281,
      28,    26,   170,     0,   169
};

  /* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -398,  -398,  -398,  -398,  -398,   224,  -155,  -398,  -398,   226,
    -398,  -398,  -306,  -398,  -398,  -398,  -398,  -192,  -293,  -163,
    -398,  -398,  -398,  -398,  -195,  -249,    -2,  -398,    44,  -398,
      26,  -398,  -398,  -398,  -398,  -398,  -398,  -398,  -398,  -398,
    -398,  -398,  -398,  -398,  -398,  -398,  -398,  -398,   -98,    77,
      21,  -398,  -398,    13,  -398,   175,  -398,  -398,  -398,  -398,
    -398,  -398,  -398,  -398,  -398,  -398,  -398,  -398,  -398,   -15,
      -6,  -398,  -180,  -398,    -5,  -398,  -397,  -398,  -398,  -133,
     161,     0,  -398,  -398,    -9,   -30,   157,   151,   153,  -398,
     136,  -398,   142,  -398,   -77,  -398,  -398,  -398,  -398,  -398,
    -398,  -398,  -398,  -398,   277,     8,  -398,  -398,  -398,   -92,
     -46,  -398,  -398,    -1,  -398,   -22,  -398,  -398,  -398,  -398,
     264,  -398,  -398,  -398,  -398,  -398,  -113,  -398,  -123,   -90,
    -398,   -14,  -398,  -398,  -398
};

  /* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
      -1,     1,     2,    43,     3,    44,   253,    45,    46,    47,
     189,   259,   280,   366,   399,   426,   319,   284,   320,   109,
     277,   330,   377,   206,   207,    48,   222,   134,    50,    51,
     248,   180,   181,    52,    53,    54,    55,    56,    57,    58,
      59,   220,    60,    61,    62,   195,   101,   268,   269,   105,
     270,   327,   106,   107,    63,   197,    64,    65,    66,    67,
     329,    68,    69,    70,   290,   343,   388,    71,   225,   128,
     291,   384,   223,   339,    72,   138,   434,    73,   435,    74,
      75,    76,    77,   150,    78,    79,    80,    81,    82,   156,
      83,   159,    84,   164,    85,    86,    87,   166,    88,   115,
     116,   119,   112,    89,   117,   135,   246,   304,   352,   305,
     306,   421,   422,    99,   190,    90,   113,   334,   335,   211,
      91,   254,   255,   395,   424,   312,   313,   359,   411,   412,
     413,    92,   260,   110,   102
};

  /* YYTABLE[YYPACT[STATE-NUM]] -- What to do in state STATE-NUM.  If
     positive, shift that token.  If negative, reduce the rule whose
     number is the opposite.  If YYTABLE_NINF, syntax error.  */
static const yytype_int16 yytable[] =
{
      93,    49,    98,   230,   125,    98,   256,   118,   276,   165,
     278,   124,   104,   100,   368,   111,   114,   114,   272,    95,
     130,   212,   285,   364,   215,   367,   193,   123,   122,   160,
     168,   186,   257,   183,   407,   127,   129,   154,   338,   203,
     169,   316,   441,   200,   292,   208,   299,   265,   209,   452,
     170,   266,   171,     4,   410,   342,   454,   183,   227,   288,
      94,   155,   136,   184,   209,   204,   242,   187,   185,   243,
     204,   161,   317,   317,   267,   172,   137,   228,    94,   157,
     173,   137,   322,   162,   137,   163,   194,   241,   333,   302,
     382,   158,   174,   205,   175,   318,   244,   245,   261,   176,
       6,    96,   431,   201,   177,     8,   178,   262,   209,   288,
      10,   289,   179,   347,   410,   196,   358,   293,   294,   210,
     209,   362,   214,   374,   375,   140,    97,   103,   108,   126,
     121,   139,   442,   141,   142,   143,   451,   151,   144,   232,
     145,   235,   379,   152,   370,   146,   147,   153,   450,   167,
     182,   188,   191,   192,   198,   148,   149,   199,   213,   249,
     202,   385,   209,   216,   219,   390,   301,   250,   217,   264,
     224,   226,   229,   252,   233,   234,   401,   251,   247,   -11,
     258,   408,   263,   397,   183,  -102,   271,   274,   279,   402,
     204,   336,   283,   287,   308,   300,   295,   275,   314,   324,
      98,   266,   326,   281,   380,   332,   415,   328,   282,   417,
     315,   418,   430,   337,   286,   341,   345,   346,  -254,   353,
     350,   360,   361,   351,   298,   249,   429,   363,   354,   317,
     365,   369,   371,   250,   372,   373,   437,   376,   -32,   383,
     303,   378,   386,   387,   389,   391,   -32,   443,   444,   392,
     311,  -255,   414,   400,   323,   403,   321,   406,   416,   420,
     137,   423,   425,   427,   428,   432,   446,   453,    13,   131,
     447,   132,   297,   307,   331,   404,   273,   436,   298,   348,
     357,    19,    20,   340,   344,    49,   325,    21,    22,   129,
      23,    24,   239,    26,   349,    28,   218,    29,   231,   120,
     419,   240,    31,   237,   355,   356,   238,   394,   236,   133,
     440,   448,     0,   436,    34,     0,    35,    36,    37,    38,
     436,     0,     0,     0,   309,     0,     0,     0,     0,     0,
       0,     0,    13,     0,     0,     0,     0,    49,     0,     0,
       0,     0,     0,     0,     0,    19,    20,     0,   393,     0,
       0,    21,    22,   396,    23,    24,     0,    26,     0,    28,
     398,    29,     0,     0,     0,     0,    31,     0,     0,   405,
       0,     0,     0,   409,     0,     0,     0,     0,   310,     0,
      35,    36,    37,    38,     0,     0,     0,   303,     0,     0,
       0,     0,     0,     5,     6,     0,     7,     0,     0,     8,
       0,     0,     9,     0,    10,    11,     0,     0,     0,     0,
       0,     0,     0,    12,     0,   438,     0,    13,   311,    14,
      15,    16,     0,     0,     0,    17,    18,   445,     0,     0,
      19,    20,     0,     0,   449,     0,    21,    22,     0,    23,
      24,    25,    26,    27,    28,     0,    29,     0,    30,     0,
       0,    31,     0,    32,     0,    33,     0,     0,     0,     0,
       0,     0,     0,    34,     0,    35,    36,    37,    38,    39,
       0,    40,    41,    42,     5,     6,     0,     7,     0,     0,
       8,     0,     0,     9,   381,    10,    11,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    13,     0,
      14,    15,    16,     0,     0,     0,    17,    18,     0,     0,
       0,    19,    20,     0,     0,     0,     0,    21,    22,     0,
      23,    24,     0,    26,    27,    28,     0,    29,     0,    30,
       0,     0,    31,     0,    32,     0,    33,     0,     0,     0,
       0,     0,     0,     0,    34,     0,    35,    36,    37,    38,
      39,     0,    40,    41,    42,     5,     6,     0,     7,     0,
       0,     8,     0,     0,     9,     0,    10,    11,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    13,
       0,    14,    15,    16,     0,     0,     0,    17,    18,     0,
       0,     0,    19,    20,     0,     0,     0,     0,    21,    22,
       0,    23,    24,     0,    26,    27,    28,     0,    29,     0,
      30,     0,     0,    31,     0,    32,     0,    33,     0,     0,
       0,     0,     0,     0,     0,    34,     0,    35,    36,    37,
      38,    39,     0,    40,    41,    42,     5,     0,     0,     7,
       0,     0,     0,     0,     0,     9,     0,     0,    11,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      13,     0,     0,    15,    16,     0,     0,     0,     0,    18,
       0,     0,     0,    19,    20,     0,     0,     0,     0,    21,
      22,     0,    23,    24,   221,    26,    27,    28,     0,    29,
       5,    30,     0,     7,    31,     0,    32,     0,    33,     9,
       0,     0,    11,     0,     0,     0,    34,     0,    35,    36,
      37,    38,     0,     0,    13,     0,    42,    15,    16,     0,
       0,     0,     0,    18,     0,     0,     0,    19,    20,     0,
       0,     0,     0,    21,    22,     0,    23,    24,   296,    26,
      27,    28,     0,    29,     0,    30,   439,     0,    31,     0,
      32,     0,    33,     0,    13,     0,     0,     0,     0,     0,
      34,     0,    35,    36,    37,    38,     0,    19,    20,     0,
      42,     0,    13,    21,    22,     0,    23,    24,     0,    26,
       0,    28,     0,    29,     0,    19,    20,     0,    31,     0,
       0,    21,    22,     0,    23,    24,     0,    26,     0,    28,
      34,    29,    35,    36,    37,    38,    31,     0,     0,     0,
       0,    13,     0,     0,     0,     0,     0,     0,    34,     0,
      35,    36,    37,    38,    19,    20,     0,     0,    42,    13,
      21,    22,     0,    23,    24,     0,    26,     0,    28,     0,
      29,     0,   433,    20,     0,    31,     0,     0,    21,    22,
       0,    23,    24,     0,    26,     0,    28,    34,    29,    35,
      36,    37,    38,    31,     0,     0,     0,    13,     0,     0,
       0,     0,     0,     0,     0,    34,     0,    35,    36,    37,
      38,    20,     0,     0,     0,    13,    21,    22,     0,    23,
      24,     0,    26,     0,    28,     0,    29,     0,     0,    20,
       0,    31,     0,     0,    21,    22,     0,    23,    24,     0,
      26,     0,     0,    34,    29,    35,    36,    37,    38,    31,
       0,     0,     0,    13,     0,     0,     0,     0,     0,     0,
       0,    34,     0,    35,    36,    37,    38,    20,     0,     0,
       0,     0,    21,    22,     0,    23,    24,     0,    26,     0,
       0,     0,    29,     0,     0,     0,     0,    31,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    35,    36,    37,    38
};

static const yytype_int16 yycheck[] =
{
       5,     3,    11,   136,    34,    14,   186,    21,   203,    86,
     205,    33,    17,    14,   320,    20,    21,    22,   198,     6,
      42,   111,   214,   316,   114,   318,    21,    32,    28,    22,
       3,    15,   187,    21,    24,    40,    41,    47,   287,    24,
      13,    24,    24,     7,   224,    15,    27,    51,    34,   446,
      23,    55,    25,     0,    40,    27,   453,    21,    56,    31,
      55,    71,    40,    51,    34,    55,    21,    51,    56,    24,
      55,    64,    55,    55,    78,    48,    62,    75,    55,    54,
      53,    62,   262,    76,    62,    78,    81,   164,   280,   244,
     339,    66,    65,    78,    67,    78,    51,    52,     6,    72,
       9,    55,   408,   108,    77,    14,    79,    15,    34,    31,
      19,    33,    85,   293,    40,   102,    30,    15,    16,   111,
      34,   313,   114,    26,    27,    29,    55,    55,    15,    15,
      55,     5,   425,    37,    38,    39,   442,    10,    42,   139,
      44,   150,   334,    12,   324,    49,    50,     4,   441,    80,
      16,    51,    42,    41,    15,    59,    60,    16,    69,   181,
      15,   341,    34,    73,    35,   345,   243,   181,    74,   191,
      15,     7,    16,    55,    59,    42,   368,   182,    30,    73,
      73,   376,    16,   363,    21,    41,    16,    55,    30,   369,
      55,   281,    16,    43,    73,    55,   226,   202,    73,    15,
     209,    55,     7,   208,   337,    16,   386,    55,   209,   389,
      73,   391,   407,    42,   219,    15,    15,    27,    15,    15,
      73,   311,    16,    74,   229,   247,   406,    15,    56,    55,
      15,    15,    73,   247,    55,    16,   416,    16,    15,     7,
     245,    16,    15,    33,    15,    15,    73,   427,   428,    16,
     255,    15,    55,    16,   263,    27,   261,    15,    15,    15,
      62,    16,    16,    15,    15,    15,    15,    15,    32,    45,
     433,    45,   228,   247,   279,   373,   199,   410,   283,   294,
     310,    45,    46,   288,   290,   287,   265,    51,    52,   294,
      54,    55,   156,    57,   299,    59,   121,    61,   137,    22,
     392,   159,    66,   152,   309,   310,   153,   353,   151,    45,
     423,   434,    -1,   446,    78,    -1,    80,    81,    82,    83,
     453,    -1,    -1,    -1,    24,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    32,    -1,    -1,    -1,    -1,   339,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    45,    46,    -1,   353,    -1,
      -1,    51,    52,   358,    54,    55,    -1,    57,    -1,    59,
     365,    61,    -1,    -1,    -1,    -1,    66,    -1,    -1,   374,
      -1,    -1,    -1,   378,    -1,    -1,    -1,    -1,    78,    -1,
      80,    81,    82,    83,    -1,    -1,    -1,   392,    -1,    -1,
      -1,    -1,    -1,     8,     9,    -1,    11,    -1,    -1,    14,
      -1,    -1,    17,    -1,    19,    20,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    28,    -1,   420,    -1,    32,   423,    34,
      35,    36,    -1,    -1,    -1,    40,    41,   432,    -1,    -1,
      45,    46,    -1,    -1,   439,    -1,    51,    52,    -1,    54,
      55,    56,    57,    58,    59,    -1,    61,    -1,    63,    -1,
      -1,    66,    -1,    68,    -1,    70,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    78,    -1,    80,    81,    82,    83,    84,
      -1,    86,    87,    88,     8,     9,    -1,    11,    -1,    -1,
      14,    -1,    -1,    17,    18,    19,    20,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    32,    -1,
      34,    35,    36,    -1,    -1,    -1,    40,    41,    -1,    -1,
      -1,    45,    46,    -1,    -1,    -1,    -1,    51,    52,    -1,
      54,    55,    -1,    57,    58,    59,    -1,    61,    -1,    63,
      -1,    -1,    66,    -1,    68,    -1,    70,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    78,    -1,    80,    81,    82,    83,
      84,    -1,    86,    87,    88,     8,     9,    -1,    11,    -1,
      -1,    14,    -1,    -1,    17,    -1,    19,    20,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    32,
      -1,    34,    35,    36,    -1,    -1,    -1,    40,    41,    -1,
      -1,    -1,    45,    46,    -1,    -1,    -1,    -1,    51,    52,
      -1,    54,    55,    -1,    57,    58,    59,    -1,    61,    -1,
      63,    -1,    -1,    66,    -1,    68,    -1,    70,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    78,    -1,    80,    81,    82,
      83,    84,    -1,    86,    87,    88,     8,    -1,    -1,    11,
      -1,    -1,    -1,    -1,    -1,    17,    -1,    -1,    20,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      32,    -1,    -1,    35,    36,    -1,    -1,    -1,    -1,    41,
      -1,    -1,    -1,    45,    46,    -1,    -1,    -1,    -1,    51,
      52,    -1,    54,    55,    56,    57,    58,    59,    -1,    61,
       8,    63,    -1,    11,    66,    -1,    68,    -1,    70,    17,
      -1,    -1,    20,    -1,    -1,    -1,    78,    -1,    80,    81,
      82,    83,    -1,    -1,    32,    -1,    88,    35,    36,    -1,
      -1,    -1,    -1,    41,    -1,    -1,    -1,    45,    46,    -1,
      -1,    -1,    -1,    51,    52,    -1,    54,    55,    56,    57,
      58,    59,    -1,    61,    -1,    63,    24,    -1,    66,    -1,
      68,    -1,    70,    -1,    32,    -1,    -1,    -1,    -1,    -1,
      78,    -1,    80,    81,    82,    83,    -1,    45,    46,    -1,
      88,    -1,    32,    51,    52,    -1,    54,    55,    -1,    57,
      -1,    59,    -1,    61,    -1,    45,    46,    -1,    66,    -1,
      -1,    51,    52,    -1,    54,    55,    -1,    57,    -1,    59,
      78,    61,    80,    81,    82,    83,    66,    -1,    -1,    -1,
      -1,    32,    -1,    -1,    -1,    -1,    -1,    -1,    78,    -1,
      80,    81,    82,    83,    45,    46,    -1,    -1,    88,    32,
      51,    52,    -1,    54,    55,    -1,    57,    -1,    59,    -1,
      61,    -1,    45,    46,    -1,    66,    -1,    -1,    51,    52,
      -1,    54,    55,    -1,    57,    -1,    59,    78,    61,    80,
      81,    82,    83,    66,    -1,    -1,    -1,    32,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    78,    -1,    80,    81,    82,
      83,    46,    -1,    -1,    -1,    32,    51,    52,    -1,    54,
      55,    -1,    57,    -1,    59,    -1,    61,    -1,    -1,    46,
      -1,    66,    -1,    -1,    51,    52,    -1,    54,    55,    -1,
      57,    -1,    -1,    78,    61,    80,    81,    82,    83,    66,
      -1,    -1,    -1,    32,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    78,    -1,    80,    81,    82,    83,    46,    -1,    -1,
      -1,    -1,    51,    52,    -1,    54,    55,    -1,    57,    -1,
      -1,    -1,    61,    -1,    -1,    -1,    -1,    66,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    80,    81,    82,    83
};

  /* YYSTOS[STATE-NUM] -- The (internal number of the) accessing
     symbol of state STATE-NUM.  */
static const yytype_uint8 yystos[] =
{
       0,    90,    91,    93,     0,     8,     9,    11,    14,    17,
      19,    20,    28,    32,    34,    35,    36,    40,    41,    45,
      46,    51,    52,    54,    55,    56,    57,    58,    59,    61,
      63,    66,    68,    70,    78,    80,    81,    82,    83,    84,
      86,    87,    88,    92,    94,    96,    97,    98,   114,   115,
     117,   118,   122,   123,   124,   125,   126,   127,   128,   129,
     131,   132,   133,   143,   145,   146,   147,   148,   150,   151,
     152,   156,   163,   166,   168,   169,   170,   171,   173,   174,
     175,   176,   177,   179,   181,   183,   184,   185,   187,   192,
     204,   209,   220,   163,    55,   142,    55,    55,   173,   202,
     202,   135,   223,    55,   163,   138,   141,   142,    15,   108,
     222,   163,   191,   205,   163,   188,   189,   193,   220,   190,
     193,    55,   170,   163,   204,   174,    15,   163,   158,   163,
     204,    94,    98,   209,   116,   194,    40,    62,   164,     5,
      29,    37,    38,    39,    42,    44,    49,    50,    59,    60,
     172,    10,    12,     4,    47,    71,   178,    54,    66,   180,
      22,    64,    76,    78,   182,   183,   186,    80,     3,    13,
      23,    25,    48,    53,    65,    67,    72,    77,    79,    85,
     120,   121,    16,    21,    51,    56,    15,    51,    51,    99,
     203,    42,    41,    21,    81,   134,   142,   144,    15,    16,
       7,   163,    15,    24,    55,    78,   112,   113,    15,    34,
     194,   208,   218,    69,   194,   218,    73,    74,   144,    35,
     130,    56,   115,   161,    15,   157,     7,    56,    75,    16,
     168,   169,   170,    59,    42,   173,   175,   176,   177,   179,
     181,   183,    21,    24,    51,    52,   195,    30,   119,   204,
     220,   163,    55,    95,   210,   211,   161,    95,    73,   100,
     221,     6,    15,    16,   204,    51,    55,    78,   136,   137,
     139,    16,   161,   138,    55,   163,   113,   109,   113,    30,
     101,   163,   202,    16,   106,   106,   163,    43,    31,    33,
     153,   159,   161,    15,    16,   174,    56,   117,   163,    27,
      55,   183,    95,   163,   196,   198,   199,   119,    73,    24,
      78,   163,   214,   215,    73,    73,    24,    55,    78,   105,
     107,   163,   161,   173,    15,   139,     7,   140,    55,   149,
     110,   163,    16,   106,   206,   207,   218,    42,   114,   162,
     163,    15,    27,   154,   159,    15,    27,   161,   158,   163,
      73,    74,   197,    15,    56,   163,   163,   174,    30,   216,
     218,    16,   106,    15,   107,    15,   102,   107,   101,    15,
     161,    73,    55,    16,    26,    27,    16,   111,    16,   106,
     168,    18,   114,     7,   160,   161,    15,    33,   155,    15,
     161,    15,    16,   163,   199,   212,   163,   161,   163,   103,
      16,   106,   161,    27,   137,   163,    15,    24,   113,   163,
      40,   217,   218,   219,    55,   161,    15,   161,   161,   198,
      15,   200,   201,    16,   213,    16,   104,    15,    15,   161,
     113,   101,    15,    45,   165,   167,   168,   161,   163,    24,
     215,    24,   107,   161,   161,   163,    15,   108,   217,   163,
     107,   101,   165,    15,   165
};

  /* YYR1[YYN] -- Symbol number of symbol that rule YYN derives.  */
static const yytype_uint8 yyr1[] =
{
       0,    89,    90,    91,    92,    92,    93,    93,    94,    94,
      95,    95,    96,    96,    97,    97,    98,    98,    99,    99,
     100,   100,   101,   101,   102,   102,   103,   103,   104,   104,
     105,   105,   106,   106,   107,   107,   108,   108,   109,   109,
     110,   110,   111,   111,   112,   112,   113,   114,   114,   115,
     115,   116,   116,   117,   117,   117,   117,   117,   117,   117,
     117,   118,   118,   119,   119,   120,   120,   121,   121,   121,
     121,   121,   121,   121,   121,   121,   121,   121,   121,   122,
     123,   124,   124,   124,   124,   124,   125,   126,   127,   127,
     128,   129,   129,   130,   130,   131,   131,   132,   133,   134,
     134,   135,   135,   136,   136,   136,   137,   137,   138,   138,
     139,   139,   140,   140,   141,   141,   142,   142,   143,   144,
     144,   145,   146,   146,   147,   147,   147,   147,   147,   147,
     147,   147,   148,   148,   149,   149,   150,   150,   151,   151,
     152,   152,   153,   153,   154,   154,   155,   155,   156,   157,
     157,   158,   158,   159,   159,   160,   160,   161,   161,   162,
     162,   163,   163,   164,   164,   165,   165,   166,   166,   167,
     167,   168,   168,   169,   169,   170,   170,   171,   171,   172,
     172,   172,   172,   172,   172,   172,   172,   172,   172,   172,
     173,   173,   174,   174,   175,   175,   176,   176,   177,   177,
     178,   178,   179,   179,   180,   180,   181,   181,   182,   182,
     182,   182,   183,   183,   184,   184,   184,   185,   185,   186,
     186,   187,   187,   187,   187,   187,   187,   187,   187,   187,
     187,   188,   188,   189,   189,   190,   190,   191,   191,   192,
     192,   193,   193,   194,   194,   195,   195,   195,   196,   196,
     197,   197,   198,   198,   199,   199,   200,   200,   201,   201,
     202,   202,   203,   203,   204,   204,   205,   205,   206,   206,
     207,   207,   208,   208,   209,   209,   210,   211,   211,   212,
     212,   213,   213,   214,   214,   214,   215,   215,   216,   216,
     217,   217,   218,   218,   219,   219,   220,   220,   221,   221,
     222,   222,   223,   223
};

  /* YYR2[YYN] -- Number of symbols on the right hand side of rule YYN.  */
static const yytype_uint8 yyr2[] =
{
       0,     2,     1,     2,     1,     1,     2,     0,     6,     3,
       1,     0,     2,     1,     2,     2,     7,     5,     3,     2,
       2,     4,     2,     0,     1,     0,     4,     0,     3,     0,
       4,     2,     1,     0,     3,     1,     2,     4,     1,     0,
       4,     0,     3,     0,     4,     2,     1,     1,     1,     4,
       3,     3,     0,     1,     1,     1,     1,     1,     1,     1,
       1,     3,     2,     1,     1,     3,     0,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     2,
       1,     1,     1,     1,     1,     1,     1,     1,     2,     1,
       1,     3,     1,     2,     0,     1,     1,     2,     4,     1,
       1,     2,     2,     1,     3,     1,     3,     1,     3,     1,
       3,     2,     3,     0,     1,     3,     1,     3,     3,     3,
       0,     3,     4,     2,     1,     1,     1,     1,     1,     1,
       1,     1,     8,     5,     5,     0,     7,     4,     9,     6,
       6,     6,     4,     3,     3,     0,     3,     0,     5,     3,
       0,     3,     1,     3,     1,     2,     0,     1,     4,     2,
       1,     2,     1,     4,     0,     1,     1,     4,     3,     4,
       3,     1,     3,     1,     3,     2,     1,     1,     3,     1,
       1,     1,     1,     1,     1,     1,     1,     2,     1,     2,
       2,     1,     1,     3,     1,     3,     1,     3,     1,     3,
       1,     1,     1,     3,     1,     1,     1,     3,     1,     1,
       1,     1,     2,     1,     1,     1,     1,     4,     2,     2,
       0,     3,     3,     3,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     0,     1,     0,     1,     0,     2,
       1,     2,     3,     3,     0,     3,     3,     2,     3,     2,
       3,     0,     1,     4,     1,     0,     1,     0,     2,     1,
       3,     2,     3,     0,     3,     2,     4,     2,     5,     0,
       1,     2,     1,     2,     7,     4,     2,     3,     0,     3,
       0,     3,     0,     2,     4,     2,     2,     3,     1,     0,
       1,     1,     5,     4,     3,     2,     2,     1,     4,     0,
       4,     0,     2,     0
};


#define yyerrok         (yyerrstatus = 0)
#define yyclearin       (yychar = YYEMPTY)
#define YYEMPTY         (-2)
#define YYEOF           0

#define YYACCEPT        goto yyacceptlab
#define YYABORT         goto yyabortlab
#define YYERROR         goto yyerrorlab


#define YYRECOVERING()  (!!yyerrstatus)

#define YYBACKUP(Token, Value)                                  \
do                                                              \
  if (yychar == YYEMPTY)                                        \
    {                                                           \
      yychar = (Token);                                         \
      yylval = (Value);                                         \
      YYPOPSTACK (yylen);                                       \
      yystate = *yyssp;                                         \
      goto yybackup;                                            \
    }                                                           \
  else                                                          \
    {                                                           \
      yyerror (YY_("syntax error: cannot back up")); \
      YYERROR;                                                  \
    }                                                           \
while (0)

/* Error token number */
#define YYTERROR        1
#define YYERRCODE       256


/* YYLLOC_DEFAULT -- Set CURRENT to span from RHS[1] to RHS[N].
   If N is 0, then set CURRENT to the empty location which ends
   the previous symbol: RHS[0] (always defined).  */

#ifndef YYLLOC_DEFAULT
# define YYLLOC_DEFAULT(Current, Rhs, N)                                \
    do                                                                  \
      if (N)                                                            \
        {                                                               \
          (Current).first_line   = YYRHSLOC (Rhs, 1).first_line;        \
          (Current).first_column = YYRHSLOC (Rhs, 1).first_column;      \
          (Current).last_line    = YYRHSLOC (Rhs, N).last_line;         \
          (Current).last_column  = YYRHSLOC (Rhs, N).last_column;       \
        }                                                               \
      else                                                              \
        {                                                               \
          (Current).first_line   = (Current).last_line   =              \
            YYRHSLOC (Rhs, 0).last_line;                                \
          (Current).first_column = (Current).last_column =              \
            YYRHSLOC (Rhs, 0).last_column;                              \
        }                                                               \
    while (0)
#endif

#define YYRHSLOC(Rhs, K) ((Rhs)[K])


/* Enable debugging if requested.  */
#if YYDEBUG

# ifndef YYFPRINTF
#  include <stdio.h> /* INFRINGES ON USER NAME SPACE */
#  define YYFPRINTF fprintf
# endif

# define YYDPRINTF(Args)                        \
do {                                            \
  if (yydebug)                                  \
    YYFPRINTF Args;                             \
} while (0)


/* YY_LOCATION_PRINT -- Print the location on the stream.
   This macro was not mandated originally: define only if we know
   we won't break user code: when these are the locations we know.  */

#ifndef YY_LOCATION_PRINT
# if defined YYLTYPE_IS_TRIVIAL && YYLTYPE_IS_TRIVIAL

/* Print *YYLOCP on YYO.  Private, do not rely on its existence. */

YY_ATTRIBUTE_UNUSED
static unsigned
yy_location_print_ (FILE *yyo, YYLTYPE const * const yylocp)
{
  unsigned res = 0;
  int end_col = 0 != yylocp->last_column ? yylocp->last_column - 1 : 0;
  if (0 <= yylocp->first_line)
    {
      res += YYFPRINTF (yyo, "%d", yylocp->first_line);
      if (0 <= yylocp->first_column)
        res += YYFPRINTF (yyo, ".%d", yylocp->first_column);
    }
  if (0 <= yylocp->last_line)
    {
      if (yylocp->first_line < yylocp->last_line)
        {
          res += YYFPRINTF (yyo, "-%d", yylocp->last_line);
          if (0 <= end_col)
            res += YYFPRINTF (yyo, ".%d", end_col);
        }
      else if (0 <= end_col && yylocp->first_column < end_col)
        res += YYFPRINTF (yyo, "-%d", end_col);
    }
  return res;
 }

#  define YY_LOCATION_PRINT(File, Loc)          \
  yy_location_print_ (File, &(Loc))

# else
#  define YY_LOCATION_PRINT(File, Loc) ((void) 0)
# endif
#endif


# define YY_SYMBOL_PRINT(Title, Type, Value, Location)                    \
do {                                                                      \
  if (yydebug)                                                            \
    {                                                                     \
      YYFPRINTF (stderr, "%s ", Title);                                   \
      yy_symbol_print (stderr,                                            \
                  Type, Value, Location); \
      YYFPRINTF (stderr, "\n");                                           \
    }                                                                     \
} while (0)


/*----------------------------------------.
| Print this symbol's value on YYOUTPUT.  |
`----------------------------------------*/

static void
yy_symbol_value_print (FILE *yyoutput, int yytype, YYSTYPE const * const yyvaluep, YYLTYPE const * const yylocationp)
{
  FILE *yyo = yyoutput;
  YYUSE (yyo);
  YYUSE (yylocationp);
  if (!yyvaluep)
    return;
# ifdef YYPRINT
  if (yytype < YYNTOKENS)
    YYPRINT (yyoutput, yytoknum[yytype], *yyvaluep);
# endif
  YYUSE (yytype);
}


/*--------------------------------.
| Print this symbol on YYOUTPUT.  |
`--------------------------------*/

static void
yy_symbol_print (FILE *yyoutput, int yytype, YYSTYPE const * const yyvaluep, YYLTYPE const * const yylocationp)
{
  YYFPRINTF (yyoutput, "%s %s (",
             yytype < YYNTOKENS ? "token" : "nterm", yytname[yytype]);

  YY_LOCATION_PRINT (yyoutput, *yylocationp);
  YYFPRINTF (yyoutput, ": ");
  yy_symbol_value_print (yyoutput, yytype, yyvaluep, yylocationp);
  YYFPRINTF (yyoutput, ")");
}

/*------------------------------------------------------------------.
| yy_stack_print -- Print the state stack from its BOTTOM up to its |
| TOP (included).                                                   |
`------------------------------------------------------------------*/

static void
yy_stack_print (yytype_int16 *yybottom, yytype_int16 *yytop)
{
  YYFPRINTF (stderr, "Stack now");
  for (; yybottom <= yytop; yybottom++)
    {
      int yybot = *yybottom;
      YYFPRINTF (stderr, " %d", yybot);
    }
  YYFPRINTF (stderr, "\n");
}

# define YY_STACK_PRINT(Bottom, Top)                            \
do {                                                            \
  if (yydebug)                                                  \
    yy_stack_print ((Bottom), (Top));                           \
} while (0)


/*------------------------------------------------.
| Report that the YYRULE is going to be reduced.  |
`------------------------------------------------*/

static void
yy_reduce_print (yytype_int16 *yyssp, YYSTYPE *yyvsp, YYLTYPE *yylsp, int yyrule)
{
  unsigned long int yylno = yyrline[yyrule];
  int yynrhs = yyr2[yyrule];
  int yyi;
  YYFPRINTF (stderr, "Reducing stack by rule %d (line %lu):\n",
             yyrule - 1, yylno);
  /* The symbols being reduced.  */
  for (yyi = 0; yyi < yynrhs; yyi++)
    {
      YYFPRINTF (stderr, "   $%d = ", yyi + 1);
      yy_symbol_print (stderr,
                       yystos[yyssp[yyi + 1 - yynrhs]],
                       &(yyvsp[(yyi + 1) - (yynrhs)])
                       , &(yylsp[(yyi + 1) - (yynrhs)])                       );
      YYFPRINTF (stderr, "\n");
    }
}

# define YY_REDUCE_PRINT(Rule)          \
do {                                    \
  if (yydebug)                          \
    yy_reduce_print (yyssp, yyvsp, yylsp, Rule); \
} while (0)

/* Nonzero means print parse trace.  It is left uninitialized so that
   multiple parsers can coexist.  */
int yydebug;
#else /* !YYDEBUG */
# define YYDPRINTF(Args)
# define YY_SYMBOL_PRINT(Title, Type, Value, Location)
# define YY_STACK_PRINT(Bottom, Top)
# define YY_REDUCE_PRINT(Rule)
#endif /* !YYDEBUG */


/* YYINITDEPTH -- initial size of the parser's stacks.  */
#ifndef YYINITDEPTH
# define YYINITDEPTH 200
#endif

/* YYMAXDEPTH -- maximum size the stacks can grow to (effective only
   if the built-in stack extension method is used).

   Do not make this value too large; the results are undefined if
   YYSTACK_ALLOC_MAXIMUM < YYSTACK_BYTES (YYMAXDEPTH)
   evaluated with infinite-precision integer arithmetic.  */

#ifndef YYMAXDEPTH
# define YYMAXDEPTH 10000
#endif


#if YYERROR_VERBOSE

# ifndef yystrlen
#  if defined __GLIBC__ && defined _STRING_H
#   define yystrlen strlen
#  else
/* Return the length of YYSTR.  */
static YYSIZE_T
yystrlen (const char *yystr)
{
  YYSIZE_T yylen;
  for (yylen = 0; yystr[yylen]; yylen++)
    continue;
  return yylen;
}
#  endif
# endif

# ifndef yystpcpy
#  if defined __GLIBC__ && defined _STRING_H && defined _GNU_SOURCE
#   define yystpcpy stpcpy
#  else
/* Copy YYSRC to YYDEST, returning the address of the terminating '\0' in
   YYDEST.  */
static char *
yystpcpy (char *yydest, const char *yysrc)
{
  char *yyd = yydest;
  const char *yys = yysrc;

  while ((*yyd++ = *yys++) != '\0')
    continue;

  return yyd - 1;
}
#  endif
# endif

# ifndef yytnamerr
/* Copy to YYRES the contents of YYSTR after stripping away unnecessary
   quotes and backslashes, so that it's suitable for yyerror.  The
   heuristic is that double-quoting is unnecessary unless the string
   contains an apostrophe, a comma, or backslash (other than
   backslash-backslash).  YYSTR is taken from yytname.  If YYRES is
   null, do not copy; instead, return the length of what the result
   would have been.  */
static YYSIZE_T
yytnamerr (char *yyres, const char *yystr)
{
  if (*yystr == '"')
    {
      YYSIZE_T yyn = 0;
      char const *yyp = yystr;

      for (;;)
        switch (*++yyp)
          {
          case '\'':
          case ',':
            goto do_not_strip_quotes;

          case '\\':
            if (*++yyp != '\\')
              goto do_not_strip_quotes;
            /* Fall through.  */
          default:
            if (yyres)
              yyres[yyn] = *yyp;
            yyn++;
            break;

          case '"':
            if (yyres)
              yyres[yyn] = '\0';
            return yyn;
          }
    do_not_strip_quotes: ;
    }

  if (! yyres)
    return yystrlen (yystr);

  return yystpcpy (yyres, yystr) - yyres;
}
# endif

/* Copy into *YYMSG, which is of size *YYMSG_ALLOC, an error message
   about the unexpected token YYTOKEN for the state stack whose top is
   YYSSP.

   Return 0 if *YYMSG was successfully written.  Return 1 if *YYMSG is
   not large enough to hold the message.  In that case, also set
   *YYMSG_ALLOC to the required number of bytes.  Return 2 if the
   required number of bytes is too large to store.  */
static int
yysyntax_error (YYSIZE_T *yymsg_alloc, char **yymsg,
                yytype_int16 *yyssp, int yytoken)
{
  YYSIZE_T yysize0 = yytnamerr (YY_NULLPTR, yytname[yytoken]);
  YYSIZE_T yysize = yysize0;
  enum { YYERROR_VERBOSE_ARGS_MAXIMUM = 5 };
  /* Internationalized format string. */
  const char *yyformat = YY_NULLPTR;
  /* Arguments of yyformat. */
  char const *yyarg[YYERROR_VERBOSE_ARGS_MAXIMUM];
  /* Number of reported tokens (one for the "unexpected", one per
     "expected"). */
  int yycount = 0;

  /* There are many possibilities here to consider:
     - If this state is a consistent state with a default action, then
       the only way this function was invoked is if the default action
       is an error action.  In that case, don't check for expected
       tokens because there are none.
     - The only way there can be no lookahead present (in yychar) is if
       this state is a consistent state with a default action.  Thus,
       detecting the absence of a lookahead is sufficient to determine
       that there is no unexpected or expected token to report.  In that
       case, just report a simple "syntax error".
     - Don't assume there isn't a lookahead just because this state is a
       consistent state with a default action.  There might have been a
       previous inconsistent state, consistent state with a non-default
       action, or user semantic action that manipulated yychar.
     - Of course, the expected token list depends on states to have
       correct lookahead information, and it depends on the parser not
       to perform extra reductions after fetching a lookahead from the
       scanner and before detecting a syntax error.  Thus, state merging
       (from LALR or IELR) and default reductions corrupt the expected
       token list.  However, the list is correct for canonical LR with
       one exception: it will still contain any token that will not be
       accepted due to an error action in a later state.
  */
  if (yytoken != YYEMPTY)
    {
      int yyn = yypact[*yyssp];
      yyarg[yycount++] = yytname[yytoken];
      if (!yypact_value_is_default (yyn))
        {
          /* Start YYX at -YYN if negative to avoid negative indexes in
             YYCHECK.  In other words, skip the first -YYN actions for
             this state because they are default actions.  */
          int yyxbegin = yyn < 0 ? -yyn : 0;
          /* Stay within bounds of both yycheck and yytname.  */
          int yychecklim = YYLAST - yyn + 1;
          int yyxend = yychecklim < YYNTOKENS ? yychecklim : YYNTOKENS;
          int yyx;

          for (yyx = yyxbegin; yyx < yyxend; ++yyx)
            if (yycheck[yyx + yyn] == yyx && yyx != YYTERROR
                && !yytable_value_is_error (yytable[yyx + yyn]))
              {
                if (yycount == YYERROR_VERBOSE_ARGS_MAXIMUM)
                  {
                    yycount = 1;
                    yysize = yysize0;
                    break;
                  }
                yyarg[yycount++] = yytname[yyx];
                {
                  YYSIZE_T yysize1 = yysize + yytnamerr (YY_NULLPTR, yytname[yyx]);
                  if (! (yysize <= yysize1
                         && yysize1 <= YYSTACK_ALLOC_MAXIMUM))
                    return 2;
                  yysize = yysize1;
                }
              }
        }
    }

  switch (yycount)
    {
# define YYCASE_(N, S)                      \
      case N:                               \
        yyformat = S;                       \
      break
      YYCASE_(0, YY_("syntax error"));
      YYCASE_(1, YY_("syntax error, unexpected %s"));
      YYCASE_(2, YY_("syntax error, unexpected %s, expecting %s"));
      YYCASE_(3, YY_("syntax error, unexpected %s, expecting %s or %s"));
      YYCASE_(4, YY_("syntax error, unexpected %s, expecting %s or %s or %s"));
      YYCASE_(5, YY_("syntax error, unexpected %s, expecting %s or %s or %s or %s"));
# undef YYCASE_
    }

  {
    YYSIZE_T yysize1 = yysize + yystrlen (yyformat);
    if (! (yysize <= yysize1 && yysize1 <= YYSTACK_ALLOC_MAXIMUM))
      return 2;
    yysize = yysize1;
  }

  if (*yymsg_alloc < yysize)
    {
      *yymsg_alloc = 2 * yysize;
      if (! (yysize <= *yymsg_alloc
             && *yymsg_alloc <= YYSTACK_ALLOC_MAXIMUM))
        *yymsg_alloc = YYSTACK_ALLOC_MAXIMUM;
      return 1;
    }

  /* Avoid sprintf, as that infringes on the user's name space.
     Don't have undefined behavior even if the translation
     produced a string with the wrong number of "%s"s.  */
  {
    char *yyp = *yymsg;
    int yyi = 0;
    while ((*yyp = *yyformat) != '\0')
      if (*yyp == '%' && yyformat[1] == 's' && yyi < yycount)
        {
          yyp += yytnamerr (yyp, yyarg[yyi++]);
          yyformat += 2;
        }
      else
        {
          yyp++;
          yyformat++;
        }
  }
  return 0;
}
#endif /* YYERROR_VERBOSE */

/*-----------------------------------------------.
| Release the memory associated to this symbol.  |
`-----------------------------------------------*/

static void
yydestruct (const char *yymsg, int yytype, YYSTYPE *yyvaluep, YYLTYPE *yylocationp)
{
  YYUSE (yyvaluep);
  YYUSE (yylocationp);
  if (!yymsg)
    yymsg = "Deleting";
  YY_SYMBOL_PRINT (yymsg, yytype, yyvaluep, yylocationp);

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  YYUSE (yytype);
  YY_IGNORE_MAYBE_UNINITIALIZED_END
}




/* The lookahead symbol.  */
int yychar;

/* The semantic value of the lookahead symbol.  */
YYSTYPE yylval;
/* Location data for the lookahead symbol.  */
YYLTYPE yylloc
# if defined YYLTYPE_IS_TRIVIAL && YYLTYPE_IS_TRIVIAL
  = { 1, 1, 1, 1 }
# endif
;
/* Number of syntax errors so far.  */
int yynerrs;


/*----------.
| yyparse.  |
`----------*/

int
yyparse (void)
{
    int yystate;
    /* Number of tokens to shift before error messages enabled.  */
    int yyerrstatus;

    /* The stacks and their tools:
       'yyss': related to states.
       'yyvs': related to semantic values.
       'yyls': related to locations.

       Refer to the stacks through separate pointers, to allow yyoverflow
       to reallocate them elsewhere.  */

    /* The state stack.  */
    yytype_int16 yyssa[YYINITDEPTH];
    yytype_int16 *yyss;
    yytype_int16 *yyssp;

    /* The semantic value stack.  */
    YYSTYPE yyvsa[YYINITDEPTH];
    YYSTYPE *yyvs;
    YYSTYPE *yyvsp;

    /* The location stack.  */
    YYLTYPE yylsa[YYINITDEPTH];
    YYLTYPE *yyls;
    YYLTYPE *yylsp;

    /* The locations where the error started and ended.  */
    YYLTYPE yyerror_range[3];

    YYSIZE_T yystacksize;

  int yyn;
  int yyresult;
  /* Lookahead token as an internal (translated) token number.  */
  int yytoken = 0;
  /* The variables used to return semantic value and location from the
     action routines.  */
  YYSTYPE yyval;
  YYLTYPE yyloc;

#if YYERROR_VERBOSE
  /* Buffer for error messages, and its allocated size.  */
  char yymsgbuf[128];
  char *yymsg = yymsgbuf;
  YYSIZE_T yymsg_alloc = sizeof yymsgbuf;
#endif

#define YYPOPSTACK(N)   (yyvsp -= (N), yyssp -= (N), yylsp -= (N))

  /* The number of symbols on the RHS of the reduced rule.
     Keep to zero when no symbol should be popped.  */
  int yylen = 0;

  yyssp = yyss = yyssa;
  yyvsp = yyvs = yyvsa;
  yylsp = yyls = yylsa;
  yystacksize = YYINITDEPTH;

  YYDPRINTF ((stderr, "Starting parse\n"));

  yystate = 0;
  yyerrstatus = 0;
  yynerrs = 0;
  yychar = YYEMPTY; /* Cause a token to be read.  */
  yylsp[0] = yylloc;
  goto yysetstate;

/*------------------------------------------------------------.
| yynewstate -- Push a new state, which is found in yystate.  |
`------------------------------------------------------------*/
 yynewstate:
  /* In all cases, when you get here, the value and location stacks
     have just been pushed.  So pushing a state here evens the stacks.  */
  yyssp++;

 yysetstate:
  *yyssp = yystate;

  if (yyss + yystacksize - 1 <= yyssp)
    {
      /* Get the current used size of the three stacks, in elements.  */
      YYSIZE_T yysize = yyssp - yyss + 1;

#ifdef yyoverflow
      {
        /* Give user a chance to reallocate the stack.  Use copies of
           these so that the &'s don't force the real ones into
           memory.  */
        YYSTYPE *yyvs1 = yyvs;
        yytype_int16 *yyss1 = yyss;
        YYLTYPE *yyls1 = yyls;

        /* Each stack pointer address is followed by the size of the
           data in use in that stack, in bytes.  This used to be a
           conditional around just the two extra args, but that might
           be undefined if yyoverflow is a macro.  */
        yyoverflow (YY_("memory exhausted"),
                    &yyss1, yysize * sizeof (*yyssp),
                    &yyvs1, yysize * sizeof (*yyvsp),
                    &yyls1, yysize * sizeof (*yylsp),
                    &yystacksize);

        yyls = yyls1;
        yyss = yyss1;
        yyvs = yyvs1;
      }
#else /* no yyoverflow */
# ifndef YYSTACK_RELOCATE
      goto yyexhaustedlab;
# else
      /* Extend the stack our own way.  */
      if (YYMAXDEPTH <= yystacksize)
        goto yyexhaustedlab;
      yystacksize *= 2;
      if (YYMAXDEPTH < yystacksize)
        yystacksize = YYMAXDEPTH;

      {
        yytype_int16 *yyss1 = yyss;
        union yyalloc *yyptr =
          (union yyalloc *) YYSTACK_ALLOC (YYSTACK_BYTES (yystacksize));
        if (! yyptr)
          goto yyexhaustedlab;
        YYSTACK_RELOCATE (yyss_alloc, yyss);
        YYSTACK_RELOCATE (yyvs_alloc, yyvs);
        YYSTACK_RELOCATE (yyls_alloc, yyls);
#  undef YYSTACK_RELOCATE
        if (yyss1 != yyssa)
          YYSTACK_FREE (yyss1);
      }
# endif
#endif /* no yyoverflow */

      yyssp = yyss + yysize - 1;
      yyvsp = yyvs + yysize - 1;
      yylsp = yyls + yysize - 1;

      YYDPRINTF ((stderr, "Stack size increased to %lu\n",
                  (unsigned long int) yystacksize));

      if (yyss + yystacksize - 1 <= yyssp)
        YYABORT;
    }

  YYDPRINTF ((stderr, "Entering state %d\n", yystate));

  if (yystate == YYFINAL)
    YYACCEPT;

  goto yybackup;

/*-----------.
| yybackup.  |
`-----------*/
yybackup:

  /* Do appropriate processing given the current state.  Read a
     lookahead token if we need one and don't already have one.  */

  /* First try to decide what to do without reference to lookahead token.  */
  yyn = yypact[yystate];
  if (yypact_value_is_default (yyn))
    goto yydefault;

  /* Not known => get a lookahead token if don't already have one.  */

  /* YYCHAR is either YYEMPTY or YYEOF or a valid lookahead symbol.  */
  if (yychar == YYEMPTY)
    {
      YYDPRINTF ((stderr, "Reading a token: "));
      yychar = yylex ();
    }

  if (yychar <= YYEOF)
    {
      yychar = yytoken = YYEOF;
      YYDPRINTF ((stderr, "Now at end of input.\n"));
    }
  else
    {
      yytoken = YYTRANSLATE (yychar);
      YY_SYMBOL_PRINT ("Next token is", yytoken, &yylval, &yylloc);
    }

  /* If the proper action on seeing token YYTOKEN is to reduce or to
     detect an error, take that action.  */
  yyn += yytoken;
  if (yyn < 0 || YYLAST < yyn || yycheck[yyn] != yytoken)
    goto yydefault;
  yyn = yytable[yyn];
  if (yyn <= 0)
    {
      if (yytable_value_is_error (yyn))
        goto yyerrlab;
      yyn = -yyn;
      goto yyreduce;
    }

  /* Count tokens shifted since error; after three, turn off error
     status.  */
  if (yyerrstatus)
    yyerrstatus--;

  /* Shift the lookahead token.  */
  YY_SYMBOL_PRINT ("Shifting", yytoken, &yylval, &yylloc);

  /* Discard the shifted token.  */
  yychar = YYEMPTY;

  yystate = yyn;
  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++yyvsp = yylval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END
  *++yylsp = yylloc;
  goto yynewstate;


/*-----------------------------------------------------------.
| yydefault -- do the default action for the current state.  |
`-----------------------------------------------------------*/
yydefault:
  yyn = yydefact[yystate];
  if (yyn == 0)
    goto yyerrlab;
  goto yyreduce;


/*-----------------------------.
| yyreduce -- Do a reduction.  |
`-----------------------------*/
yyreduce:
  /* yyn is the number of a rule to reduce with.  */
  yylen = yyr2[yyn];

  /* If YYLEN is nonzero, implement the default value of the action:
     '$$ = $1'.

     Otherwise, the following line sets YYVAL to garbage.
     This behavior is undocumented and Bison
     users should not rely upon it.  Assigning to YYVAL
     unconditionally makes the parser a bit smaller, and it avoids a
     GCC warning that YYVAL may be used uninitialized.  */
  yyval = yyvsp[1-yylen];

  /* Default location.  */
  YYLLOC_DEFAULT (yyloc, (yylsp - yylen), yylen);
  YY_REDUCE_PRINT (yyn);
  switch (yyn)
    {
      
#line 1891 "parse.tab.c" /* yacc.c:1646  */
      default: break;
    }
  /* User semantic actions sometimes alter yychar, and that requires
     that yytoken be updated with the new translation.  We take the
     approach of translating immediately before every use of yytoken.
     One alternative is translating here after every semantic action,
     but that translation would be missed if the semantic action invokes
     YYABORT, YYACCEPT, or YYERROR immediately after altering yychar or
     if it invokes YYBACKUP.  In the case of YYABORT or YYACCEPT, an
     incorrect destructor might then be invoked immediately.  In the
     case of YYERROR or YYBACKUP, subsequent parser actions might lead
     to an incorrect destructor call or verbose syntax error message
     before the lookahead is translated.  */
  YY_SYMBOL_PRINT ("-> $$ =", yyr1[yyn], &yyval, &yyloc);

  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);

  *++yyvsp = yyval;
  *++yylsp = yyloc;

  /* Now 'shift' the result of the reduction.  Determine what state
     that goes to, based on the state we popped back to and the rule
     number reduced by.  */

  yyn = yyr1[yyn];

  yystate = yypgoto[yyn - YYNTOKENS] + *yyssp;
  if (0 <= yystate && yystate <= YYLAST && yycheck[yystate] == *yyssp)
    yystate = yytable[yystate];
  else
    yystate = yydefgoto[yyn - YYNTOKENS];

  goto yynewstate;


/*--------------------------------------.
| yyerrlab -- here on detecting error.  |
`--------------------------------------*/
yyerrlab:
  /* Make sure we have latest lookahead translation.  See comments at
     user semantic actions for why this is necessary.  */
  yytoken = yychar == YYEMPTY ? YYEMPTY : YYTRANSLATE (yychar);

  /* If not already recovering from an error, report this error.  */
  if (!yyerrstatus)
    {
      ++yynerrs;
#if ! YYERROR_VERBOSE
      yyerror (YY_("syntax error"));
#else
# define YYSYNTAX_ERROR yysyntax_error (&yymsg_alloc, &yymsg, \
                                        yyssp, yytoken)
      {
        char const *yymsgp = YY_("syntax error");
        int yysyntax_error_status;
        yysyntax_error_status = YYSYNTAX_ERROR;
        if (yysyntax_error_status == 0)
          yymsgp = yymsg;
        else if (yysyntax_error_status == 1)
          {
            if (yymsg != yymsgbuf)
              YYSTACK_FREE (yymsg);
            yymsg = (char *) YYSTACK_ALLOC (yymsg_alloc);
            if (!yymsg)
              {
                yymsg = yymsgbuf;
                yymsg_alloc = sizeof yymsgbuf;
                yysyntax_error_status = 2;
              }
            else
              {
                yysyntax_error_status = YYSYNTAX_ERROR;
                yymsgp = yymsg;
              }
          }
        yyerror (yymsgp);
        if (yysyntax_error_status == 2)
          goto yyexhaustedlab;
      }
# undef YYSYNTAX_ERROR
#endif
    }

  yyerror_range[1] = yylloc;

  if (yyerrstatus == 3)
    {
      /* If just tried and failed to reuse lookahead token after an
         error, discard it.  */

      if (yychar <= YYEOF)
        {
          /* Return failure if at end of input.  */
          if (yychar == YYEOF)
            YYABORT;
        }
      else
        {
          yydestruct ("Error: discarding",
                      yytoken, &yylval, &yylloc);
          yychar = YYEMPTY;
        }
    }

  /* Else will try to reuse lookahead token after shifting the error
     token.  */
  goto yyerrlab1;


/*---------------------------------------------------.
| yyerrorlab -- error raised explicitly by YYERROR.  |
`---------------------------------------------------*/
yyerrorlab:

  /* Pacify compilers like GCC when the user code never invokes
     YYERROR and the label yyerrorlab therefore never appears in user
     code.  */
  if (/*CONSTCOND*/ 0)
     goto yyerrorlab;

  yyerror_range[1] = yylsp[1-yylen];
  /* Do not reclaim the symbols of the rule whose action triggered
     this YYERROR.  */
  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);
  yystate = *yyssp;
  goto yyerrlab1;


/*-------------------------------------------------------------.
| yyerrlab1 -- common code for both syntax error and YYERROR.  |
`-------------------------------------------------------------*/
yyerrlab1:
  yyerrstatus = 3;      /* Each real token shifted decrements this.  */

  for (;;)
    {
      yyn = yypact[yystate];
      if (!yypact_value_is_default (yyn))
        {
          yyn += YYTERROR;
          if (0 <= yyn && yyn <= YYLAST && yycheck[yyn] == YYTERROR)
            {
              yyn = yytable[yyn];
              if (0 < yyn)
                break;
            }
        }

      /* Pop the current state because it cannot handle the error token.  */
      if (yyssp == yyss)
        YYABORT;

      yyerror_range[1] = *yylsp;
      yydestruct ("Error: popping",
                  yystos[yystate], yyvsp, yylsp);
      YYPOPSTACK (1);
      yystate = *yyssp;
      YY_STACK_PRINT (yyss, yyssp);
    }

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++yyvsp = yylval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END

  yyerror_range[2] = yylloc;
  /* Using YYLLOC is tempting, but would change the location of
     the lookahead.  YYLOC is available though.  */
  YYLLOC_DEFAULT (yyloc, yyerror_range, 2);
  *++yylsp = yyloc;

  /* Shift the error token.  */
  YY_SYMBOL_PRINT ("Shifting", yystos[yyn], yyvsp, yylsp);

  yystate = yyn;
  goto yynewstate;


/*-------------------------------------.
| yyacceptlab -- YYACCEPT comes here.  |
`-------------------------------------*/
yyacceptlab:
  yyresult = 0;
  goto yyreturn;

/*-----------------------------------.
| yyabortlab -- YYABORT comes here.  |
`-----------------------------------*/
yyabortlab:
  yyresult = 1;
  goto yyreturn;

#if !defined yyoverflow || YYERROR_VERBOSE
/*-------------------------------------------------.
| yyexhaustedlab -- memory exhaustion comes here.  |
`-------------------------------------------------*/
yyexhaustedlab:
  yyerror (YY_("memory exhausted"));
  yyresult = 2;
  /* Fall through.  */
#endif

yyreturn:
  if (yychar != YYEMPTY)
    {
      /* Make sure we have latest lookahead translation.  See comments at
         user semantic actions for why this is necessary.  */
      yytoken = YYTRANSLATE (yychar);
      yydestruct ("Cleanup: discarding lookahead",
                  yytoken, &yylval, &yylloc);
    }
  /* Do not reclaim the symbols of the rule whose action triggered
     this YYABORT or YYACCEPT.  */
  YYPOPSTACK (yylen);
  YY_STACK_PRINT (yyss, yyssp);
  while (yyssp != yyss)
    {
      yydestruct ("Cleanup: popping",
                  yystos[*yyssp], yyvsp, yylsp);
      YYPOPSTACK (1);
    }
#ifndef yyoverflow
  if (yyss != yyssa)
    YYSTACK_FREE (yyss);
#endif
#if YYERROR_VERBOSE
  if (yymsg != yymsgbuf)
    YYSTACK_FREE (yymsg);
#endif
  return yyresult;
}
#line 598 "parse.y" /* yacc.c:1906  */


#include <stdio.h>
void yyerror (const char *s)
{
    if(yylloc.first_line > 0)	{
        fprintf (stderr, "%d.%d-%d.%d:", yylloc.first_line, yylloc.first_column,
	                                     yylloc.last_line,  yylloc.last_column);
    }
    fprintf(stderr, " %s with [%s]\n", s, yytext);
}


