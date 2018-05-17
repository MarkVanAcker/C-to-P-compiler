from antlr4.Token import Token

def Warning(t:Token,msg:str):

    if t is None:
        print("Warning: " + msg)
    else:
        print("Warning at line "+t.line+","+"column "+t.column+": "+ msg)
