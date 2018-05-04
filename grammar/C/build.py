import glob, os, sys


print("Building Antlr4 Python files form C.g4 grammar\n")
#TODO: maybe mkdir build
os.system('java -jar ./lib/antlr-4.7.1-complete.jar -Dlanguage=Python3 C.g4 -visitor -o ./build') # building



