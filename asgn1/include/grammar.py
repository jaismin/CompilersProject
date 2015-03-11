# this shit needs to be imported from parser.py
class Node(object): 
    gid = 1   
    def __init__(self,name,children,val=None):
        self.name = name
        self.children = children
        self.id=Node.gid
        self.val=val
        Node.gid+=1

def create_leaf(name1,name2):
    leaf1 = Node(name2,[])
    leaf2 = Node(name1,[leaf1])
    return leaf2

def p_program_structure(p):
    '''ProgramStructure : ObjectDef'''
    p[0] = Node("ProgramStructure", [p[1]])
    

#object definition

def p_object_define(p):
    'ObjectDef : ObjectDeclare block'
    p[0] = Node("ObjectDef", [p[1], p[2]])
   
# object declaration
def p_object_declare(p):
    '''ObjectDeclare : KWRD_OBJECT IDENTIFIER 
                | KWRD_OBJECT IDENTIFIER KWRD_EXTNDS IDENTIFIER'''
    if len(p) == 3:
      child1 = create_leaf("KWRD_OBJECT", p[1])
      child2 = create_leaf("IDENTIFIER", p[2])
      p[0] = Node("ObjectDeclare", [child1, child2])
    else:
      child1 = create_leaf("KWRD_OBJECT", p[1])
      child2 = create_leaf("IDENTIFIER", p[2])
      child3 = create_leaf("KWRD_EXTNDS", p[3])
      child4 = create_leaf("IDENTIFIER", p[4])
      p[0] = Node("ObjectDeclare", [child1, child2, child3, child4])

    

# expression
def p_expression(p):
    '''expression : assignment_expression'''
    p[0] = Node("expression", [p[1]])
    # val=p[1].val
    # p[0] = Node("",)
    # p[0] = p[1]

def p_expression_optional(p):
        '''expression_optional : expression
                          | empty'''
        p[0] = Node("expression_optional", [p[1]])
        # p[0] = p[1]


def p_assignment_expression(p):
    '''assignment_expression : assignment
                             | conditional_or_expression'''
    p[0] = Node("assignment_expression", [p[1]])
    # val=p[1].val

# assignment

def p_assignment(p):
    '''assignment : valid_variable assignment_operator assignment_expression'''
    p[0] = Node("assignment", [p[1], p[2], p[3]])
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
    child1 = create_leaf("ASSIGN_OP", p[1])
    p[0] = Node("assignment_operator", [child1])
        # p[0] = p[1]

# OR(||) has least precedence, and OR is left assosiative 
# a||b||c => first evalutae a||b then (a||b)||c
def p_conditional_or_expression(p):
    '''conditional_or_expression : conditional_and_expression
                                | conditional_or_expression OR conditional_and_expression'''
    if len(p) == 2:
      p[0] = Node("conditional_or_expression", [p[1]])
    else:
      child1 = create_leaf("OR", p[2])
      p[0] = Node("conditional_or_expression", [p[1], child1, p[3]])
    # self.binop(p, ConditionalOr)

# AND(&&) has next least precedence, and AND is left assosiative 
# a&&b&&c => first evalutae a&&b then (a&&b)&&c

def p_conditional_and_expression(p):
    '''conditional_and_expression : inclusive_or_expression
                                    | conditional_and_expression AND inclusive_or_expression'''
    if len(p) == 2:
      p[0] = Node("conditional_and_expression", [p[1]])
    else:
      child1 = create_leaf("AND", p[2])
      p[0] = Node("conditional_and_expression", [p[1], child1, p[3]])
    # self.binop(p, ConditionalAnd)

def p_inclusive_or_expression(p):
    '''inclusive_or_expression : exclusive_or_expression
                                   | inclusive_or_expression OR_BITWISE exclusive_or_expression'''
    if len(p) == 2:
      p[0] = Node("inclusive_or_expression", [p[1]])
    else:
      child1 = create_leaf("OR_BITWISE", p[2])
      p[0] = Node("inclusive_or_expression", [p[1], child1, p[3]])
        # self.binop(p, Or)

def p_exclusive_or_expression(p):
    '''exclusive_or_expression : and_expression
                                   | exclusive_or_expression XOR and_expression'''
    if len(p) == 2:
      p[0] = Node("exclusive_or_expression", [p[1]])
    else:
      child1 = create_leaf("XOR", p[2])
      p[0] = Node("exclusive_or_expression", [p[1], child1, p[3]])
    # self.binop(p, Xor)

