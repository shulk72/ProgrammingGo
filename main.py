from core.lex import LexAnalyzer
from core.parser import NParser, REPL


if __name__ == '__main__':
    lexer = LexAnalyzer()
    parser = NParser()
    REPL(lexer, parser)
