from lex import LexAnalyzer
from parser import NParser, REPL

if __name__ == '__main__':
    data = ' [25/(3*40) + {300-20} -16.5]{(300-250)<(400-500)}20 & 30 | 50 # This is a comment'
    # Lexer = LexAnalyzer()
    # for tok in Lexer.tokenize(data):
    #     print('type=%r, value=%r' % (tok.type, tok.value))
    lexer = LexAnalyzer()
    parser = NParser()
    REPL(lexer, parser)