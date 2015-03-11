# dictionary of names
names = {}

def p_program_structure(p):
    '''ProgramStructure : ProgramStructure  class_and_objects
                      | class_and_objects '''
    
def p_class_and_objects(p):
  '''class_and_objects : SingletonObject
                       | class_declaration'''

def p_SingletonObject(p):
    'SingletonObject : ObjectDeclare block'
   
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

def p_expression_optional(p):
        '''expression_optional : expression
                          | empty'''
        # p[0] = p[1]


def p_assignment_expression(p):
    '''assignment_expression : assignment
                             | conditional_or_expression'''
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
    '''unary_expression : PLUS unary_expression
                            | MINUS unary_expression
                            | unary_expression_not_plus_minus'''


def p_unary_expression_not_plus_minus(p):
    '''unary_expression_not_plus_minus : base_variable_set
                                           | TILDA unary_expression
                                           | NOT unary_expression
                                           | cast_expression'''
def p_base_variable_set(p):
  '''base_variable_set : variable_literal
                        | LPAREN expression RPAREN'''

def p_cast_expression(p):
        '''cast_expression : LPAREN primitive_type RPAREN unary_expression'''
        # p[0] = Cast(Type(p[2], dimensions=p[3]), p[5])

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
    '''int_float : FLOAT_CONST
                | INT_CONST'''


def p_method_invocation(p):
    '''method_invocation : name LPAREN argument_list_opt RPAREN '''
    # p[0] = MethodInvocation(p[3], target=p[1], arguments=p[5])

def p_array_access(p):
    '''array_access : name LBPAREN expression RBPAREN '''
        # p[0] = ArrayAccess(p[3], p[1])

def p_argument_list_opt(p):
    '''argument_list_opt : argument_list'''
        # p[0] = p[1]

def p_argument_list_opt2(p):
    '''argument_list_opt : empty'''
        # p[0] = []

def p_argument_list(p):
    '''argument_list : expression
                    | argument_list COMMA expression'''
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

def p_valid_variable(p):
    '''valid_variable : name
                      | array_access'''


def p_variableliteral(p):
    '''variable_literal : valid_variable
                        | primary'''



# BLOCK STATEMENTS


def p_block(p):
      '''block : BLOCK_BEGIN block_statements_opt BLOCK_END '''
      print '1'
        # p[0] = Block(p[2])

