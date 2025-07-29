import re

from CodeGenerator import CodeGenerator
from LL1Parser import LL1Parser
from LexicalAnalyzer import LexicalAnalyzer
from SemanticAnalyser import SemanticAnalyser

rules = [
    ('TOKEN_ONELINECOMMENT', r'\/\/[^\n]*'),            #online comment
    ('TOKEN_MULTILINECOMMENT', r'\/\*(.|\n)*?\*\/'),    #multi-line comment
    ('TOKEN_INT', r'int'),                              # int
    ('TOKEN_FLOAT', r'float'),                          # float
    ('TOKEN_STRINGTYPE', r'string'),                    # strintype
    ('TOKEN_ELSEIF', r'\b(else\s*if)\b'),               # else
    ('TOKEN_ELSE', r'else'),                            # else
    ('TOKEN_IF', r'if'),                                # if
    ('TOKEN_WHILE', r'while'),                          # while
    ('TOKEN_PRINT', r'Console\.Writeline'),             # print
    ('TOKEN_LBRACKET', r'\('),                          # (
    ('TOKEN_RBRACKET', r'\)'),                          # )
    ('TOKEN_LBRACE', r'\{'),                            # {
    ('TOKEN_RBRACE', r'\}'),                            # }
    ('TOKEN_COMMA', r','),                              # ,
    ('TOKEN_PCOMMA', r';'),                             # ;
    ('TOKEN_EQ', r'=='),                                # ==
    ('TOKEN_NE', r'!='),                                # !=
    ('TOKEN_LE', r'<='),                                # <=
    ('TOKEN_GE', r'>='),                                # >=
    ('TOKEN_OR', r'\|\|'),                              # ||
    ('TOKEN_AND', r'&&'),                               # &&
    ('TOKEN_ATTR', r'\='),                              # =
    ('TOKEN_LT', r'<'),                                 # <
    ('TOKEN_GT', r'>'),                                 # >
    ('TOKEN_PLUS', r'\+'),                              # +
    ('TOKEN_MINUS', r'-'),                              # -
    ('TOKEN_MULT', r'\*'),                              # *
    ('TOKEN_DIV', r'\/'),                               # /
    ('TOKEN_ID', r'[a-zA-Z]\w*'),                       # identifiers
    ('TOKEN_STRING', r"'[^']*'"),                       # strings
    ('TOKEN_NUMBER', r'\d+(\.\d+)?')                    # numbers
]


tokens = []
stripped_tokens = []

##TEST ONELINE COMMENT WITH ANOTHER CODE LINE - SUCCESS
#input_string = "//this is a online comment \n while (i < 5){Console.Writeline('HELLO WORLD');}"

##TEST ONELINE COMMENT - SUCCESS
#input_string = "//this is a online comment "

##TEST MULTILINE COMMENT WITHIN OTHER CODE - SUCCESS
#input_string = '''if (x > 5) {
#    /* This is a multi-line
#       comment */
#    Console.Writeline('Hello, World!');
#}'''

##TEST MULTILINE COMMENT ONLY - SUCCESS
#input_string = '''/* This is a multi-line \ncomment */'''

##TEST ASSIGNMENT STATEMENT - SUCCESS
#input_string = "myvariable = 3;"

##TEST FLOAT ASSIGNMENT STATEMENT - SUCCESS
#input_string = "float x = 2.55;"

##TEST INT ASSIGNMENT STATEMENT - SUCCESS
#input_string = "int x = 3;"

##TEST IF STATEMENT - SUCCESS
#input_string = "if (x > 5) { Console.Writeline(5); }"

##TEST IF STATEMENT - SUCCESS
#input_string = "if (x > 5) { Console.Writeline('hello world'); }"

##TEST IF & ELSE IF STATEMENT - SUCCESS
#input_string = "if (x > 5) { Console.Writeline('Hello, World!'); } else if(x>5){Console.Writeline('Hello, planet!'); }"

##TEST IF & ELSE STATEMENT - SUCCESS
#input_string = "if (x > 5) { Console.Writeline('Hello, World!'); } else {Console.Writeline('Hello, World!'); }"

#TEST WHILE LOOP - SUCCESS
input_string = "while (i < 5){Console.Writeline('Hello, World!');}"

##TEST PRINT ONLY - SUCCESS
#input_string = "Console.Writeline('Hello, World!');"

##TEST IF STATEMENT - SUCCESS
#input_string = "x = 3 + 2;"

##TEST WHILE LOOP WITH IF - FAILURE AT CODE GENERATION
#input_string = "while (i < 5){if (x > 5) { Console.Writeline('hello world'); }}"

result = LexicalAnalyzer.analyze_tokens(input_string,rules,tokens)
LexicalAnalyzer.strip_comment_tokens(tokens,stripped_tokens)

if tokens and not stripped_tokens:
    print('Only comment tokens have been identified. No code to generate')
else:
    LL1Parser.parser(stripped_tokens)
    SemanticAnalyser.type_checker(stripped_tokens)
    CodeGenerator.generate_code(stripped_tokens)
    print()