def p_and_expression(p):
    '''and_expression : equality_expression
                          | and_expression AND_BITWISE equality_expression'''
    if len(p) == 2:
      p[0] = Node("and_expression", [p[1]])
    else:
      child1 = create_leaf("AND_BITWISE", p[2])
      p[0] = Node("and_expression", [p[1], child1, p[3]])
    # self.binop(p, And)
def p_equality_expression(p):
    '''equality_expression : relational_expression
                            | equality_expression EQUAL relational_expression
                            | equality_expression NEQUAL relational_expression'''
    if len(p) == 2:
      p[0] = Node("relational_expression", [p[1]])
    else:
      child1 = create_leaf("binop", p[2])
      p[0] = Node("relational_expression", [p[1], child1, p[3]])
    # self.binop(p, Equality)

def p_relational_expression(p):
    '''relational_expression : shift_expression
                                 | relational_expression GREATER shift_expression
                                 | relational_expression LESS shift_expression
                                 | relational_expression GEQ shift_expression
                                 | relational_expression LEQ shift_expression'''
    if len(p) == 2:
      p[0] = Node("relational_expression", [p[1]])
    else:
      child1 = create_leaf("binop", p[2])
      p[0] = Node("relational_expression", [p[1], child1, p[3]])
    # self.binop(p, Relational)

def p_shift_expression(p):
        '''shift_expression : additive_expression
                            | shift_expression LSHIFT additive_expression
                            | shift_expression RSHIFT additive_expression'''
        if len(p) == 2:
          p[0] = Node("shift_expression", [p[1]])
        else:
          child1 = create_leaf("binop", p[2])
          p[0] = Node("shift_expression", [p[1], child1, p[3]])
        # self.binop(p, Shift)
def p_additive_expression(p):
    '''additive_expression : multiplicative_expression
                               | additive_expression PLUS multiplicative_expression
                               | additive_expression MINUS multiplicative_expression'''
    if len(p) == 2:
      p[0] = Node("additive_expression", [p[1]])
    else:
      child1 = create_leaf("binop", p[2])
      p[0] = Node("additive_expression", [p[1], child1, p[3]])
    # self.binop(p, Additive)

def p_multiplicative_expression(p):
    '''multiplicative_expression : unary_expression
                                     | multiplicative_expression TIMES unary_expression
                                     | multiplicative_expression DIVIDE unary_expression
                                     | multiplicative_expression REMAINDER unary_expression'''
    if len(p) == 2:
      p[0] = Node("multiplicative_expression", [p[1]])
    else:
      child1 = create_leaf("binop", p[2])
      p[0] = Node("multiplicative_expression", [p[1], child1, p[3]])
    # self.binop(p, Multiplicative)
def p_unary_expression(p):
    '''unary_expression : PLUS unary_expression
                            | MINUS unary_expression
                            | unary_expression_not_plus_minus'''
    if len(p) == 3:
      child1 = create_leaf("unop", p[1])
      p[0] = Node("unary_expression", [child1, p[2]])
    else:
      p[0] = Node("unary_expression", [p[1]])

def p_unary_expression_not_plus_minus(p):
    '''unary_expression_not_plus_minus : variable_literal
                                           | TILDA unary_expression
                                           | NOT unary_expression
                                           | LPAREN expression RPAREN'''
    if len(p) == 2:
      p[0] = Node("unary_expression_not_plus_minus", [p[1]])
    elif len(p) == 3:
      child1 = create_leaf("unop", p[1])
      p[0] = Node("unary_expression_not_plus_minus", [child1, p[2]])
    else:
      child1 = create_leaf("LPAREN", p[1])
      child2 = create_leaf("RPAREN", p[3])
      p[0] = Node("unary_expression_not_plus_minus", [child1, p[2], child2])

def p_primary(p):
    '''primary : literal
                | method_invocation'''
    p[0] = Node("primary", [p[1]])


def p_literal(p):
    '''literal : int_float
                | CHARACTER
                | STRING_CONST
                | BOOL_CONSTT
                | BOOL_CONSTF
                | KWRD_NULL'''
    # Where is your god now
    if type(p[1]) == type("compiler-sucks"):    # here
      child1 = create_leaf("const", p[1])
      p[0] = Node("literal", [child1])
    else:
      p[0] = Node("literal", [p[1]])


def p_int_float(p):
    '''int_float : FLOAT_CONST
                | INT_CONST'''
    child1 = create_leaf("int-const", p[1])
    p[0] = Node("int_float", [child1])

# def p_method_invocation(p):
#     '''method_invocation : IDENTIFIER LPAREN argument_list_opt RPAREN '''
#     # p[0] = MethodInvocation(p[1], arguments=p[3])

