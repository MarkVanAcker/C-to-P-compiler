import glob, os, sys


os.chdir("./test") # run each c file in test dir
files = []
for file in glob.glob("*.c"):
    files.append(file) # collect each file

os.chdir("./..") # return to root dir
for file in files:
    print("Running testfile: " + file)
    os.system('python3 main.py ' + './test/' + file) # run each test case
    os.system('dot -Tpng .AST.dot -o ' + './test/abstract_syntax_trees/' + file + '.png') # create an AST for each case
    print("Created AST: " + file + '.png')
    print('\n')
