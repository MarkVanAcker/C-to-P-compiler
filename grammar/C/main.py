import sys
from antlr4 import *
from CLexer import CLexer
from CParser_e import CParser_e
from CsubListener import CsubListener
from CsubVisitor import CsubVisitor
from traverser import AstVisitor
from SymbolTable import *

def main(argv):
    input = FileStream(argv[1])
    lexer = CLexer(input)
    stream = CommonTokenStream(lexer)
    parser = CParser_e(stream)
    try:
        tree = parser.program()
        visitor = CsubVisitor()
        ast = visitor.visit(tree)
        st = SymbolTable()
        astvisit = AstVisitor(ast,st)
        astvisit.traverse()
        ToDotST(st)
    except Exception as e:
        print("Compilation terminated: ", e.args)



if __name__ == '__main__':
    main(sys.argv)
