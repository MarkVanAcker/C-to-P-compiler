from antlr4.Token import Token

class SemanticsError(Exception):
    def __init__(self,t:Token,message:str):

        newmessage = message
        if t is not None:
            newmessage = str(t.line)+":"+str(t.column)+": "+message

        super().__init__("SemanticsError: "+ newmessage)