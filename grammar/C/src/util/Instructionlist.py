from src.util.PInstruction import *

#Container for all instructions

class InstructionList:

    def __init__(self):
        self.instructionlist = []
        #might add some bonus info

    def AddInstruction(self,ins):

        if isinstance(ins,InstructionList):
            self.instructionlist.extend(ins.instructionlist)
        elif isinstance(ins,PInstruction):

            self.instructionlist.append(ins)

        else:
            pass # can this even occur?

    def printProgram(self):

        f = open('program.p','w')

        for ins in self.instructionlist:
            f.write(ins.write)

        f.close()
