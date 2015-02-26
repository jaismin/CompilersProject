#!/usr/bin/env python2

import ply.lex as lex
import ply.yacc as yacc
from .model import *

class ExpressionParser(object):

    def p_expression(self, p):
        '''expression : assignment_expression'''
        p[0] = p[1]


    def p_assignment_expression(self, p):
        '''assignment_expression : assignment'''
        p[0] = p[1]

    def p_assignment(self, p):
        '''assignment : postfix_expression assignment_operator assignment_expression'''
        p[0] = Assignment(p[2], p[1], p[3])

    def p_assignment_operator(self, p):
        '''assignment_operator : '='
                               | TIMES_ASSIGN
                               | DIVIDE_ASSIGN
                               | REMAINDER_ASSIGN
                               | PLUS_ASSIGN
                               | MINUS_ASSIGN'''
        p[0] = p[1]

    
    
    def p_postfix_expression(self, p):
        '''postfix_expression :  name
                              | post_increment_expression
                              | post_decrement_expression'''
        p[0] = p[1]


    def p_post_increment_expression(self, p):
        '''post_increment_expression : postfix_expression PLUSPLUS'''
        p[0] = Unary('x++', p[1])

    def p_post_decrement_expression(self, p):
        '''post_decrement_expression : postfix_expression MINUSMINUS'''
        p[0] = Unary('x--', p[1])

    def p_dims_opt(self, p):
        '''dims_opt : dims'''
        p[0] = p[1]

    def p_dims_opt2(self, p):
        '''dims_opt : empty'''
        p[0] = 0

    
    



