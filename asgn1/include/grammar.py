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
    '''ProgramStructure : ProgramStructure  class_and_objects
                      | class_and_objects '''
    if len(p) == 3:
      p[0] = Node("ProgramStructure", [p[1], p[2]])
    else:
      p[0] = Node("ProgramStructure", [p[1]])
    
def p_class_and_objects(p):
  '''class_and_objects : SingletonObject
                       | class_declaration'''
  p[0] = Node("class_and_objects", [p[1]])

def p_SingletonObject(p):
    'SingletonObject : ObjectDeclare block'
    p[0] = Node("SingletonObject", [p[1], p[2]])
   
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

def p_expression_optional(p):
        '''expression_optional : expression
                          | empty'''
        p[0] = Node("expression_optional", [p[1]])

def p_assignment_expression(p):
    '''assignment_expression : assignment
                             | conditional_or_expression'''
    p[0] = Node("assignment_expression", [p[1]])

# assignment

def p_assignment(p):
    '''assignment : valid_variable assignment_operator assignment_expression'''
    p[0] = Node("assignment", [p[1], p[2], p[3]])


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

def p_inclusive_or_expression(p):
    '''inclusive_or_expression : exclusive_or_expression
                                   | inclusive_or_expression OR_BITWISE exclusive_or_expression'''
    if len(p) == 2:
      p[0] = Node("inclusive_or_expression", [p[1]])
    else:
      child1 = create_leaf("OR_BITWISE", p[2])
      p[0] = Node("inclusive_or_expression", [p[1], child1, p[3]])

def p_exclusive_or_expression(p):
    '''exclusive_or_expression : and_expression
                                   | exclusive_or_expression XOR and_expression'''
    if len(p) == 2:
      p[0] = Node("exclusive_or_expression", [p[1]])
    else:
      child1 = create_leaf("XOR", p[2])
      p[0] = Node("exclusive_or_expression", [p[1], child1, p[3]])

def p_and_expression(p):
    '''and_expression : equality_expression
                          | and_expression AND_BITWISE equality_expression'''
    if len(p) == 2:
      p[0] = Node("and_expression", [p[1]])
    else:
      child1 = create_leaf("AND_BITWISE", p[2])
      p[0] = Node("and_expression", [p[1], child1, p[3]])

def p_equality_expression(p):
    '''equality_expression : relational_expression
                            | equality_expression EQUAL relational_expression
                            | equality_expression NEQUAL relational_expression'''
    if len(p) == 2:
      p[0] = Node("relational_expression", [p[1]])
    else:
      child1 = create_leaf("EqualityOp", p[2])
      p[0] = Node("relational_expression", [p[1], child1, p[3]])
   

def p_relational_expression(p):
    '''relational_expression : shift_expression
                                 | relational_expression GREATER shift_expression
                                 | relational_expression LESS shift_expression
                                 | relational_expression GEQ shift_expression
                                 | relational_expression LEQ shift_expression'''
    if len(p) == 2:
      p[0] = Node("relational_expression", [p[1]])
    else:
      child1 = create_leaf("RelationalOp", p[2])
      p[0] = Node("relational_expression", [p[1], child1, p[3]])
   

def p_shift_expression(p):
        '''shift_expression : additive_expression
                            | shift_expression LSHIFT additive_expression
                            | shift_expression RSHIFT additive_expression'''
        if len(p) == 2:
          p[0] = Node("shift_expression", [p[1]])
        else:
          child1 = create_leaf("ShiftOp", p[2])
          p[0] = Node("shift_expression", [p[1], child1, p[3]])
       

def p_additive_expression(p):
    '''additive_expression : multiplicative_expression
                               | additive_expression PLUS multiplicative_expression
                               | additive_expression MINUS multiplicative_expression'''
    if len(p) == 2:
      p[0] = Node("additive_expression", [p[1]])
    else:
      child1 = create_leaf("AddOp", p[2])
      p[0] = Node("additive_expression", [p[1], child1, p[3]])
   

def p_multiplicative_expression(p):
    '''multiplicative_expression : unary_expression
                                     | multiplicative_expression TIMES unary_expression
                                     | multiplicative_expression DIVIDE unary_expression
                                     | multiplicative_expression REMAINDER unary_expression'''
    if len(p) == 2:
      p[0] = Node("multiplicative_expression", [p[1]])
    else:
      child1 = create_leaf("MultOp", p[2])
      p[0] = Node("multiplicative_expression", [p[1], child1, p[3]])
    