def p_method_invocation(p):
    '''method_invocation : name LPAREN argument_list_opt RPAREN '''
    child1 = create_leaf("LPAREN", p[2])
    child2 = create_leaf("RPAREN", p[4])
    p[0] = Node("method_invocation", [p[1], child1, p[3], child2])
    # p[0] = MethodInvocation(p[3], target=p[1], arguments=p[5])

def p_array_access(p):
    '''array_access : name LBPAREN expression RBPAREN '''
    child1 = create_leaf("LPAREN", p[2])
    child2 = create_leaf("RPAREN", p[4])
    p[0] = Node("array_access", [p[1], child1, p[3], child2])   
        # p[0] = ArrayAccess(p[3], p[1])

def p_argument_list_opt(p):
    '''argument_list_opt : argument_list'''
    p[0] = Node("argument_list_opt", [p[1]])
        # p[0] = p[1]

def p_argument_list_opt2(p):
    '''argument_list_opt : empty'''
    p[0] = Node("argument_list_opt", [p[1]])
        # p[0] = []

def p_argument_list(p):
    '''argument_list : expression
                    | argument_list COMMA expression'''
    if len(p) == 2:
      p[0] = Node("argument_list", [p[1]])
    else:
      child1 = create_leaf("COMMA", p[2])
      p[0] = Node("argument_list", [p[1], child1, p[3]])
    # if len(p) == 2:
    #     p[0] = [p[1]]
    # else:
    #     p[0] = p[1] + [p[3]]



# object identifier and identifier names for left hand assignment

def p_name(p):
    '''name : simple_name
            | qualified_name'''
    p[0] = Node("name", [p[1]])
    # p[0] = p[1]

def p_simple_name(p):
    '''simple_name : IDENTIFIER'''
    child1 = create_leaf("IDENTIFIER", p[1])
    p[0] = Node("simple_name", [child1])
    # p[0] = Name(p[1])

def p_qualified_name(p):
    '''qualified_name : name DOT simple_name'''
    child1 = create_leaf("DOT", p[2])
    p[0] = Node("qualified_name", [p[1], child1, p[3]])
    # p[1].append_name(p[3])
    # p[0] = p[1]

def p_valid_variable(p):
    '''valid_variable : name
                      | array_access'''
    p[0] = Node("valid_variable", [p[1]])


def p_variableliteral(p):
    '''variable_literal : valid_variable
                        | primary'''
    p[0] = Node("variable_literal", [p[1]])



# BLOCK STATEMENTS


def p_block(p):
      '''block : BLOCK_BEGIN block_statements_opt BLOCK_END '''
      child1 = create_leaf("BLOCK_BEGIN", p[1])
      child2 = create_leaf("BLOCK_END", p[3])
      p[0] = Node("block", [child1, p[2], child2])
        # p[0] = Block(p[2])

def p_block_statements_opt(p):
      '''block_statements_opt : block_statements'''
      p[0] = Node("block_statements_opt", [p[1]])

def p_block_statements_opt2(p):
    '''block_statements_opt : empty'''
    p[0] = Node("block_statements_opt", [p[1]])

def p_block_statements(p):
      '''block_statements : block_statement
                            | block_statements block_statement'''
      if len(p) == 2:
        p[0] = Node("block_statement", [p[1]])
      else:
        p[0] = Node("block_statement", [p[1], p[2]])
       # if len(p) == 2:
       #      p[0] = [p[1]]
       #  else:
       #      p[0] = p[1] + [p[2]]

def p_block_statement(p):
      '''block_statement : local_variable_declaration_statement
                           | statement'''
                           # | class_declaration
      p[0] = Node("block_statement", [p[1]])
        # p[0] = p[1]

# var (a:Int)=(h);
# var (a:Int,b:Int,c:Int)=(1,2,3);
# var (a:Int)=(h)
# var (a:Int,b:Int,c:Int)=(1,2,3)
# supported

def p_modifier_opts(p):
  '''modifier_opts : modifier
                    | empty '''
  p[0] = Node("modifier_opts", [p[1]])

def p_declaration_keyword(p):
  '''declaration_keyword : KWRD_VAR
                    | KWRD_VAL '''
  child1 = create_leaf("KWRD VAR/VAL", p[1])
  p[0] = Node("declaration_keyword", [child1])


def p_local_variable_declaration_statement(p):
      '''local_variable_declaration_statement : local_variable_declaration STATE_END '''
      child1 = create_leaf("STATE_END", p[2])
      p[0] = Node("local_variable_declaration_statement", [p[1], child1])
        # p[0] = p[1]

