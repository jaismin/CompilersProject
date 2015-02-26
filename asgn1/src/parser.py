import sys
import scalalex 
import ply.yacc as yacc
import pickle
import sys
import os.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)))
from include.grammar import *

class Node(object): 
    gid = 1   
    def __init__(self,name,children,val=None):
        self.name = name
        self.children = children
        self.id=Node.gid
        self.val=val
        Node.gid+=1

def create_child_nodes(name1,name2):
    leaf1 = Node(name2,[])
    leaf2 = Node(name1,[leaf1])
    return leaf2

def printnodes(current_node):
    if (len(current_node.children)==0):
        return;
    for i in current_node.children:
        print str(current_node.id)+" [label=\""+str(current_node.name)+"\"];"+str(i.id)+" [label=\""+str(i.name)+"\"];"+str(current_node.id)+"->"+str(i.id)
    for i in current_node.children:
        printnodes(i)

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
node=parser.parse(code_full)
# printnodes(node)