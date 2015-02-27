# dictionary of names
names = {}

def p_program_structure(p):
    'ProgramStructure : ObjectDef'

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
    '''assignment_operator :    ASSIGN
                               | TIMES_ASSIGN
                               | DIVIDE_ASSIGN
                               | REMAINDER_ASSIGN
                               | PLUS_ASSIGN
                               | MINUS_ASSIGN
                               | LSHIFT_ASSIGN
                               | RSHIFT_ASSIGN
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
                                   | inclusive_or_expression OR_BITWISE exclusive_or_expression'''
        # self.binop(p, Or)

def p_exclusive_or_expression(p):
    '''exclusive_or_expression : and_expression
                                   | exclusive_or_expression XOR and_expression'''
    # self.binop(p, Xor)

def p_and_expression(p):
    '''and_expression : equality_expression
                          | and_expression AND_BITWISE equality_expression'''
    # self.binop(p, And)
def p_equality_expression(p):
    '''equality_expression : relational_expression
                            | equality_expression EQUAL relational_expression
                            | equality_expression NEQUAL relational_expression'''
    # self.binop(p, Equality)
def p_relational_expression(p):
    '''relational_expression : shift_expression
                                 | relational_expression GREATER shift_expression
                                 | relational_expression LESS shift_expression
                                 | relational_expression GEQ shift_expression
                                 | relational_expression LEQ shift_expression'''
    # self.binop(p, Relational)
def p_shift_expression(p):
        '''shift_expression : additive_expression
                            | shift_expression LSHIFT additive_expression
                            | shift_expression RSHIFT additive_expression'''
        # self.binop(p, Shift)
def p_additive_expression(p):
    '''additive_expression : multiplicative_expression
                               | additive_expression PLUS multiplicative_expression
                               | additive_expression MINUS multiplicative_expression'''
    # self.binop(p, Additive)

def p_multiplicative_expression(p):
    '''multiplicative_expression : unary_expression
                                     | multiplicative_expression TIMES unary_expression
                                     | multiplicative_expression DIVIDE unary_expression
                                     | multiplicative_expression REMAINDER unary_expression'''
    # self.binop(p, Multiplicative)
def p_unary_expression(p):
    '''unary_expression :PLUS unary_expression
                            | MINUS unary_expression
                            | unary_expression_not_plus_minus'''


def p_unary_expression_not_plus_minus(p):
    '''unary_expression_not_plus_minus : variable_literal
                                           | TILDA unary_expression
                                           | NOT unary_expression'''

def p_primary(p):
    '''primary : literal
                | method_invocation'''


def p_literal(p):
    '''literal : int_float
                | CHARACTER
                | STRING_CONST
                | BOOL_CONSTT
                | BOOL_CONSTF
                | KWRD_NULL'''


def p_int_float(p):
    '''int_float : FLOAT_CONST | 
                | INT_CONST'''

def p_method_invocation(p):
    '''method_invocation : IDENTIFIER LPAREN argument_list_opt RPAREN '''
    # p[0] = MethodInvocation(p[1], arguments=p[3])

def p_method_invocation3(p):
    '''method_invocation : name DOT IDENTIFIER LPAREN argument_list_opt RPAREN '''
    # p[0] = MethodInvocation(p[3], target=p[1], arguments=p[5])

def p_array_access(p):
    '''array_access : name LPAREN expression RPAREN '''
        # p[0] = ArrayAccess(p[3], p[1])

def p_argument_list_opt(p):
    '''argument_list_opt : argument_list'''
        # p[0] = p[1]

def p_argument_list_opt2(p):
    '''argument_list_opt : empty'''
        # p[0] = []

def p_argument_list(p):
    '''argument_list : variable_literal
                    | argument_list COMMA variable_literal'''
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
    '''simple_name : IDENTIFIER'''
    # p[0] = Name(p[1])

def p_qualified_name(p):
    '''qualified_name : name DOT simple_name'''
    # p[1].append_name(p[3])
    # p[0] = p[1]

def p_valid_variable
    '''valid_variable : name
                      | array_access'''


def p_variableliteral(p):
    '''variable_literal : valid_variable
                        | primary'''



# BLOCK STATEMENTS


def p_block(p):
      '''block : '{' block_statements_opt '}' '''
        # p[0] = Block(p[2])

def p_block_statements_opt(p):
      '''block_statements_opt : block_statements'''
        # p[0] = p[1]

def p_block_statements_opt2(p):
    '''block_statements_opt : empty'''
    # p[0] = []

def p_block_statements(p):
      '''block_statements : block_statement
                            | block_statements block_statement'''

       # if len(p) == 2:
       #      p[0] = [p[1]]
       #  else:
       #      p[0] = p[1] + [p[2]]

def p_block_statement(p):
      '''block_statement : local_variable_declaration_statement
                           | statement
                           | class_declaration'''
        # p[0] = p[1]

def p_local_variable_declaration_statement(p):
      '''local_variable_declaration_statement : local_variable_declaration STATE_END '''
        # p[0] = p[1]

def p_local_variable_declaration_statement2(p):
      '''local_variable_declaration_statement : local_variable_declaration newline '''
        # p[0] = p[1]

def p_local_variable_declaration(p):
      '''local_variable_declaration : KWRD_VAR LPAREN variable_declarators RPAREN'''
        # p[0] = VariableDeclaration(p[1], p[2])

def p_local_variable_declaration2(p):
      '''local_variable_declaration : modifier KWRD_VAR LPAREN variable_declarators RPAREN'''
        # p[0] = VariableDeclaration(p[2], p[3], modifiers=p[1])

def p_variable_declarators(p):
      '''variable_declarators : variable_declarator
                                | variable_declarators COMMA variable_declarator'''
        # if len(p) == 2:
        #     p[0] = [p[1]]
        # else:
        #     p[0] = p[1] + [p[3]]

def p_variable_declarator(self, p):
      '''variable_declarator : variable_declarator_id'''

def p_variable_declarator_id(self, p):
      '''variable_declarator_id : IDENTIFIER COLON type'''
      # p[0] = Variable(p[1], dimensions=p[2])

def p_modifier(p):
      '''modifier : PROTECTED
                  | PRIVATE'''

        #  by default its public
        # p[0] = p[1]

def p_type(p):
        '''type : primitive_type
                | reference_type'''
        # p[0] = p[1]

def p_primitive_type(p):
    '''primitive_type : INT
                      | FLOAT
                      | CHAR
                      | STRING
                      | BOOLEAN'''
        # p[0] = p[1]

def p_reference_type(p):
      '''reference_type : class_type
                        | array_type'''
      # p[0] = p[1]

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
        print("Syntax error at EOF")+