class StatementParser(object):

    def p_block(self, p):
        '''block : '{' block_statements_opt '}' '''
        p[0] = Block(p[2])

    def p_block_statements_opt(self, p):
        '''block_statements_opt : block_statements'''
        p[0] = p[1]

    def p_block_statements_opt2(self, p):
        '''block_statements_opt : empty'''
        p[0] = []

    def p_block_statements(self, p):
        '''block_statements : block_statement
                            | block_statements block_statement'''
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[2]]

    def p_block_statement(self, p):
        '''block_statement : local_variable_declaration_statement
                           | statement
                           | class_declaration'''
        p[0] = p[1]

    def p_local_variable_declaration_statement(self, p):
        '''local_variable_declaration_statement : local_variable_declaration ';' '''
        p[0] = p[1]

    def p_local_variable_declaration(self, p):
        '''local_variable_declaration : type variable_declarators'''
        p[0] = VariableDeclaration(p[1], p[2])

    def p_variable_declarators(self, p):
        '''variable_declarators : variable_declarator
                                | variable_declarators ',' variable_declarator'''
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[3]]

    def p_variable_declarator(self, p):
        '''variable_declarator : variable_declarator_id
                               | variable_declarator_id '=' variable_initializer'''
        if len(p) == 2:
            p[0] = VariableDeclarator(p[1])
        else:
            p[0] = VariableDeclarator(p[1], initializer=p[3])

    def p_variable_declarator_id(self, p):
        '''variable_declarator_id : NAME dims_opt'''
        p[0] = Variable(p[1], dimensions=p[2])

    def p_variable_initializer(self, p):
        '''variable_initializer : expression
                                | array_initializer'''
        p[0] = p[1]

    def p_statement(self, p):
        '''statement : statement_without_trailing_substatement
                     | if_then_statement
                     | if_then_else_statement
                     | while_statement
                     | for_statement'''
        p[0] = p[1]

    def p_statement_without_trailing_substatement(self, p):
        '''statement_without_trailing_substatement : block
                                                   | expression_statement
                                                   | empty_statement
                                                   | switch_statement
                                                   | do_statement
                                                   | return_statement'''
        p[0] = p[1]

    def p_expression_statement(self, p):
        '''expression_statement : statement_expression ';' '''
        p[0] = p[1]

    def p_statement_expression(self, p):
        '''statement_expression : assignment
                                | pre_increment_expression
                                | pre_decrement_expression
                                | post_increment_expression
                                | post_decrement_expression
                                | method_invocation
                                | class_instance_creation_expression'''
        p[0] = p[1]


    def p_if_then_statement(self, p):
        '''if_then_statement : IF '(' expression ')' statement'''
        p[0] = IfThenElse(p[3], p[5])

    def p_if_then_else_statement(self, p):
        '''if_then_else_statement : IF '(' expression ')' statement_no_short_if ELSE statement'''
        p[0] = IfThenElse(p[3], p[5], p[7])

     def p_if_then_else_statement_no_short_if(self, p):
        '''if_then_else_statement_no_short_if : IF '(' expression ')' statement_no_short_if ELSE statement_no_short_if'''
        p[0] = IfThenElse(p[3], p[5], p[7])

    def p_while_statement(self, p):
        '''while_statement : WHILE '(' expression ')' statement'''
        p[0] = While(p[3], p[5])

    def p_while_statement_no_short_if(self, p):
        '''while_statement_no_short_if : WHILE '(' expression ')' statement_no_short_if'''
        p[0] = While(p[3], p[5])


    def p_for_statement(self, p):
        '''for_statement : FOR '(' for_init_opt ';' expression_opt ';' for_update_opt ')' statement'''
        p[0] = For(p[3], p[5], p[7], p[9])

    def p_for_statement_no_short_if(self, p):
        '''for_statement_no_short_if : FOR '(' for_init_opt ';' expression_opt ';' for_update_opt ')' statement_no_short_if'''
        p[0] = For(p[3], p[5], p[7], p[9])

    def p_method_invocation(self, p):
        '''method_invocation : NAME '(' argument_list_opt ')' '''
        p[0] = MethodInvocation(p[1], arguments=p[3])

     def p_empty_statement(self, p):
        '''empty_statement : ';' '''
        p[0] = Empty()

    def p_switch_statement(self, p):
        '''switch_statement : SWITCH '(' expression ')' switch_block'''
        p[0] = Switch(p[3], p[5])

    def p_do_statement(self, p):
        '''do_statement : DO statement WHILE '(' expression ')' ';' '''
        p[0] = DoWhile(p[5], body=p[2])

    def p_return_statement(self, p):
        '''return_statement : RETURN expression_opt ';' '''
        p[0] = Return(p[2])


     def p_statement_no_short_if(self, p):
        '''statement_no_short_if : statement_without_trailing_substatement
                                 | labeled_statement_no_short_if
                                 | if_then_else_statement_no_short_if
                                 | while_statement_no_short_if
                                 | for_statement_no_short_if'''
        p[0] = p[1]


    def p_for_init_opt(self, p):
        '''for_init_opt : for_init
                        | empty'''
        p[0] = p[1]

    def p_for_init(self, p):
        '''for_init : statement_expression_list
                    | local_variable_declaration'''
        p[0] = p[1]

    def p_statement_expression_list(self, p):
        '''statement_expression_list : statement_expression
                                     | statement_expression_list ',' statement_expression'''
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[3]]


    def p_expression_opt(self, p):
        '''expression_opt : expression
                          | empty'''
        p[0] = p[1]

    def p_for_update_opt(self, p):
        '''for_update_opt : for_update
                          | empty'''
        p[0] = p[1]

    def p_for_update(self, p):
        '''for_update : statement_expression_list'''
        p[0] = p[1]



    def p_comma_opt(self, p):
        '''comma_opt : ','
                     | empty'''
        # ignore

    def p_array_initializer(self, p):
        '''array_initializer : '{' comma_opt '}' '''
        p[0] = ArrayInitializer()

    def p_array_initializer2(self, p):
        '''array_initializer : '{' variable_initializers '}'
                             | '{' variable_initializers ',' '}' '''
        p[0] = ArrayInitializer(p[2])

    def p_variable_initializers(self, p):
        '''variable_initializers : variable_initializer
                                 | variable_initializers ',' variable_initializer'''
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[3]]

    def p_switch_block3(self, p):
        '''switch_block : '{' switch_label '}' '''
        p[0] = [SwitchCase(p[2])]

    def p_switch_label(self, p):
        '''switch_label : CASE constant_expression ':'
                        | DEFAULT ':' '''
        if len(p) == 3:
            p[0] = 'default'
        else:
            p[0] = p[2]


    def p_constant_expression(self, p):
        '''constant_expression : expression'''
        p[0] = p[1]

    
    
class NameParser(object):

    def p_name(self, p):
        '''name : simple_name'''
        p[0] = p[1]

    def p_simple_name(self, p):
        '''simple_name : NAME'''
        p[0] = Name(p[1])


class LiteralParser(object):

    def p_literal(self, p):
        '''literal : NUM
                   | CHAR_LITERAL
                   | STRING_LITERAL
                   | TRUE
                   | FALSE
                   | NULL'''
        p[0] = Literal(p[1])

class TypeParser(object):

    def p_type(self, p):
        '''type : primitive_type
                | reference_type'''
        p[0] = p[1]

    def p_primitive_type(self, p):
        '''primitive_type : BOOLEAN
                          | VOID
                          | BYTE
                          | SHORT
                          | INT
                          | LONG
                          | CHAR
                          | FLOAT
                          | DOUBLE'''
        p[0] = p[1]

    def p_reference_type(self, p):
        '''reference_type : array_type'''
        p[0] = p[1]


    def p_array_type(self, p):
        '''array_type : primitive_type dims'''
        p[0] = Type(p[1], dimensions=p[2])