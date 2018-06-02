import sys
from antlr4 import *
from build.CLexer import CLexer
from src.error.CParser_e import CParser_e
from src.parser.CsubVisitor import CsubVisitor
from src.parser.traverser import AstVisitor
from src.parser.SymbolTable import *
from src.astclasses.AST import *
from src.error.Error import SemanticsError

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
        ast.handle(st)
        ToDotAST(ast)
        ToDotST(st)
        code = ast.getCode()
        code.printProgram()
    except SemanticsError as e:
        print(e)
    #except Exception as e:
    #    print(e)



if __name__ == '__main__':
    main(sys.argv)