def p_unary_expression(p):
    '''unary_expression : PLUS unary_expression
                            | MINUS unary_expression
                            | unary_expression_not_plus_minus'''
    if len(p) == 3:
      child1 = create_leaf("UnaryOp", p[1])
      p[0] = Node("unary_expression", [child1, p[2]])
    else:
      p[0] = Node("unary_expression", [p[1]])


def p_unary_expression_not_plus_minus(p):
    '''unary_expression_not_plus_minus : base_variable_set
                                           | TILDA unary_expression
                                           | NOT unary_expression
                                           | cast_expression'''
    if len(p) == 2:
      p[0] = Node("unary_expression_not_plus_minus", [p[1]])
    else:
      child1 = create_leaf("Unary_1Op", p[1])
      p[0] = Node("unary_expression_not_plus_minus", [child1, p[2]])
    

def p_base_variable_set(p):
  '''base_variable_set : variable_literal
                        | LPAREN expression RPAREN'''
  if len(p) == 2:
    p[0] = Node("base_variable_set", [p[1]])
  else:
    child1 = create_leaf("LPAREN", p[1])
    child2 = create_leaf("RPAREN", p[3])
    p[0] = Node("base_variable_set", [child1, p[2], child2])


def p_cast_expression(p):
        '''cast_expression : LPAREN primitive_type RPAREN unary_expression'''
        child1 = create_leaf("LPAREN", p[1])
        child2 = create_leaf("RPAREN", p[3])
        p[0] = Node("cast_expression", [child1, p[2], child2, p[4]])
       

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
    if type(p[1]) == type("sample-string"):    # here
      child1 = create_leaf("LiteralConst", p[1])
      p[0] = Node("literal", [child1])
    else:
      p[0] = Node("literal", [p[1]])


def p_int_float(p):
    '''int_float : FLOAT_CONST
                | INT_CONST'''
    child1 = create_leaf("IntFloatConst", p[1])
    p[0] = Node("int_float", [child1])


def p_method_invocation(p):
    '''method_invocation : name LPAREN argument_list_opt RPAREN '''
    child1 = create_leaf("LPAREN", p[2])
    child2 = create_leaf("RPAREN", p[4])
    p[0] = Node("method_invocation", [p[1], child1, p[3], child2])

def p_array_access(p):
    '''array_access : name LBPAREN expression RBPAREN '''
    child1 = create_leaf("LBPAREN", p[2])
    child2 = create_leaf("RBPAREN", p[4])
    p[0] = Node("array_access", [p[1], child1, p[3], child2])   


def p_argument_list_opt(p):
    '''argument_list_opt : argument_list'''
    p[0] = Node("argument_list_opt", [p[1]])


def p_argument_list_opt2(p):
    '''argument_list_opt : empty'''
    p[0] = Node("argument_list_opt", [p[1]])
        

def p_argument_list(p):
    '''argument_list : expression
                    | argument_list COMMA expression'''
    if len(p) == 2:
      p[0] = Node("argument_list", [p[1]])
    else:
      child1 = create_leaf("COMMA", p[2])
      p[0] = Node("argument_list", [p[1], child1, p[3]])
    



# object identifier and identifier names for left hand assignment

def p_name(p):
    '''name : simple_name
            | qualified_name'''
    p[0] = Node("name", [p[1]])
    

def p_simple_name(p):
    '''simple_name : IDENTIFIER'''
    child1 = create_leaf("IDENTIFIER", p[1])
    p[0] = Node("simple_name", [child1])
    

def p_qualified_name(p):
    '''qualified_name : name DOT simple_name'''
    child1 = create_leaf("DOT", p[2])
    p[0] = Node("qualified_name", [p[1], child1, p[3]])
   

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
      

def p_block_statement(p):
      '''block_statement : local_variable_declaration_statement
                           | statement
                           | class_declaration
                           | SingletonObject
                           | method_declaration'''
      p[0] = Node("block_statement", [p[1]])

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

# 
def p_local_variable_declaration(p):
      '''local_variable_declaration : modifier_opts declaration_keyword variable_declaration_body'''
      p[0] = Node("local_variable_declaration", [p[1], p[2], p[3]])
     

def p_variable_declaration_initializer(p):
  '''variable_declaration_initializer : expression
                                      | array_initializer
                                      | class_initializer'''
  p[0] = Node("variable_declaration_initializer", [p[1]])

