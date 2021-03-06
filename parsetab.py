
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\xd2;~\xdf\xb4\xda\rpt\x88\x0bm\xc3F\n\xf6'
    
_lr_action_items = {'$end':([3,4,6,8,9,12,21,24,26,27,28,29,30,31,33,34,],[-14,-12,0,-13,-2,-14,-10,-1,-11,-3,-6,-4,-5,-9,-8,-7,]),'COS':([0,2,7,10,11,14,15,17,18,19,20,23,],[1,1,1,1,1,1,1,1,1,1,1,1,]),'FRAC':([0,2,7,10,11,14,15,17,18,19,20,23,],[2,2,2,2,2,2,2,2,2,2,2,2,]),'NAME':([0,2,7,10,11,14,15,17,18,19,20,23,],[3,12,12,12,12,12,12,12,12,12,12,12,]),'TIMES':([3,4,8,9,12,13,16,21,22,24,25,26,27,28,29,30,31,32,33,34,],[-14,-12,-13,20,-14,20,20,-10,20,20,20,-11,20,-6,20,-5,-9,20,-8,-7,]),'END':([4,8,12,21,26,27,28,29,30,31,32,33,34,],[-12,-13,-14,-10,-11,-3,-6,-4,-5,-9,34,-8,-7,]),'NUMBER':([0,2,7,10,11,14,15,17,18,19,20,23,],[4,4,4,4,4,4,4,4,4,4,4,4,]),'MINUS':([0,2,3,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[10,10,-14,-12,10,-13,19,10,10,-14,19,10,10,19,10,10,10,10,-10,19,10,19,19,-11,-3,-6,-4,-5,-9,19,-8,-7,]),'MIDDLE':([4,8,12,13,21,26,27,28,29,30,31,33,34,],[-12,-13,-14,23,-10,-11,-3,-6,-4,-5,-9,-8,-7,]),'EQUALS':([3,],[14,]),'PLUS':([3,4,8,9,12,13,16,21,22,24,25,26,27,28,29,30,31,32,33,34,],[-14,-12,-13,17,-14,17,17,-10,17,17,17,-11,-3,-6,-4,-5,-9,17,-8,-7,]),'LPAREN':([0,1,2,5,7,10,11,14,15,17,18,19,20,23,],[7,11,7,15,7,7,7,7,7,7,7,7,7,7,]),'RPAREN':([4,8,12,16,21,22,25,26,27,28,29,30,31,33,34,],[-12,-13,-14,26,-10,31,33,-11,-3,-6,-4,-5,-9,-8,-7,]),'PI':([0,2,7,10,11,14,15,17,18,19,20,23,],[8,8,8,8,8,8,8,8,8,8,8,8,]),'SIN':([0,2,7,10,11,14,15,17,18,19,20,23,],[5,5,5,5,5,5,5,5,5,5,5,5,]),'DIVIDE':([3,4,8,9,12,13,16,21,22,24,25,26,27,28,29,30,31,32,33,34,],[-14,-12,-13,18,-14,18,18,-10,18,18,18,-11,18,-6,18,-5,-9,18,-8,-7,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,2,7,10,11,14,15,17,18,19,20,23,],[9,13,16,21,22,24,25,27,28,29,30,32,]),'statement':([0,],[6,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> NAME EQUALS expression','statement',3,'p_statement_assign','/home/kristoffer/PycharmProjects/test/calc.py',72),
  ('statement -> expression','statement',1,'p_statement_expr','/home/kristoffer/PycharmProjects/test/calc.py',77),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','/home/kristoffer/PycharmProjects/test/calc.py',81),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','/home/kristoffer/PycharmProjects/test/calc.py',82),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','/home/kristoffer/PycharmProjects/test/calc.py',83),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','/home/kristoffer/PycharmProjects/test/calc.py',84),
  ('expression -> FRAC expression MIDDLE expression END','expression',5,'p_expression_devide','/home/kristoffer/PycharmProjects/test/calc.py',91),
  ('expression -> SIN LPAREN expression RPAREN','expression',4,'p_expression_sin','/home/kristoffer/PycharmProjects/test/calc.py',95),
  ('expression -> COS LPAREN expression RPAREN','expression',4,'p_expression_cos','/home/kristoffer/PycharmProjects/test/calc.py',99),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','/home/kristoffer/PycharmProjects/test/calc.py',104),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','/home/kristoffer/PycharmProjects/test/calc.py',108),
  ('expression -> NUMBER','expression',1,'p_expression_number','/home/kristoffer/PycharmProjects/test/calc.py',112),
  ('expression -> PI','expression',1,'p_expression_pi','/home/kristoffer/PycharmProjects/test/calc.py',116),
  ('expression -> NAME','expression',1,'p_expression_name','/home/kristoffer/PycharmProjects/test/calc.py',120),
]
