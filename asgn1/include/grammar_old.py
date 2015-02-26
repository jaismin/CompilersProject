# dictionary of names
names = { }

precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('right','UMINUS'),
    )

def p_program_structure(p):
    'ProgramStructure : HeaderDef ObjectDef'

def p_header_define(p):
    '''HeaderDef : Package HeaderDef
                | Import HeaderDef
                | empty'''

# Library Naming

def p_import_librarynames(p):
    '''LibraryName : IDENTIFIER DOT LibraryName
                    | IDENTIFIER'''

def p_import_expression(p):
    '''ImportExpr : ImportExpr COMMA LibraryName 
                  | LibraryName
    '''

#package definition

def p_package_define(p):
    'Package : KWRD_PACKAGE ImportExpr'


#import definition
def p_import_define(p):
    '''Import : KWRD_IMPORT ImportExpr 
              | KWRD_IMPORT ImportExpr STATE_END'''


#object definition

def p_object_define(p):
    'ObjectDef : ObjectDeclare BLOCK_BEGIN Block BLOCK_END'

# object declaration
def p_object_declare(p):
    '''ObjectDeclare : KWRD_OBJECT IDENTIFIER 
                | KWRD_OBJECT IDENTIFIER KWRD_EXTNDS IDENTIFIER'''


# block arithmetic_statements
def p_block_statements(p):
    '''Block : arithmetic_statement STATE_END Block
                        | print_st STATE_END Block
                        | empty'''



def p_arithmetic_statement_assign(p):
    'arithmetic_statement : IDENTIFIER ASSIGN expression'
    names[p[1]] = p[3]

def p_arithmetic_statement_expr(p):
    'arithmetic_statement : expression'
    # print(p[1])

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
    "expression : LPAREN expression RPAREN"
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

def p_printstatement_1(p):
    "print_st : IDENTIFIER LPAREN IDENTIFIER RPAREN "
    try:
        print(names[p[3]])
    except LookupError:
        print("Undefined name '%s'" % p[3])

def p_empty(p):
    'empty :'
    pass
def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")