def p_variable_arguement_list(p):
  ''' variable_arguement_list : variable_declaration_initializer
                    | variable_arguement_list COMMA variable_declaration_initializer'''
  if len(p) == 2:
    p[0] = Node("variable_arguement_list", [p[1]])
  else:
    child1 = create_leaf("COMMA", p[2])
    p[0] = Node("variable_arguement_list", [p[1], child1, p[3]])

def p_variable_declaration_body(p):
      '''variable_declaration_body : variable_declarator ASSIGN  variable_declaration_initializer 
                                    | LPAREN variable_declarators RPAREN ASSIGN LPAREN variable_arguement_list RPAREN'''
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
 
def p_variable_declaration_body1(p):
  ''' variable_declaration_body : IDENTIFIER ASSIGN LPAREN func_arguement_list_opt RPAREN FUNTYPE expression'''      
  
  child1 = create_leaf("IDENTIFIER", p[1])
  child2 = create_leaf("ASSIGN", p[2])
  child3 = create_leaf("LPAREN", p[3])
  child4 = create_leaf("RPAREN", p[5])
  child5 = create_leaf("FUNTYPE", p[6])
  p[0] = Node("variable_declaration_body", [child1, child2, child3, p[4], child4, child5,p[7]])
def p_variable_declarators(p):
      '''variable_declarators : variable_declarator
                                | variable_declarators COMMA variable_declarator'''
      if len(p) == 2:
        p[0] = Node("variable_declarators", [p[1]])
      else:
        child1 = create_leaf("COMMA", p[2])
        p[0] = Node("variable_declarators", [p[1], child1, p[3]])
  

def p_variable_declarator(p):
      '''variable_declarator : variable_declarator_id'''
      p[0] = Node("variable_declarator", [p[1]])


def p_variable_declarator_id(p):
      '''variable_declarator_id : IDENTIFIER COLON type'''
      child1 = create_leaf("IDENTIFIER", p[1])
      child2 = create_leaf("COLON", p[2])
      p[0] = Node("variable_declarator_id", [child1, child2, p[3]])
      # p[0] = Variable(p[1], dimensions=p[2])


def p_statement(p):
        '''statement : normal_statement 
                     | if_then_statement
                     | if_then_else_statement
                     | while_statement
                     | do_while_statement
                     | for_statement'''
        p[0] = Node("statement", [p[1]])


def p_normal_statement(p):
        '''normal_statement : block 
                             | expression_statement
                             | empty_statement
                             | return_statement
                             | switch_statement'''
 
        p[0] = Node("normal_statement", [p[1]])
 


def p_expression_statement(p):
        '''expression_statement : statement_expression STATE_END'''
        child1 = create_leaf("STATE_END", p[2])
        p[0] = Node("expression_statement", [p[1], child1])
                               

def p_statement_expression(p):
        '''statement_expression : assignment
                                | method_invocation'''
            
        p[0] = Node("statement_expression", [p[1]])
    

def p_if_then_statement(p):
        '''if_then_statement : KWRD_IF LPAREN expression RPAREN statement'''
        child1 = create_leaf("IF", p[1])
        child2 = create_leaf("LPAREN", p[2])
        child3 = create_leaf("RPAREN", p[4])
        p[0] = Node("if_then_statement", [child1, child2, p[3], child3, p[5]])
        

def p_if_then_else_statement(p):
        '''if_then_else_statement : KWRD_IF LPAREN expression RPAREN if_then_else_intermediate KWRD_ELSE statement'''
        child1 = create_leaf("IF", p[1])
        child2 = create_leaf("LPAREN", p[2])
        child3 = create_leaf("RPAREN", p[4])
        child4 = create_leaf("ELSE", p[6])
        p[0] = Node("if_then_else_statement", [child1, child2, p[3], child3, p[5], child4, p[7]])
       

def p_if_then_else_statement_precedence(p):
        '''if_then_else_statement_precedence : KWRD_IF LPAREN expression RPAREN if_then_else_intermediate KWRD_ELSE if_then_else_intermediate'''
        child1 = create_leaf("IF", p[1])
        child2 = create_leaf("LPAREN", p[2])
        child3 = create_leaf("RPAREN", p[4])
        child4 = create_leaf("ELSE", p[6])
        p[0] = Node("if_then_else_statement_precedence", [child1, child2, p[3], child3, p[5], child4, p[7]])
      

