from sly import Parser
import math

class GeckoParser(Parser):
    # debugfile = 'parser.out'

    tokens = GeckoLexer.tokens

    precedence = (
        ('right', CROCANTE),
        ('right', ASSIGN),
        ('left', INTEGRAL),
        ('left', THEN),
        ('left', WITH_EXPR),
        ('left', MONO_WITH_EXPR, COMMA),
        ('right', WITH_ASSIGNS),
        ('left', PLUS, MINUS),
        ('left', TIMES, DIV, MOD),
        ('right', CONSTANT),
        ('right', MATHFUNC, UMINUS),
        ('right', POW),
        ('nonassoc', NUMBER),
        ('nonassoc', AT, DEGSYM),
    )

    mathfuncs = {
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "asin": math.asin,
        "acos": math.acos,
        "atan": math.atan,
        "sind": lambda x: math.sin(math.radians(x)),
        "cosd": lambda x: math.cos(math.radians(x)),
        "tand": lambda x: math.tan(math.radians(x)),
        "asind": lambda x: math.degrees(math.asin(x)),
        "acosd": lambda x: math.degrees(math.acos(x)),
        "atand": lambda x: math.degrees(math.atan(x)),
        "rt": math.sqrt,
        "ln": math.log,
        "angle": np.angle,
        "abs": abs,
        "deg": math.degrees,
        "rad": math.radians,
    }

    binops = {
        '+': lambda x,y: x+y,
        '-': lambda x,y: x-y,
        '*': lambda x,y: x*y,
        '/': lambda x,y: x/y,
        '^': lambda x,y: x**y,
        '%': lambda x,y: x%y,
    }




