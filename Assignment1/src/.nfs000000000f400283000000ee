# lexer for a Scala language
import ply.lex as lex
import sys
import os.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)))
from include.tokensDefination import *
from include.regexDefination import *
import include.printLexerOutput as printLexerOutput

# build the lexer
lexer = lex.lex()

# read the file contents
f = open(sys.argv[1],"r")
code_full = f.read()
code_full=code_full+'\n'
f.close()

#use the lexer
lexer.input(code_full)

# print the output
printLexerOutput.printLexer(lexer,code_full)
