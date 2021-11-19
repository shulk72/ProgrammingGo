from sly import Lexer


class LexAnalyzer(Lexer):
    tokens = {ID, PLUS, MINUS, TIMES,
              DIVIDE, DOUBLEE, EQUAL, LPAREN, RPAREN, LBRACE,
              RBRACE, LBLOCK, RBLOCK, LTE, GTE, LT, GT,
              NOTE, AND, OR, COMMENT, IF, ELSE, ELSEIF, WHILE,
              FOR, INTEGER, FLOAT, NEWLINE, PLOT
              }

    # String containing ignored characters between tokens
    ignore = ' \t'

    # Regular expression rules for tokens
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    DOUBLEE = r'\=\='
    EQUAL = r'='
    LPAREN = r'\('
    RPAREN = r'\)'
    LBRACE = r'\['
    RBRACE = r'\]'
    LBLOCK = r'\{'
    RBLOCK = r'\}'
    LTE = r'\<\='
    GTE = r'\>\='
    LT = r'\<'
    GT = r'\>'
    NOTE = r'\!='
    AND = r'\&'
    OR = r'\|'
    COMMENT = r'\#.*'
    ID['if'] = IF
    ID['else']= ELSE
    ID['elseif'] = ELSEIF
    ID['while'] = WHILE
    ID['for'] = FOR
    ID['sin']   = MATHFUNC
    ID['cos']   = MATHFUNC
    ID['tan']   = MATHFUNC
    ID['asin']  = MATHFUNC
    ID['acos']  = MATHFUNC
    ID['atan']  = MATHFUNC
    ID['sind']  = MATHFUNC
    ID['cosd']  = MATHFUNC
    ID['tand']  = MATHFUNC
    ID['asind'] = MATHFUNC
    ID['acosd'] = MATHFUNC
    ID['atand'] = MATHFUNC
    ID['rt']    = MATHFUNC
    ID['ln']    = MATHFUNC
    ID['angle'] = MATHFUNC
    ID['abs']   = MATHFUNC
    ID['plot] = PLOT
    
    @_(r'\d+')
    def INTEGER(self, t):
      t.value = int(t.value)
      return t

    @_(r'(\d*\.\d+)|(\d+\.\d*)')
    def FLOAT(self, t):
      t.value = float(t.value)
      return t

# Define a rule so we can track line numbers
    @_(r'\n+')
    def NEWLINE(self, t):
      t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.Lexer.skip(1)

