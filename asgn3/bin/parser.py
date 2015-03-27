import sys
import ply.yacc as yacc
import scalalex
import pickle
import sys
import os.path
import re
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)))
from include.grammar import *

def p_error(p):
  
    flag=-1;
    # print dir(yacc)
    
    # assert(False)

    # print("Syntax error at '%s'" % p.value),
    # print('\t Error: {}'.format(p))

    while 1:

        tok = yacc.token()             # Get the next token
        if not tok:
            flag=1
            break
        if tok.type == 'STATE_END': 
            flag=0
            break

    if flag==0:
        yacc.errok()
        return tok
    else:
        yacc.restart()
      
def printnodes(current_node, file):
    #sys.stderr.write(str(current_node.name) + "\n")
    if (len(current_node.children)==0):
        return;
    for i in current_node.children:
        flag=0
        if (isinstance(i.name, basestring)):
            matchObj = re.match( r'".*"', i.name , re.M|re.I)
            if matchObj:
                if (len(matchObj.group())==len(i.name)):
                    flag=1
                    print >> file, str(current_node.id)+" [label=\""+str(current_node.name)+"\"];"+str(i.id)+" [label=\""+str((matchObj.group()).replace('"', '\\\"'))+"\"];"+str(current_node.id)+"->"+str(i.id)
        if flag==0 :
            print >> file, str(current_node.id)+" [label=\""+str(current_node.name)+"\"];"+str(i.id)+" [label=\""+str(i.name)+"\"];"+str(current_node.id)+"->"+str(i.id)
        flag=0
        
    for i in current_node.children:
        printnodes(i, file)

def printleaves(current_node, file):
    if (len(current_node.children) == 0):
        print >> file, str(current_node.name) + " "
    else:
        for i in current_node.children:
            printleaves(i)

# Get the token map
tokens = scalalex.tokens

# Build the grammar
parser=yacc.yacc()

#Read from file
f = open(sys.argv[1],"r")
code_full = f.read()
code_full=code_full+'\n'
f.close()

#parse over the input

#Find the dot file for the given parse tree
node = parser.parse(code_full)
if len(sys.argv) == 3:
  f = open(sys.argv[2], "w+")
else:
  filename=os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))+'/test1.dot'
  f = open(filename, "w+")
if node:
  print >> f, "digraph G {"
  printnodes(node, f)
  print >> f, "}"

#Find the left to right order of the leaves
# printleaves(node)