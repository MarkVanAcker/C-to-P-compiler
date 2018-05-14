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

if not os.path.exists('./testoutput'):
    os.makedirs('./testoutput')


if not os.path.exists('./testoutput/abstract_syntax_trees/'):
    os.makedirs('./testoutput/abstract_syntax_trees/')


if not os.path.exists('./testoutput/symbol_tables/'):
    os.makedirs('./testoutput/symbol_tables/')

for file in files:
    print("Running testfile: " + file)
    os.system('python c2p.py ' + './test/' + file) # run each test case
    os.system('dot -Tpng ./output/.AST.dot -o ' + './testoutput/abstract_syntax_trees/' + file + '.png') # create an AST for each case
    print("Created AST: " + file + '.png')
    os.system('dot -Tpng ./output/.ST.dot -o ' + './testoutput/symbol_tables/' + file + '.png')  # create an AST for each case
    print("Created Symbol Table: " + file + '.png')

    print('\n')



print("\n#######################################################\n" +
      "#               Running Testcases Done                #\n" +
      "#######################################################\n\n"
) 

print( "All the AST's can be found in ./testoutput/abstract_syntax_trees")
print( "All the Symbol Tables can be found in ./testoutput/symbol_tables")
