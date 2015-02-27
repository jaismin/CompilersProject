
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = 'n3\x1d2\xd5\xb8\xba\xbc\xcf\xec\x8bH\xb3N\x94{'
    
_lr_action_items = {'STATE_END':([8,10,13,22,23,24,28,29,30,31,34,35,47,49,51,52,53,54,56,],[-8,-6,19,-7,-5,-26,37,-27,-19,44,-27,-24,-25,-18,-20,-23,-21,-22,-28,]),'KWRD_PACKAGE':([0,2,4,8,9,10,13,19,22,23,],[1,1,1,-8,-9,-6,-10,-11,-7,-5,]),'INT_CONST':([20,25,27,37,38,40,41,42,43,44,],[24,24,24,24,24,24,24,24,24,24,]),'KWRD_IMPORT':([0,2,4,8,9,10,13,19,22,23,],[5,5,5,-8,-9,-6,-10,-11,-7,-5,]),'BLOCK_END':([20,26,32,37,44,48,55,],[-29,-17,45,-29,-29,-15,-16,]),'DIVIDE':([24,29,30,34,35,36,47,49,51,52,53,54,],[-26,-27,41,-27,-24,41,-25,41,41,-23,41,-22,]),'RPAREN':([24,34,35,36,47,50,51,52,53,54,],[-26,-27,-24,47,-25,56,-20,-23,-21,-22,]),'ASSIGN':([29,],[38,]),'-':([20,25,27,37,38,40,41,42,43,44,],[25,25,25,25,25,25,25,25,25,25,]),'BLOCK_BEGIN':([15,21,46,],[20,-13,-14,]),'TIMES':([24,29,30,34,35,36,47,49,51,52,53,54,],[-26,-27,43,-27,-24,43,-25,43,43,-23,43,-22,]),'KWRD_EXTNDS':([21,],[33,]),'COMMA':([8,9,10,13,22,23,],[-8,17,-6,17,-7,-5,]),'LPAREN':([20,25,27,29,37,38,40,41,42,43,44,],[27,27,27,39,27,27,27,27,27,27,27,]),'PLUS':([24,29,30,34,35,36,47,49,51,52,53,54,],[-26,-27,40,-27,-24,40,-25,40,-20,-23,-21,-22,]),'KWRD_OBJECT':([0,2,4,6,7,8,9,10,11,12,13,19,22,23,],[-29,-29,-29,16,-4,-8,-9,-6,-2,-3,-10,-11,-7,-5,]),'IDENTIFIER':([1,5,16,17,18,20,25,27,33,37,38,39,40,41,42,43,44,],[10,10,21,10,10,29,34,34,46,29,34,50,34,34,34,34,29,]),'MINUS':([24,29,30,34,35,36,47,49,51,52,53,54,],[-26,-27,42,-27,-24,42,-25,42,-20,-23,-21,-22,]),'DOT':([10,],[18,]),'$end':([3,14,45,],[0,-1,-12,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'LibraryName':([1,5,17,18,],[8,8,22,23,]),'Package':([0,2,4,],[2,2,2,]),'ProgramStructure':([0,],[3,]),'ObjectDeclare':([6,],[15,]),'print_st':([20,37,44,],[31,31,31,]),'Block':([20,37,44,],[32,48,55,]),'ObjectDef':([6,],[14,]),'ImportExpr':([1,5,],[9,13,]),'Import':([0,2,4,],[4,4,4,]),'arithmetic_statement':([20,37,44,],[28,28,28,]),'expression':([20,25,27,37,38,40,41,42,43,44,],[30,35,36,30,49,51,52,53,54,30,]),'HeaderDef':([0,2,4,],[6,11,12,]),'empty':([0,2,4,20,37,44,],[7,7,7,26,26,26,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> ProgramStructure","S'",1,None,None,None),
  ('ProgramStructure -> HeaderDef ObjectDef','ProgramStructure',2,'p_program_structure','/home/siddhantmanocha/Dropbox/Studies/6thsem/cs335/compilerProject/asgn1/include/grammar.py',11),
  ('HeaderDef -> Package HeaderDef','HeaderDef',2,'p_header_define','/home/siddhantmanocha/Dropbox/Studies/6thsem/cs335/compilerProject/asgn1/include/grammar.py',14),
  ('HeaderDef -> Import HeaderDef','HeaderDef',2,'p_header_define','/home/siddhantmanocha/Dropbox/Studies/6thsem/cs335/compilerProject/asgn1/include/grammar.py',15),
  ('HeaderDef -> empty','HeaderDef',1,'p_header_define','/home/siddhantmanocha/Dropbox/Studies/6thsem/cs335/compilerProject/asgn1/include/grammar.py',16),
  ('LibraryName -> IDENTIFIER DOT LibraryName','LibraryName',3,'p_import_librarynames','/home/siddhantmanocha/Dropbox/Studies/6thsem/cs335/compilerProject/asgn1/include/grammar.py',21),
  ('LibraryName -> IDENTIFIER','LibraryName',1,'p_import_librarynames','/home/siddhantmanocha/Dropbox/Studies/6thsem/cs335/compilerProject/asgn1/include/grammar.py',22),
  ('ImportExpr -> ImportExpr COMMA LibraryName','ImportExpr',3,'p_import_expression','/home/siddhantmanocha/Dropbox/Studies/6thsem/cs335/compilerProject/asgn1/include/grammar.py',25),
  ('ImportExpr -> LibraryName','ImportExpr',1,'p_import_expression','/home/siddhantmanocha/Dropbox/Studies/6thsem/cs335/compilerProject/asgn1/include/grammar.py',26),
  ('Package -> KWRD_PACKAGE ImportExpr','Package',2,'p_package_define','/home/siddhantmanocha/Dropbox/Studies/6thsem/cs335/compilerProject/asgn1/include/grammar.py',32),
  ('Import -> KWRD_IMPORT ImportExpr','Import',2,'p_import_define','/home/siddhantmanocha/Dropbox/Studies/6thsem/cs335/compilerProject/asgn1/include/grammar.py',37),
  ('Import -> KWRD_IMPORT ImportExpr STATE_END','Import',3,'p_import_define','/home/siddhantmanocha/Dropbox/Studies/6thsem/cs335/compilerProject/asgn1/include/grammar.py',38),
  ('ObjectDef -> ObjectDeclare BLOCK_BEGIN Block BLOCK_END','ObjectDef',4,'p_object_define','/home/siddhantmanocha/Dropbox/Studies/6thsem/cs335/compilerProject/asgn1/include/grammar.py',44),
  ('ObjectDeclare -> KWRD_OBJECT IDENTIFIER','ObjectDeclare',2,'p_object_declare','/home/siddhantmanocha/Dropbox/Studies/6thsem/cs335/compilerProject/asgn1/include/grammar.py',48),
  ('ObjectDeclare -> KWRD_OBJECT IDENTIFIER KWRD_EXTNDS IDENTIFIER','ObjectDeclare',4,'p_object_declare','/home/siddhantmanocha/Dropbox/Studies/6thsem/cs335/compilerProject/asgn1/include/grammar.py',49),
  ('Block -> arithmetic_statement STATE_END Block','Block',3,'p_block_statements','/home/siddhantmanocha/Dropbox/Studies/6thsem/cs335/compilerProject/asgn1/include/grammar.py',54),
  ('Block -> print_st STATE_END Block','Block',3,'p_block_statements','/home/siddhantmanocha/Dropbox/Studies/6thsem/cs335/compilerProject/asgn1/include/grammar.py',55),
  ('Block -> empty','Block',1,'p_block_statements','/home/siddhantmanocha/Dropbox/Studies/6thsem/cs335/compilerProject/asgn1/include/grammar.py',56),
  ('arithmetic_statement -> IDENTIFIER ASSIGN expression','arithmetic_statement',3,'p_arithmetic_statement_assign','/home/siddhantmanocha/Dropbox/Studies/6thsem/cs335/compilerProject/asgn1/include/grammar.py',61),
  ('arithmetic_statement -> expression','arithmetic_statement',1,'p_arithmetic_statement_expr','/home/siddhantmanocha/Dropbox/Studies/6thsem/cs335/compilerProject/asgn1/include/grammar.py',65),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','/home/siddhantmanocha/Dropbox/Studies/6thsem/cs335/compilerProject/asgn1/include/grammar.py',69),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','/home/siddhantmanocha/Dropbox/Studies/6thsem/cs335/compilerProject/asgn1/include/grammar.py',70),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','/home/siddhantmanocha/Dropbox/Studies/6thsem/cs335/compilerProject/asgn1/include/grammar.py',71),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','/home/siddhantmanocha/Dropbox/Studies/6thsem/cs335/compilerProject/asgn1/include/grammar.py',72),
  ('expression -> - expression','expression',2,'p_expression_uminus','/home/siddhantmanocha/Dropbox/Studies/6thsem/cs335/compilerProject/asgn1/include/grammar.py',80),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','/home/siddhantmanocha/Dropbox/Studies/6thsem/cs335/compilerProject/asgn1/include/grammar.py',84),
  ('expression -> INT_CONST','expression',1,'p_expression_number','/home/siddhantmanocha/Dropbox/Studies/6thsem/cs335/compilerProject/asgn1/include/grammar.py',88),
  ('expression -> IDENTIFIER','expression',1,'p_expression_name','/home/siddhantmanocha/Dropbox/Studies/6thsem/cs335/compilerProject/asgn1/include/grammar.py',92),
  ('print_st -> IDENTIFIER LPAREN IDENTIFIER RPAREN','print_st',4,'p_printstatement_1','/home/siddhantmanocha/Dropbox/Studies/6thsem/cs335/compilerProject/asgn1/include/grammar.py',100),
  ('empty -> <empty>','empty',0,'p_empty','/home/siddhantmanocha/Dropbox/Studies/6thsem/cs335/compilerProject/asgn1/include/grammar.py',107),
]