import sys
import scalalex 
import ply.yacc as yacc

# Get the token map
tokens = scalalex.tokens

#Parsing Rules

precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('right','UMINUS'),
    )


# dictionary of names
names = { }


def p_statement_assign(p):
    'statement : IDENTIFIER ASSIGN expression'
    names[p[1]] = p[3]

def p_statement_expr(p):
    'statement : expression'
    print(p[1])

def p_expression_binop(p):
    '''expression : expression PLUS  expression
                  | expression MINUS  expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if p[2] == '+'  : p[0] = p[1] + p[3]
    elif p[2] == '-' : p[0] = p[1] - p[3]
    elif p[2] == '*' : p[0] = p[1] * p[3]
    elif p[2] == '/' : p[0] = p[1] / p[3]

def p_expression_uminus(p):
    "expression : '-' expression %prec UMINUS"
    p[0] = -p[2]

def p_expression_group(p):
    "expression : '(' expression ')'"
    p[0] = p[2]

def p_expression_number(p):
    "expression : INT_CONST"
    p[0] = p[1]

def p_expression_name(p):
    "expression : IDENTIFIER"
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

import profile
# Build the grammar

yacc.yacc()
#yacc.yacc(method='LALR',write_tables=False,debug=True)

#profile.run("yacc.yacc(method='LALR')")

while 1:
    try:
        s = raw_input('calc > ')
    except EOFError:
        break
    if not s: continue
    yacc.parse(s)