# 
def p_local_variable_declaration(p):
      '''local_variable_declaration : modifier_opts declaration_keyword variable_declaration_body'''
      p[0] = Node("local_variable_declaration", [p[1], p[2], p[3]])
        # p[0] = VariableDeclaration(p[1], p[2])

def p_variable_declaration_body(p):
      '''variable_declaration_body : variable_declarator ASSIGN  expression 
                                    | LPAREN variable_declarators RPAREN ASSIGN LPAREN argument_list RPAREN'''
      if len(p) == 4:
        child1 = create_leaf("ASSIGN", p[2])
        p[0] = Node("variable_declaration_body", [p[1], child1, p[3]])
      else:
        child1 = create_leaf("LPAREN", p[1])
        child2 = create_leaf("RPAREN", p[3])
        child3 = create_leaf("ASSIGN", p[4])
        child4 = create_leaf("LPAREN", p[5])
        child5 = create_leaf("RPAREN", p[7])
        p[0] = Node("variable_declaration_body", [child1, p[2], child2, child3, child4, p[6], child5])
        # p[0] = VariableDeclaration(p[1], p[2])



def p_variable_declarators(p):
      '''variable_declarators : variable_declarator
                                | variable_declarators COMMA variable_declarator'''
      if len(p) == 2:
        p[0] = Node("variable_declarators", [p[1]])
      else:
        child1 = create_leaf("COMMA", p[2])
        p[0] = Node("variable_declarators", [p[1], child1, p[3]])
        # if len(p) == 2:
        #     p[0] = [p[1]]
        # else:
        #     p[0] = p[1] + [p[3]]

def p_variable_declarator(p):
      '''variable_declarator : variable_declarator_id'''
      p[0] = Node("variable_declarator", [p[1]])


def p_variable_declarator_id(p):
      '''variable_declarator_id : IDENTIFIER COLON primitive_type'''
      child1 = create_leaf("IDENTIFIER", p[1])
      child2 = create_leaf("COLON", p[2])
      p[0] = Node("variable_declarator_id", [child1, child2, p[3]])
      # p[0] = Variable(p[1], dimensions=p[2])


def p_statement(p):
        '''statement : normal_statement 
                     | if_then_statement
                     | if_then_else_statement
                     | while_statement
                     | do_while_statement'''
                     # | for_statement
        p[0] = Node("statement", [p[1]])
        # p[0] = p[1]


def p_normal_statement(p):
        '''normal_statement : block 
                             | expression_statement
                             | empty_statement
                             | return_statement'''
                             # | assert_statement
                             # | 
                             # | 
                             # | do_statement
                             # | break_statement
                             # | continue_statement
                             # | 
                             # | synchronized_statement
                             # | throw_statement
                             # | try_statement
                             # | try_statement_with_resources
        p[0] = Node("normal_statement", [p[1]])
        # p[0] = p[1]


def p_expression_statement(p):
        '''expression_statement : statement_expression STATE_END'''
                                # | explicit_constructor_invocation
        child1 = create_leaf("STATE_END", p[2])
        p[0] = Node("expression_statement", [p[1], child1])
        # if len(p) == 2:
        #     p[0] = p[1]
        # else:
        #     p[0] = ExpressionStatement(p[1])

def p_statement_expression(p):
        '''statement_expression : assignment
                                | method_invocation'''
        p[0] = Node("statement_expression", [p[1]])
                                # | class_instance_creation_expression
        # p[0] = p[1]

def p_if_then_statement(p):
        '''if_then_statement : KWRD_IF LPAREN expression RPAREN statement'''
        child1 = create_leaf("IF", p[1])
        child2 = create_leaf("LPAREN", p[2])
        child3 = create_leaf("RPAREN", p[4])
        p[0] = Node("if_then_statement", [child1, child2, p[3], child3, p[5]])
        # p[0] = IfThenElse(p[3], p[5])

def p_if_then_else_statement(p):
        '''if_then_else_statement : KWRD_IF LPAREN expression RPAREN if_then_else_intermediate KWRD_ELSE statement'''
        child1 = create_leaf("IF", p[1])
        child2 = create_leaf("LPAREN", p[2])
        child3 = create_leaf("RPAREN", p[4])
        child4 = create_leaf("ELSE", p[6])
        p[0] = Node("if_then_else_statement", [child1, child2, p[3], child3, p[5], child4, p[7]])
        # p[0] = IfThenElse(p[3], p[5], p[7])

