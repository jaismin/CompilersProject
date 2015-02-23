import sys
sys.path.insert(0,"../..")

if sys.version_info[0] >= 3:
    raw_input = input

tokens = (
    'NAME','NUMBER',
    )

literals = ['=','+','-','*','/', '(',')']

# Tokens

t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Build the lexer
import ply.lex as lex
lex.lex()

class Node(object): 
    gid = 1   
    def __init__(self,name,children):
        self.name = name
        self.children = children
        self.id=Node.gid
        Node.gid+=1

# Parsing rules
precedence = (
    ('left','+','-'),
    ('left','*','/'),
    ('right','UMINUS'),
    )

# dictionary of names
names = { }

def create_child_nodes(name1,name2):
    leaf1 = Node(name2,[])
    leaf2 = Node(name1,[leaf1])
    return leaf2

def p_statement_assign(p):
    'statement : NAME "=" expression'
    names[p[1]] = p[3]
    child1=create_child_nodes("NAME",p[1]);
    child2=create_child_nodes("EQUAL",p[2]);
    p[0] = Node("statement -> NAME = expression",[child1,child2,p[3]])
    

def p_statement_expr(p):
    'statement : expression'
    p[0] = Node("statement -> expression",[p[1]])
    
    # print(p[1])

def p_expression_binop(p):
    '''expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression'''

    #p[0] = Node("binop",[p[1],p[3]], p[2])
    child1=create_child_nodes("binop",p[2])
    p[0] = Node("expression -> expression binop expression",[p[1],child1,p[3]])
    # if p[2] == '+'  : #p[0] = p[1] + p[3]
    # elif p[2] == '-': #p[0] = p[1] - p[3]
    # elif p[2] == '*': #p[0] = p[1] * p[3]
    # elif p[2] == '/': #p[0] = p[1] / p[3]

def p_expression_uminus(p):
    "expression : '-' expression %prec UMINUS"
    #p[0] = -p[2]

def p_expression_group(p):
    "expression : '(' expression ')'"
    child1=create_child_nodes("LEFT_PAREN",p[1])
    child3=create_child_nodes("RIGHT_PAREN",p[3])
    p[0] = Node("expression -> ( expression )",[child1,p[2],child3])
    #p[0] = Node("group", [p[2]], ['(',')'])
    
    # #p[0] = p[2]

def p_expression_number(p):
    "expression : NUMBER"
    child1=create_child_nodes("NUMBER",p[1])
    p[0] = Node("expression -> NUMBER",[child1])
    # #p[0] = p[1]
    #p[0] = Node("number", [], [p[1]])
    

def p_expression_name(p):
    "expression : NAME"
    try:
        child1=create_child_nodes("NAME",p[1])
        p[0] = Node("expression -> NAME",[child1])
        # p[0] = names[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        assert(False);
        p[0] = 0

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
yacc.yacc()

def printnodes(current_node):
        # current_node.id = gid
        # print current_node.name
        if (len(current_node.children)==0):
            return;
        # val2 = val
        for i in current_node.children:
            # printnodes(i) 
            # val2 += 1
            print str(current_node.id)+" [label=\""+str(current_node.name)+"\"];"+str(i.id)+" [label=\""+str(i.name)+"\"];"+str(current_node.id)+"->"+str(i.id)
        for i in current_node.children:
            # val=val+1
            printnodes(i)

        #     print current_node.count,'->',i
        #     # print ,
        # for i in current_node.children:
        #     print current_node.count,'->',i.count             
        #     # print i.type,
        # # print 
        # for i in current_node.children:
        #     # print 'hello'
        #     printnodes(i)

while 1:
    try:
        s = raw_input('calc > ')
    except EOFError:
        break
    if not s: continue
    # print yacc.parse(s).children[0].children[0].type
    node=yacc.parse(s)
    printnodes(node)
    
    # for node in yacc.parse(s):
    #     print node.type
    # yacc.parse(s)
