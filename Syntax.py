from sly import Parser
from lex import LexAnalyzer

class CalcParser(Parser):
    # Get the token list from the lexer (required)
    tokens = LexAnalyzer.tokens

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
    def expr(self,p):
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
    def statement(self,p):
        pass

    @_('expr GT expr')
    def expr(self,p):
        if p[2] == '>':
            p[0] = p[1] > p[3]
    @_('expr LT expr')
    def expr(self,p):
        if p[2] == '<':
            p[0] = p[1] < p[3]
    @_('expr GTE expr')
    def expr(self,p):
        if p[2] == '>=':
            p[0] = p[1] >= p[3]
    @_('expr LTE expr')
    def expr(self,p):
        if p[2] == '<=':
            p[0] = p[1] <= p[3]
    @_('expr DOUBLEE expr')
    def expr(self,p):
        if p[2] == '==':
            p[0] = p[1] == p[3]
    @_('expr NOTE expr')
    def expr(self,p):
        if p[2] == '!=':
            p[0] = p[1] != p[3]
    @_('expr AND expr')
    def expr(self,p):
        if p[2] == '&':
            p[0] = p[1] and p[3]
    @_('expr OR expr')
    def expr(self,p):
        if p[2] == '|':
            p[0] = p[1] or p[3]

    @_('ID')
    def expr(self, p):
        try:
            return self.names[p.ID]
        except LookupError:
            print("Undefined name '%s'" % p.ID)
            return 0

if __name__ == '__main__':
    lexer = LexAnalyzer()
    parser = CalcParser()

    while True:
        try:
            text = input('calc > ')
            result = parser.parse(lexer.tokenize(text))
            print(result)
        except EOFError:
            break