def p_if_then_else_intermediate(p):
        '''if_then_else_intermediate : normal_statement
                                              | if_then_else_statement_precedence'''
        p[0] = Node("if_then_else_intermediate", [p[1]])
       

def p_while_statement(p):
        '''while_statement : KWRD_WHILE LPAREN expression RPAREN statement'''
        child1 = create_leaf("WHILE", p[1])
        child2 = create_leaf("LPAREN", p[2])
        child3 = create_leaf("RPAREN", p[4])
        p[0] = Node("while_statement", [child1, child2, p[3], child3, p[5]])
        

def p_do_while_statement(p):
        '''do_while_statement : KWRD_DO statement KWRD_WHILE LPAREN expression RPAREN STATE_END '''
        child1 = create_leaf("DO", p[1])
        child2 = create_leaf("WHILE", p[3])
        child3 = create_leaf("LPAREN", p[4])
        child4 = create_leaf("RPAREN", p[6])
        child5 = create_leaf("STATE_END", p[7])
        p[0] = Node("do_while_statement", [child1, p[2], child2, child3, p[5], child4, child5])
       

def p_for_statement(p):
  '''for_statement : KWRD_FOR LPAREN for_logic RPAREN statement'''
  child1 = create_leaf ("FOR",p[1])
  child2 = create_leaf ("LPAREN",p[2])
  child3 = create_leaf ("RPAREN",p[4])
  p[0] = Node("for_statement",[child1,child2,p[3],child3,p[5]])


def p_for_logic(p):
    ''' for_logic : for_update 
                  | for_update STATE_END for_logic '''
    if len(p)==2:
      p[0]=Node("for_logic",[p[1]])
    else:
      child1 = create_leaf("STATE_END",p[2])
      p[0] = Node("for_logic",[p[1],child1,p[3]])

def p_for_update(p):
  ''' for_update : for_loop for_step_opts '''
  p[0]=Node("for_update",[p[1],p[2]])

def p_for_loop(p):
  ''' for_loop : IDENTIFIER CHOOSE expression for_untilTo expression '''
  
  child1 = create_leaf("IDENTIFIER",p[1])
  child2 = create_leaf("CHOOSE",p[2])
  p[0] = Node("for_loop_st",[child1,child2,p[3],p[4],p[5]])

def p_for_untilTo(p):
  '''for_untilTo : KWRD_UNTIL 
                  | KWRD_TO'''

  child1 = create_leaf("UNTIL_TO",p[1])
  p[0]=Node("for_untilTo",[child1])


def p_for_step_opts(p):
  ''' for_step_opts : KWRD_BY expression
                    | empty'''
  if len(p)==2:
    p[0]=Node("for_step_opts",[p[1]])
  else :
    child1 = create_leaf("BY",p[1])
    p[0]=Node("for_step_opts",[child1,p[2]])

               
def p_switch_statement( p):
        '''switch_statement : expression KWRD_MATCH switch_block '''
        child1 = create_leaf("MATCH", p[2])
        p[0] = Node("switch_statement", [p[1], child1, p[3]])
        

def p_switch_block(p):
        '''switch_block : BLOCK_BEGIN BLOCK_END '''
        child1 = create_leaf("BLOCK_BEGIN", p[1])
        child2 = create_leaf("BLOCK_END", p[2])
        p[0] = Node("switch_block", [child1, child2])
       

def p_switch_block2(p):
        '''switch_block : BLOCK_BEGIN switch_block_statements BLOCK_END '''
        child1 = create_leaf("BLOCK_BEGIN", p[1])
        child2 = create_leaf("BLOCK_END", p[3])
        p[0] = Node("switch_block", [child1, p[2], child2])
       

def p_switch_block3(p):
        '''switch_block : BLOCK_BEGIN switch_labels BLOCK_END '''
        child1 = create_leaf("BLOCK_BEGIN", p[1])
        child2 = create_leaf("BLOCK_END", p[3])
        p[0] = Node("switch_block", [child1, p[2], child2])
      

def p_switch_block4(p):
        '''switch_block : BLOCK_BEGIN switch_block_statements switch_labels BLOCK_END '''
        child1 = create_leaf("BLOCK_BEGIN", p[1])
        child2 = create_leaf("BLOCK_END", p[4])
        p[0] = Node("switch_block", [child1, p[2], p[3], child2])
       