def p_if_then_else_statement_precedence(p):
        '''if_then_else_statement_precedence : KWRD_IF LPAREN expression RPAREN if_then_else_intermediate KWRD_ELSE if_then_else_intermediate'''
        child1 = create_leaf("IF", p[1])
        child2 = create_leaf("LPAREN", p[2])
        child3 = create_leaf("RPAREN", p[4])
        child4 = create_leaf("ELSE", p[6])
        p[0] = Node("if_then_else_statement_precedence", [child1, child2, p[3], child3, p[5], child4, p[7]])
        # p[0] = IfThenElse(p[3], p[5], p[7])

def p_if_then_else_intermediate(p):
        '''if_then_else_intermediate : normal_statement
                                              | if_then_else_statement_precedence'''
        p[0] = Node("if_then_else_intermediate", [p[1]])
        # p[0] = IfThenElse(p[3], p[5], p[7])

def p_while_statement(p):
        '''while_statement : KWRD_WHILE LPAREN expression RPAREN statement'''
        child1 = create_leaf("WHILE", p[1])
        child2 = create_leaf("LPAREN", p[2])
        child3 = create_leaf("RPAREN", p[4])
        p[0] = Node("while_statement", [child1, child2, p[3], child3, p[5]])
        # p[0] = While(p[3], p[5])

def p_do_while_statement(p):
        '''do_while_statement : KWRD_DO statement KWRD_WHILE LPAREN expression RPAREN STATE_END '''
        child1 = create_leaf("DO", p[1])
        child2 = create_leaf("WHILE", p[3])
        child3 = create_leaf("LPAREN", p[4])
        child4 = create_leaf("RPAREN", p[6])
        child5 = create_leaf("STATE_END", p[7])
        p[0] = Node("do_while_statement", [child1, p[2], child2, child3, p[5], child4, child5])
        # p[0] = DoWhile(p[5], body=p[2])

def p_empty_statement(p):
        '''empty_statement : STATE_END '''
        child1 = create_leaf("STATE_END", p[1])
        p[0] = Node("empty_statement", [child1])
        # p[0] = Empty()

def p_return_statement(p):
        '''return_statement : KWRD_RETURN expression_optional STATE_END '''
        child1 = create_leaf("RETURN", p[1])
        child2 = create_leaf("STATE_END", p[3])
        p[0] = Node("return_statement", [child1, p[2], child2])
        # p[0] = Return(p[2])


# def p_class_declaration(p):
#         '''class_declaration : class_header class_body'''
#         # p[0] = ClassDeclaration(p[1]['name'], p[2], modifiers=p[1]['modifiers'],
#         #                         extends=p[1]['extends'], implements=p[1]['implements'],
#         #                         type_parameters=p[1]['type_parameters'])


# def p_class_header(p):
#         '''class_header : class_header_name class_header_extends_opt'''
#         # p[1]['extends'] = p[2]
#         # p[1]['implements'] = p[3]
#         # p[0] = p[1]


# def p_class_header_name(p):
#         '''class_header_name : empty  ''' # class_header_name1 type_parameters
#                              # | class_header_name1
#         # if len(p) == 2:
#         #     p[1]['type_parameters'] = []
#         # else:
#         #     p[1]['type_parameters'] = p[2]
#         # p[0] = p[1]
# def p_class_header_extends_opt(p):
#         '''class_header_extends_opt : empty  ''' 

# def p_class_body(p):
#         '''class_body : empty  ''' 



def p_modifier(p):
      '''modifier : KWRD_PROTECTED
                  | KWRD_PRIVATE'''
      child1 = create_leaf("modifier keyword", p[1])
      p[0] = Node("modifier", [child1])
        #  by default its public
        # p[0] = p[1]

def p_type(p):
        '''type : primitive_type '''
        p[0] = Node("type", [p[1]])
                # | reference_type
        # p[0] = p[1]

def p_primitive_type(p):
    '''primitive_type : TYPE_INT
                      | TYPE_FLOAT
                      | TYPE_CHAR
                      | TYPE_STRING
                      | TYPE_BOOLEAN'''
    child1 = create_leaf("TYPE", p[1])
    p[0] = Node("primitive_type", [child1])
        # p[0] = p[1]

# def p_reference_type(p):
#       '''reference_type : class_type
#                         | array_type'''
#       # p[0] = p[1]

# print statement
def p_printstatement_1(p):
    "print_st : IDENTIFIER LPAREN IDENTIFIER RPAREN "
    try:
        print(names[p[3]])
    except LookupError:
        print("Undefined name '%s'" % p[3])

def p_empty(p):
    'empty :'
    p[0] = Node("empty", [])
    pass

def p_error(p):
    print p
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")