from build.CParser import *


class CParser_e(CParser):

    def notifyErrorListeners(self, msg:str, offendingToken:Token = None, e:RecognitionException = None):
        if offendingToken is None:
            offendingToken = self.getCurrentToken()
        self._syntaxErrors += 1
        line = offendingToken.line
        column = offendingToken.column
        listener = self.getErrorListenerDispatch()
        listener.syntaxError(self, offendingToken, line, column, msg, e)
        raise Exception()
