from src.util.PInstruction import *

#Container for all instructions

class InstructionList:

    def __init__(self):
        self.instructionlist = []
        self.maxStackSpace = 0
        #might add some bonus info

    def AddInstruction(self,ins):


        if isinstance(ins,InstructionList):
            if self.maxStackSpace < ins.maxStackSpace:
                self.maxStackSpace = ins.maxStackSpace
            self.instructionlist.extend(ins.instructionlist)
        elif isinstance(ins,PInstruction):
            self.instructionlist.append(ins)

        else:
            pass # can this even occur?

    def printProgram(self,name = 'program.p'):

        f = open('output/' + name,'w')
        for ins in self.instructionlist:
            f.write(ins.write())
            f.write('\n')

        f.close()
