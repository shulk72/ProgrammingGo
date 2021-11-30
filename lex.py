from sly import Lexer
import numpy as np


# import matplotlib.pyplot as plt


class LexAnalyzer(Lexer):
    tokens = {ID, PLUS, MINUS, TIMES, IF, EQUALS, DIV,
              LPAREN, RPAREN, NEWLINE, PLOT, MATHFUNC, POW, NUMBER, STRING, MOD,
              ASSIGN, TICK, SEMI, COMMA, PIPE, CROCANTE, AT, DEGSYM, THEN, WITH, CALC, EXIT,
              SEMI, VARS, INT, FROM, TO, NEWLINE, AS, DIV
              }

    # String containing ignored characters between tokens
    ignore = ' \t'

    # Regular expression rules for tokens
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    PLUS = r'\+'
    POW = r'\^'
    DIV = r'/'
    MINUS = r'-'
    TIMES = r'\*'
    LPAREN = r'\('
    RPAREN = r'\)'
    NUMBER = r'([0-9]*[.])?[0-9]+(e\-?[1-9][0-9]*)?'
    STRING = r'("[^\"]*")'
    MOD = r'%'
    ASSIGN = r'='
    NEWLINE = r'\n'
    TICK = r"'"
    SEMI = r';'
    COMMA = r','
    PIPE = r'\|'
    CROCANTE = r'\$'
    AT = r'@'
    DEGSYM = r'<'
    ID['from'] = FROM
    ID['to'] = TO
    ID['int'] = INT
    ID['exit'] = EXIT
    ID['equals'] = EQUALS
    ID['if'] = IF
    ID['sin'] = MATHFUNC
    ID['cos'] = MATHFUNC
    ID['tan'] = MATHFUNC
    ID['asin'] = MATHFUNC
    ID['acos'] = MATHFUNC
    ID['atan'] = MATHFUNC
    ID['sind'] = MATHFUNC
    ID['cosd'] = MATHFUNC
    ID['tand'] = MATHFUNC
    ID['asind'] = MATHFUNC
    ID['acosd'] = MATHFUNC
    ID['atand'] = MATHFUNC
    ID['rt'] = MATHFUNC
    ID['ln'] = MATHFUNC
    ID['angle'] = MATHFUNC
    ID['abs'] = MATHFUNC
    ID['plot'] = PLOT

    def t_error(t):
        print("Illegal character '%s'" % t.value[0])
        t.Lexer.skip(1)
