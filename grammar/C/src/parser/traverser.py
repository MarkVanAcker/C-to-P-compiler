class AstVisitor:
    def __init__(self,root,st):
        self.root = root
        self.st = st



    def traverse(self):

        for child in self.root.children:
            child.handle(self.st)






