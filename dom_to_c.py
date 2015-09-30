import sys

from antlr4 import *

from CJSONLexer import CJSONLexer
from CJSONParser import CJSONParser


def main(argv):
    input = FileStream(argv[1])
    lexer = CJSONLexer(input)
    stream = CommonTokenStream(lexer)
    parser = CJSONParser(stream)
    tree = parser.StartRule()

if __name__ == '__main__':

    main(sys.argv)