def p_switch_block_statements(p):
        '''switch_block_statements : switch_block_statement
                                   | switch_block_statements switch_block_statement'''
        if len(p) == 2:
          p[0] = Node("switch_block_statements", [p[1]])
        else:
          p[0] = Node("switch_block_statements", [p[1], p[2]])
    

def p_switch_block_statement(p):
        '''switch_block_statement : switch_labels block_statements'''
        p[0] = Node("switch_block_statement", [p[1], p[2]])
       

def p_switch_labels(p):
        '''switch_labels : switch_label
                         | switch_labels switch_label'''
        if len(p) == 2:
          p[0] = Node("switch_labels", [p[1]])
        else:
          p[0] = Node("switch_labels", [p[1], p[2]])
       

def p_switch_label(p):
        '''switch_label : KWRD_CASE expression FUNTYPE '''
        child1 = create_leaf("CASE", p[1])
        child2 = create_leaf("FUNTYPE", p[3])
        p[0] = Node("switch_label", [child1, p[2], child2])
      


def p_empty_statement(p):
        '''empty_statement : STATE_END '''
        child1 = create_leaf("STATE_END", p[1])
        p[0] = Node("empty_statement", [child1])
    
def p_return_statement(p):
        '''return_statement : KWRD_RETURN expression_optional STATE_END '''
        child1 = create_leaf("RETURN", p[1])
        child2 = create_leaf("STATE_END", p[3])
        p[0] = Node("return_statement", [child1, p[2], child2])
      


def p_constructor_arguement_list_opt(p):
  '''constructor_arguement_list_opt : constructor_arguement_list
                            | empty '''
  p[0] = Node("constructor_arguement_list_opt", [p[1]])
        

def p_constructor_arguement_list(p):
  '''constructor_arguement_list : constructor_arguement_list_declarator
                         | constructor_arguement_list COMMA constructor_arguement_list_declarator'''
  if len(p) == 2:
    p[0] = Node("constructor_arguement_list", [p[1]])
  else:
    child1 = create_leaf("COMMA", p[2])
    p[0] = Node("constructor_arguement_list", [p[1], child1, p[3]])


def p_constructor_arguement_list_declarator(p):
    '''constructor_arguement_list_declarator : declaration_keyword IDENTIFIER COLON type'''
    child1 = create_leaf("IDENTIFIER", p[2])
    child2 = create_leaf("COLON", p[3])
    p[0] = Node("constructor_arguement_list_declarator", [p[1], child1, child2, p[4]]) 


def p_func_arguement_list_opt(p):
  '''func_arguement_list_opt : variable_declarators
                            | empty '''
  p[0] = Node("func_arguement_list_opt", [p[1]])                       

def p_class_declaration(p):
        '''class_declaration : class_header class_body'''
        p[0] = Node("class_declaration", [p[1], p[2]])
       


def p_class_header(p):
        '''class_header : class_header_name class_header_extends_opt'''
        p[0] = Node("class_header", [p[1], p[2]])
       

def p_class_header_name(p):
        '''class_header_name : class_header_name1 LPAREN constructor_arguement_list_opt RPAREN''' # class_header_name1 type_parameters
                             # | class_header_name1
        child1 = create_leaf("LPAREN", p[2])
        child2 = create_leaf("RPAREN", p[4])
        p[0] = Node("class_header_name", [p[1], child1, p[3], child2])
       

def p_class_header_name1(p):
        '''class_header_name1 : modifier_opts KWRD_CLASS name'''
        child1 = create_leaf("CLASS", p[2])
        p[0] = Node("class_header_name1", [p[1], child1, p[3]])
       

def p_class_header_extends_opt(p):
        '''class_header_extends_opt : class_header_extends
                                    | empty'''
        p[0] = Node("class_header_extends_opt", [p[1]])


def p_class_header_extends(p):
        '''class_header_extends : KWRD_EXTNDS name LPAREN func_arguement_list_opt RPAREN'''
        child1 = create_leaf("EXTENDS", p[1])
        child2 = create_leaf("LPAREN", p[3])
        child3 = create_leaf("RPAREN", p[5])
        p[0] = Node("class_header_extends", [child1, p[2], child2, p[4], child3])


def p_class_body(p):
        '''class_body : block ''' 
        p[0] = Node("class_body", [p[1]])


def p_method_declaration(p):
        '''method_declaration : method_header method_body'''
        p[0] = Node("method_declaration", [p[1], p[2]])


