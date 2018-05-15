import sys
from antlr4 import *
from build.CLexer import CLexer
from src.error.CParser_e import CParser_e
from src.parser.CsubVisitor import CsubVisitor
from src.parser.traverser import AstVisitor
from src.parser.SymbolTable import *
from src.parser.AST import *

def main(argv):
    input = FileStream(argv[1])
    lexer = CLexer(input)
    stream = CommonTokenStream(lexer)
    parser = CParser_e(stream)
    try:
        tree = parser.program()
        visitor = CsubVisitor()
        ast = visitor.visit(tree)
        ToDotAST(ast)
        st = SymbolTable()
        #astvisit = AstVisitor(ast,st)
        #astvisit.traverse()
        ToDotST(st)
    except Exception as e:
        print("Compilation terminated: ", e.args)



if __name__ == '__main__':
    main(sys.argv)
