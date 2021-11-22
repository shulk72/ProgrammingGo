from sly import Parser
# from numpy import np
from termcolor import colored
from lex import LexAnalyzer
import math


class NParser(Parser):
    # debugfile = 'parser.out'

    tokens = LexAnalyzer.tokens

    # precedence = (
    #     ('right', CROCANTE),
    #     ('right', ASSIGN),
    #     ('left', INTEGRAL),
    #     ('left', THEN),
    #     ('left', WITH_EXPR),
    #     ('left', MONO_WITH_EXPR, COMMA),
    #     ('right', WITH_ASSIGNS),
    #     ('left', PLUS, MINUS),
    #     ('left', TIMES, DIV, MOD),
    #     ('right', CONSTANT),
    #     ('right', MATHFUNC, UMINUS),
    #     ('right', POW),
    #     ('nonassoc', NUMBER),
    #     ('nonassoc', AT, DEGSYM),
    # )

    # mathfuncs = {
    #     "sin": math.sin,
    #     "cos": math.cos,
    #     "tan": math.tan,
    #     "asin": math.asin,
    #     "acos": math.acos,
    #     "atan": math.atan,
    #     "sind": lambda x: math.sin(math.radians(x)),
    #     "cosd": lambda x: math.cos(math.radians(x)),
    #     "tand": lambda x: math.tan(math.radians(x)),
    #     "asind": lambda x: math.degrees(math.asin(x)),
    #     "acosd": lambda x: math.degrees(math.acos(x)),
    #     "atand": lambda x: math.degrees(math.atan(x)),
    #     "rt": math.sqrt,
    #     "ln": math.log,
    #
    #     "abs": abs,
    #     "deg": math.degrees,
    #     "rad": math.radians,
    # }

    # binops = {
    #     '+': lambda x, y: x + y,
    #     '-': lambda x, y: x - y,
    #     '*': lambda x, y: x * y,
    #     '/': lambda x, y: x / y,
    #     '^': lambda x, y: x ** y,
    #     '%': lambda x, y: x % y,
    # }

    def __init__(self):
        self.names = {}

    @_('ID EQUAL expr')
    def statement(self, p):
        self.names[p.ID] = p.expr

    @_('expr')
    def statement(self, p):
        print(p.expr)

    # Grammar rules and actions
    @_('expr PLUS term')
    def expr(self, p):
        return p.expr + p.term

    @_('expr MINUS term')
    def expr(self, p):
        return p.expr - p.term

    @_('term')
    def expr(self, p):
        return p.term

    @_('term TIMES factor')
    def term(self, p):
        return p.term * p.factor

    @_('term DIVIDE factor')
    def term(self, p):
        return p.term / p.factor

    @_('LT')
    def comparison(self, p):
        return p.LT

    @_('GT')
    def comparison(self, p):
        return p.GT

    @_('LTE')
    def comparison(self, p):
        return p.LTE

    @_('GTE')
    def comparison(self, p):
        return p.GTE

    @_('factor')
    def term(self, p):
        return p.factor

    @_('INTEGER')
    def factor(self, p):
        return p.INTEGER

    @_('FLOAT')
    def factor(self, p):
        return p.FLOAT

    @_('LPAREN')
    def expr(self, p):
        return p

    @_('RPAREN')
    def expr(self, p):
        return p

    @_('LPAREN expr RPAREN')
    def factor(self, p):
        return p.expr

    @_('LBLOCK expr RBLOCK')
    def factor(self, p):
        return p.expr

    @_('LBRACE expr RBRACE')
    def factor(self, p):
        return p.expr

    @_('IF LPAREN expr RPAREN ')
    def statement(self, p):
        pass

    @_('expr GT expr')
    def expr(self, p):
        if p[2] == '>':
            p[0] = p[1] > p[3]

    @_('expr LT expr')
    def expr(self, p):
        if p[2] == '<':
            p[0] = p[1] < p[3]

    @_('expr GTE expr')
    def expr(self, p):
        if p[2] == '>=':
            p[0] = p[1] >= p[3]

    @_('expr LTE expr')
    def expr(self, p):
        if p[2] == '<=':
            p[0] = p[1] <= p[3]

    @_('expr DOUBLEE expr')
    def expr(self, p):
        if p[2] == '==':
            p[0] = p[1] == p[3]

    @_('expr NOTE expr')
    def expr(self, p):
        if p[2] == '!=':
            p[0] = p[1] != p[3]

    @_('expr AND expr')
    def expr(self, p):
        if p[2] == '&':
            p[0] = p[1] and p[3]

    @_('expr OR expr')
    def expr(self, p):
        if p[2] == '|':
            p[0] = p[1] or p[3]

    @_('ID')
    def expr(self, p):
        try:
            return self.names[p.ID]
        except LookupError:
            print("Undefined name '%s'" % p.ID)
            return 0


# Aqui es que corre el programa

def REPL(lexer, parser):
    while True:
        try:
            print(colored('netsie> ', 'yellow', attrs=['bold']), end='')
            text = input()
        except EOFError:
            break
        if text:
            # parser.parse(lexer.tokenize(text))
            for tok in lexer.tokenize(text):
                print('type=%r, value=%r' % (tok.type, tok.value))