def p_method_header(p):
        '''method_header : method_header_name LPAREN func_arguement_list_opt RPAREN COLON method_return_type ASSIGN'''
        child1 = create_leaf("LPAREN", p[2])
        child2 = create_leaf("RPAREN", p[4])
        child3 = create_leaf("COLON", p[5])
        child4 = create_leaf("ASSIGN", p[7])
        p[0] = Node("method_header", [p[1], child1, p[3], child2, child3, p[6], child4])


def p_method_return_type(p):
        '''method_return_type : type''' 
        p[0] = Node("method_return_type", [p[1]])

def p_method_return_type1(p):
        '''method_return_type : TYPE_VOID'''
        child1 = create_leaf("VOID", p[1])
        p[0] = Node("method_return_type", [child1])

def p_method_header_name(p):
        '''method_header_name : modifier_opts KWRD_DEF IDENTIFIER''' # class_header_name1 type_parameters
                             # | class_header_name1
        child1 = create_leaf("DEF", p[2])
        child2 = create_leaf("IDENTIFIER", p[3])
        p[0] = Node("method_header_name", [p[1], child1, child2])


def p_method_body(p):
        '''method_body : block ''' 
        p[0] = Node("method_body", [p[1]])

def p_modifier(p):
      '''modifier : KWRD_PROTECTED
                  | KWRD_PRIVATE'''
      child1 = create_leaf("ModifierKeyword", p[1])
      p[0] = Node("modifier", [child1])


def p_type(p):
        '''type : primitive_type 
                | reference_type '''
        p[0] = Node("type", [p[1]])
        # p[0] = p[1]

def p_primitive_type(p):
    '''primitive_type : TYPE_INT
                      | TYPE_FLOAT
                      | TYPE_CHAR
                      | TYPE_STRING
                      | TYPE_BOOLEAN'''
    child1 = create_leaf("TYPE", p[1])
    p[0] = Node("primitive_type", [child1]) 


def p_reference_type(p):
      '''reference_type : class_data_type
                        | array_data_type'''
      p[0] = Node("reference_type", [p[1]])

def p_class_data_type(p):
      '''class_data_type : name'''
      p[0] = Node("class_data_type", [p[1]])

def p_array_data_type(p):
      '''array_data_type : KWRD_ARRAY LBPAREN type RBPAREN'''
      child1 = create_leaf("ARRAY", p[1])
      child2 = create_leaf("LBPAREN", p[2])
      child3 = create_leaf("RBPAREN", p[4])
      p[0] = Node("array_data_type", [child1, child2, p[3], child3])

def p_array_initializer(p):
  ''' array_initializer : KWRD_NEW KWRD_ARRAY LBPAREN type RBPAREN LPAREN INT_CONST RPAREN
                        | KWRD_ARRAY LPAREN argument_list_opt RPAREN '''
  if len(p) == 9:
    child1 = create_leaf("NEW", p[1])
    child2 = create_leaf("ARRAY", p[2])
    child3 = create_leaf("LBPAREN", p[3])
    child4 = create_leaf("RBPAREN", p[5])
    child5 = create_leaf("LPAREN", p[6])
    child6 = create_leaf("INT_CONST", p[7])
    child7 = create_leaf("RPAREN", p[8])
    p[0] = Node("array_initializer", [child1, child2, child3, p[4], child4, child5, child6, child7])
  else:
    child1 = create_leaf("ARRAY", p[1])
    child2 = create_leaf("LPAREN", p[2])
    child3 = create_leaf("RPAREN", p[4]) 
    p[0] = Node("array_initializer", [child1, child2, p[3], child3])   

def p_class_initializer(p):
  ''' class_initializer : KWRD_NEW name LPAREN argument_list_opt RPAREN ''' 
  child1 = create_leaf("NEW", p[1])
  child2 = create_leaf("LPAREN", p[3])
  child3 = create_leaf("RPAREN", p[5])
  p[0] = Node("class_initializer", [child1, p[2], child2, p[4], child3])

# print statement
# def p_printstatement_1(p):
#     "print_st : IDENTIFIER LPAREN IDENTIFIER RPAREN "
#     try:
#         print(names[p[3]])
#     except LookupError:
#         print("Undefined name '%s'" % p[3])

def p_empty(p):
    'empty :'
    child1 = create_leaf("Empty", "NOP")
    p[0] = Node("empty", [child1])
    pass
