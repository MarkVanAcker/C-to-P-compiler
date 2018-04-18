from CVisitor import CVisitor
from CParser import CParser


class CsubVisitor(CVisitor):
    # Visit a parse tree produced by CParser#program.
    def visitTerminal(self, node):
        #print(node)
        return self.defaultResult()


    def visitChildren(self, node):
        result = self.defaultResult()
        n = node.getChildCount()
        for i in range(n):
            if not self.shouldVisitNextChild(node, result):
                return

            c = node.getChild(i)
            print(c)
            childResult = c.accept(self)
            result = self.aggregateResult(result, childResult)

        return result