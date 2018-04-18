import sys
from antlr4 import *
from CLexer import CLexer
from CParser import CParser
from CsubListener import CsubListener
from CsubVisitor import CsubVisitor
 
def main(argv):
    input = FileStream(argv[1])
    lexer = CLexer(input)
    stream = CommonTokenStream(lexer)
    parser = CParser(stream)
    tree = parser.program()
    visitor = CsubVisitor()
    visitor.visit(tree)
 
if __name__ == '__main__':
    main(sys.argv)