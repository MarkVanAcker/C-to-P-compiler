import glob, os, sys


os.chdir("./test") # run each c file in test dir
files = []
for file in glob.glob("*.c"):
    files.append(file) # collect each file

os.chdir("./..") # return to root dir

print("\n#######################################################\n" +
      "#                 Running Testcases                   #\n" +
      "#######################################################\n\n\n"
) 

for file in files:
    print("Running testfile: " + file)
    os.system('python3 c2p.py ' + './test/' + file) # run each test case
    os.system('dot -Tpng .AST.dot -o ' + './test/abstract_syntax_trees/' + file + '.png') # create an AST for each case
    print("Created AST: " + file + '.png')
    print('\n')



print("\n#######################################################\n" +
      "#               Running Testcases Done                #\n" +
      "#######################################################\n\n"
) 

print( "All the AST's can be found in ./test/abstract_syntax_trees")
