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

# expression
def p_expression(p):
    '''expression : assignment_expression'''
    # val=p[1].val
    # p[0] = Node("",)
    # p[0] = p[1]

def p_assignment_expression(p):
    '''assignment_expression : assignment
                             | conditional_expression'''
    # val=p[1].val

# assignment

def p_assignment(p):
    '''assignment : valid_variable assignment_operator assignment_expression'''
    # p[0] = Assignment(p[2], p[1], p[3])


def p_assignment_operator(p):
    '''assignment_operator : '='
                               | TIMES_ASSIGN
                               | DIVIDE_ASSIGN
                               | REMAINDER_ASSIGN
                               | PLUS_ASSIGN
                               | MINUS_ASSIGN
                               | LSHIFT_ASSIGN
                               | RSHIFT_ASSIGN
                               | RRSHIFT_ASSIGN
                               | AND_ASSIGN
                               | OR_ASSIGN
                               | XOR_ASSIGN'''
        # p[0] = p[1]

# OR(||) has least precedence, and OR is left assosiative 
# a||b||c => first evalutae a||b then (a||b)||c
def p_conditional_or_expression(p):
    '''conditional_or_expression : conditional_and_expression
                                | conditional_or_expression OR conditional_and_expression'''
    # self.binop(p, ConditionalOr)

# AND(&&) has next least precedence, and AND is left assosiative 
# a&&b&&c => first evalutae a&&b then (a&&b)&&c

def p_conditional_and_expression(p):
    '''conditional_and_expression : inclusive_or_expression
                                    | conditional_and_expression AND inclusive_or_expression'''
    # self.binop(p, ConditionalAnd)

def p_inclusive_or_expression(p):
    '''inclusive_or_expression : exclusive_or_expression
                                   | inclusive_or_expression '|' exclusive_or_expression'''
        # self.binop(p, Or)

def p_exclusive_or_expression(p):
    '''exclusive_or_expression : and_expression
                                   | exclusive_or_expression '^' and_expression'''
    # self.binop(p, Xor)

def p_and_expression(p):
    '''and_expression : equality_expression
                          | and_expression '&' equality_expression'''
    # self.binop(p, And)
def p_equality_expression(p):
    '''equality_expression : relational_expression
                            | equality_expression EQ relational_expression
                            | equality_expression NEQ relational_expression'''
    # self.binop(p, Equality)
def p_relational_expression(p):
    '''relational_expression : shift_expression
                                 | relational_expression '>' shift_expression
                                 | relational_expression '<' shift_expression
                                 | relational_expression GTEQ shift_expression
                                 | relational_expression LTEQ shift_expression'''
    # self.binop(p, Relational)
def p_shift_expression(p):
        '''shift_expression : additive_expression
                            | shift_expression LSHIFT additive_expression
                            | shift_expression RSHIFT additive_expression
                            | shift_expression RRSHIFT additive_expression'''
        # self.binop(p, Shift)
def p_additive_expression(p):
    '''additive_expression : multiplicative_expression
                               | additive_expression '+' multiplicative_expression
                               | additive_expression '-' multiplicative_expression'''
    # self.binop(p, Additive)

def p_multiplicative_expression(p):
    '''multiplicative_expression : unary_expression
                                     | multiplicative_expression '*' unary_expression
                                     | multiplicative_expression '/' unary_expression
                                     | multiplicative_expression '%' unary_expression'''
    # self.binop(p, Multiplicative)
def p_unary_expression(p):
    '''unary_expression :'+' unary_expression
                            | '-' unary_expression
                            | unary_expression_not_plus_minus'''


def p_unary_expression_not_plus_minus(p):
    '''unary_expression_not_plus_minus : variable_literal
                                           | '~' unary_expression
                                           | '!' unary_expression'''

def p_primary(p):
    '''primary : literal
                | method_invocation'''


def p_literal(p):
    '''literal : int_float
                | CHAR_LITERAL
                | STRING_LITERAL
                | TRUE
                | FALSE
                | NULL'''


def p_int_float(p):
    '''int_float : Integer | 
                | Float'''

def p_method_invocation(self, p):
    '''method_invocation : NAME '(' argument_list_opt ')' '''
    # p[0] = MethodInvocation(p[1], arguments=p[3])

def p_method_invocation3(self, p):
    '''method_invocation : name '.' NAME '(' argument_list_opt ')' '''
    # p[0] = MethodInvocation(p[3], target=p[1], arguments=p[5])

def p_array_access(self, p):
    '''array_access : name '(' expression ')' '''
        # p[0] = ArrayAccess(p[3], p[1])

def p_argument_list_opt(self, p):
    '''argument_list_opt : argument_list'''
        # p[0] = p[1]

def p_argument_list_opt2(self, p):
    '''argument_list_opt : empty'''
        # p[0] = []

def p_argument_list(self, p):
    '''argument_list : variable_literal
                    | argument_list ',' variable_literal'''
    # if len(p) == 2:
    #     p[0] = [p[1]]
    # else:
    #     p[0] = p[1] + [p[3]]

# object identifier and identifier names for left hand assignment

def p_name(p):
    '''name : simple_name
            | qualified_name'''
    # p[0] = p[1]

def p_simple_name(p):
    '''simple_name : NAME'''
    # p[0] = Name(p[1])

def p_qualified_name(p):
    '''qualified_name : name '.' simple_name'''
    # p[1].append_name(p[3])
    # p[0] = p[1]

def p_valid_variable
    '''valid_variable : name
                      | array_access'''


def p_variableliteral(p):
    '''variable_literal : valid_variable
                        | primary'''


# print statement
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