def p_block_statements_opt(p):
      '''block_statements_opt : block_statements'''
      print '2'
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
                           | class_declaration
                           | SingletonObject
                           | method_declaration'''
        # p[0] = p[1]

# var (a:Int)=(h);
# var (a:Int,b:Int,c:Int)=(1,2,3);
# var (a:Int)=(h)
# var (a:Int,b:Int,c:Int)=(1,2,3)
# supported

def p_modifier_opts(p):
  '''modifier_opts : modifier
                    | empty '''

def p_declaration_keyword(p):
  '''declaration_keyword : KWRD_VAR
                    | KWRD_VAL '''


def p_local_variable_declaration_statement(p):
      '''local_variable_declaration_statement : local_variable_declaration STATE_END '''
        # p[0] = p[1]

# 
def p_local_variable_declaration(p):
      '''local_variable_declaration : modifier_opts declaration_keyword variable_declaration_body'''
      # print 'Hello World'
        # p[0] = VariableDeclaration(p[1], p[2])

def p_variable_declaration_initializer(p):
  '''variable_declaration_initializer : expression
                                      | array_initializer
                                      | class_initializer'''

def p_variable_arguement_list(p):
  ''' variable_arguement_list : variable_declaration_initializer
                    | variable_arguement_list COMMA variable_declaration_initializer'''

def p_variable_declaration_body(p):
      '''variable_declaration_body : variable_declarator ASSIGN  variable_declaration_initializer 
                                    | LPAREN variable_declarators RPAREN ASSIGN LPAREN variable_arguement_list RPAREN'''
      # print 'Hello World'
        # p[0] = VariableDeclaration(p[1], p[2])



def p_variable_declarators(p):
      '''variable_declarators : variable_declarator
                                | variable_declarators COMMA variable_declarator'''
        # if len(p) == 2:
        #     p[0] = [p[1]]
        # else:
        #     p[0] = p[1] + [p[3]]

def p_variable_declarator(p):
      '''variable_declarator : variable_declarator_id'''


def p_variable_declarator_id(p):
      '''variable_declarator_id : IDENTIFIER COLON type'''
      # p[0] = Variable(p[1], dimensions=p[2])


def p_statement(p):
        '''statement : normal_statement 
                     | if_then_statement
                     | if_then_else_statement
                     | while_statement
                     | do_while_statement'''
                     # | for_statement
        # p[0] = p[1]


def p_normal_statement(p):
        '''normal_statement : block 
                             | expression_statement
                             | empty_statement
                             | return_statement
                             | switch_statement'''
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
        # p[0] = p[1]


def p_expression_statement(p):
        '''expression_statement : statement_expression STATE_END'''
                                # | explicit_constructor_invocation
        # if len(p) == 2:
        #     p[0] = p[1]
        # else:
        #     p[0] = ExpressionStatement(p[1])

def p_statement_expression(p):
        '''statement_expression : assignment
                                | method_invocation'''
                                # | class_instance_creation_expression
        # p[0] = p[1]

def p_if_then_statement(p):
        '''if_then_statement : KWRD_IF LPAREN expression RPAREN statement'''
        # p[0] = IfThenElse(p[3], p[5])

def p_if_then_else_statement(p):
        '''if_then_else_statement : KWRD_IF LPAREN expression RPAREN if_then_else_intermediate KWRD_ELSE statement'''
        # p[0] = IfThenElse(p[3], p[5], p[7])

def p_if_then_else_statement_precedence(p):
        '''if_then_else_statement_precedence : KWRD_IF LPAREN expression RPAREN if_then_else_intermediate KWRD_ELSE if_then_else_intermediate'''
        # p[0] = IfThenElse(p[3], p[5], p[7])

def p_if_then_else_intermediate(p):
        '''if_then_else_intermediate : normal_statement
                                              | if_then_else_statement_precedence'''
        # p[0] = IfThenElse(p[3], p[5], p[7])

def p_while_statement(p):
        '''while_statement : KWRD_WHILE LPAREN expression RPAREN statement'''
        # p[0] = While(p[3], p[5])

def p_do_while_statement(p):
        '''do_while_statement : KWRD_DO statement KWRD_WHILE LPAREN expression RPAREN STATE_END '''
        # p[0] = DoWhile(p[5], body=p[2])


def p_switch_statement( p):
        '''switch_statement : expression KWRD_MATCH switch_block '''
        # p[0] = Switch(p[3], p[5])

def p_switch_block(p):
        '''switch_block : BLOCK_BEGIN BLOCK_END '''
        # p[0] = []

def p_switch_block2(p):
        '''switch_block : BLOCK_BEGIN switch_block_statements BLOCK_END '''
        # p[0] = p[2]

def p_switch_block3(p):
        '''switch_block : BLOCK_BEGIN switch_labels BLOCK_END '''
        # p[0] = [SwitchCase(p[2])]

def p_switch_block4(p):
        '''switch_block : BLOCK_BEGIN switch_block_statements switch_labels BLOCK_END '''
        # p[0] = p[2] + [SwitchCase(p[3])]

def p_switch_block_statements(p):
        '''switch_block_statements : switch_block_statement
                                   | switch_block_statements switch_block_statement'''
        # if len(p) == 2:
        #     p[0] = [p[1]]
        # else:
        #     p[0] = p[1] + [p[2]]

def p_switch_block_statement(p):
        '''switch_block_statement : switch_labels block_statements'''
        # p[0] = SwitchCase(p[1], body=p[2])

def p_switch_labels(p):
        '''switch_labels : switch_label
                         | switch_labels switch_label'''
        # if len(p) == 2:
        #     p[0] = [p[1]]
        # else:
        #     p[0] = p[1] + [p[2]]

def p_switch_label(p):
        '''switch_label : KWRD_CASE expression FUNTYPE '''
        # if len(p) == 3:
        #     p[0] = 'default'
        # else:
        #     p[0] = p[2]



def p_empty_statement(p):
        '''empty_statement : STATE_END '''
        # p[0] = Empty()

def p_return_statement(p):
        '''return_statement : KWRD_RETURN expression_optional STATE_END '''
        # p[0] = Return(p[2])


def p_constructor_arguement_list_opt(p):
  '''constructor_arguement_list_opt : constructor_arguement_list
                            | empty '''
                            # | variable_declarators COMMA variable_declarator
        # if len(p) == 2:
        #     p[0] = [p[1]]
        # else:
        #     p[0] = p[1] + [p[3]]
def p_constructor_arguement_list(p):
  '''constructor_arguement_list : constructor_arguement_list_declarator
                         | constructor_arguement_list COMMA constructor_arguement_list_declarator'''
                  
def p_constructor_arguement_list_declarator(p):
    '''constructor_arguement_list_declarator : declaration_keyword IDENTIFIER COLON type'''
      

def p_func_arguement_list_opt(p):
  '''func_arguement_list_opt : variable_declarators
                            | empty '''

def p_class_declaration(p):
        '''class_declaration : class_header class_body'''
        # p[0] = ClassDeclaration(p[1]['name'], p[2], modifiers=p[1]['modifiers'],
        #                         extends=p[1]['extends'], implements=p[1]['implements'],
        #                         type_parameters=p[1]['type_parameters'])


def p_class_header(p):
        '''class_header : class_header_name class_header_extends_opt'''
        # p[1]['extends'] = p[2]
        # p[1]['implements'] = p[3]
        # p[0] = p[1]


def p_class_header_name(p):
        '''class_header_name : class_header_name1 LPAREN constructor_arguement_list_opt RPAREN''' # class_header_name1 type_parameters
                             # | class_header_name1
        # if len(p) == 2:
        #     p[1]['type_parameters'] = []
        # else:
        #     p[1]['type_parameters'] = p[2]
        # p[0] = p[1]

def p_class_header_name1(p):
        '''class_header_name1 : modifier_opts KWRD_CLASS name'''
        # p[0] = {'modifiers': p[1], 'name': p[3]}

def p_class_header_extends_opt(p):
        '''class_header_extends_opt : class_header_extends
                                    | empty'''
        # p[0] = p[1]


def p_class_header_extends(p):
        '''class_header_extends : KWRD_EXTNDS name LPAREN func_arguement_list_opt RPAREN'''
        # p[0] = p[2]



def p_class_body(p):
        '''class_body : block ''' 



def p_method_declaration(p):
        '''method_declaration : method_header method_body'''
        # if len(p) == 2:
        #     p[0] = p[1]
        # else:
        #     p[0] = MethodDeclaration(p[1]['name'], parameters=p[1]['parameters'],
        #                              extended_dims=p[1]['extended_dims'], type_parameters=p[1]['type_parameters'],
        #                              return_type=p[1]['type'], modifiers=p[1]['modifiers'],
        #                              throws=p[1]['throws'], body=p[2])


def p_method_header(p):
        '''method_header : method_header_name LPAREN func_arguement_list_opt RPAREN COLON method_return_type ASSIGN'''
        # p[1]['extends'] = p[2]
        # p[1]['implements'] = p[3]
        # p[0] = p[1]

def p_method_return_type(p):
        '''method_return_type : type 
                              | TYPE_VOID'''
def p_method_header_name(p):
        '''method_header_name : modifier_opts KWRD_DEF IDENTIFIER''' # class_header_name1 type_parameters
                             # | class_header_name1
        # if len(p) == 2:
        #     p[1]['type_parameters'] = []
        # else:
        #     p[1]['type_parameters'] = p[2]
        # p[0] = p[1]

def p_method_body(p):
        '''method_body : block ''' 


def p_modifier(p):
      '''modifier : KWRD_PROTECTED
                  | KWRD_PRIVATE'''

        #  by default its public
        # p[0] = p[1]

def p_type(p):
        '''type : primitive_type 
                | reference_type '''
        # p[0] = p[1]

def p_primitive_type(p):
    '''primitive_type : TYPE_INT
                      | TYPE_FLOAT
                      | TYPE_CHAR
                      | TYPE_STRING
                      | TYPE_BOOLEAN'''
        # p[0] = p[1]

def p_reference_type(p):
      '''reference_type : class_data_type
                        | array_data_type'''
      # p[0] = p[1]

def p_class_data_type(p):
      '''class_data_type : name'''

def p_array_data_type(p):
      '''array_data_type : KWRD_ARRAY LBPAREN type RBPAREN'''

def p_array_initializer(p):
  ''' array_initializer : KWRD_NEW KWRD_ARRAY LBPAREN type RBPAREN LPAREN INT_CONST RPAREN
                        | KWRD_ARRAY LPAREN argument_list_opt RPAREN '''

def p_class_initializer(p):
  ''' class_initializer : KWRD_NEW name LPAREN argument_list_opt RPAREN ''' 

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
    print p
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")