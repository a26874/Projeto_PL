
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'left+-left*/aleatorio comentarioMult comentarioOne entrada escrever fim fold funcao id map numF numInt texto Z :  LstV \';\'          LstV :  V           LstV : LstV \';\' V  V : id \'=\' E  V : id \'=\' Lista  Lista : \'[\' ListIn \']\'  ListIn : numInt \',\' ListIn ListIn : numInt Texto :  texto   Texto : id    Texto : id "[" numInt "]"  Texto : Texto "<" ">" Texto   V : escrever "(" Texto ")"   V : id \'=\' entrada \'(\' \')\'   E : E \'+\' T  E : E \'-\' T  E : T  T : T \'/\' F  T : T \'*\' F  T : F   F : \'(\' E \')\'   F : numInt    F : numF    F : id    F : id "[" numInt "]"  F : aleatorio "(" numInt ")" '
    
_lr_action_items = {'id':([0,6,7,8,14,25,26,29,30,47,],[4,4,10,23,10,10,10,10,10,23,]),'escrever':([0,6,],[5,5,]),'$end':([1,6,],[0,-1,]),';':([2,3,9,10,11,12,15,17,18,19,34,38,39,40,41,42,43,44,49,51,],[6,-2,-3,-24,-4,-5,-17,-20,-22,-23,-13,-15,-16,-14,-21,-18,-19,-6,-25,-26,]),'=':([4,],[7,]),'(':([5,7,13,14,20,25,26,29,30,],[8,14,27,14,33,14,14,14,14,]),'entrada':([7,],[13,]),'[':([7,10,23,],[16,24,36,]),'numInt':([7,14,16,24,25,26,29,30,33,36,45,],[18,18,32,37,18,18,18,18,46,48,32,]),'numF':([7,14,25,26,29,30,],[19,19,19,19,19,19,]),'aleatorio':([7,14,25,26,29,30,],[20,20,20,20,20,20,]),'texto':([8,47,],[22,22,]),'/':([10,15,17,18,19,38,39,41,42,43,49,51,],[-24,29,-20,-22,-23,29,29,-21,-18,-19,-25,-26,]),'*':([10,15,17,18,19,38,39,41,42,43,49,51,],[-24,30,-20,-22,-23,30,30,-21,-18,-19,-25,-26,]),'+':([10,11,15,17,18,19,28,38,39,41,42,43,49,51,],[-24,25,-17,-20,-22,-23,25,-15,-16,-21,-18,-19,-25,-26,]),'-':([10,11,15,17,18,19,28,38,39,41,42,43,49,51,],[-24,26,-17,-20,-22,-23,26,-15,-16,-21,-18,-19,-25,-26,]),')':([10,15,17,18,19,21,22,23,27,28,38,39,41,42,43,46,49,51,52,53,],[-24,-17,-20,-22,-23,34,-9,-10,40,41,-15,-16,-21,-18,-19,51,-25,-26,-12,-11,]),'<':([21,22,23,52,53,],[35,-9,-10,35,-11,]),']':([31,32,37,48,50,],[44,-8,49,53,-7,]),',':([32,],[45,]),'>':([35,],[47,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Z':([0,],[1,]),'LstV':([0,],[2,]),'V':([0,6,],[3,9,]),'E':([7,14,],[11,28,]),'Lista':([7,],[12,]),'T':([7,14,25,26,],[15,15,38,39,]),'F':([7,14,25,26,29,30,],[17,17,17,17,42,43,]),'Texto':([8,47,],[21,52,]),'ListIn':([16,45,],[31,50,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Z","S'",1,None,None,None),
  ('Z -> LstV ;','Z',2,'p_z','arith_grammar.py',48),
  ('LstV -> V','LstV',1,'p_lstv_head','arith_grammar.py',52),
  ('LstV -> LstV ; V','LstV',3,'p_lstv_tail','arith_grammar.py',56),
  ('V -> id = E','V',3,'p_atribArith','arith_grammar.py',68),
  ('V -> id = Lista','V',3,'p_atribList','arith_grammar.py',73),
  ('Lista -> [ ListIn ]','Lista',3,'p_lista','arith_grammar.py',80),
  ('ListIn -> numInt , ListIn','ListIn',3,'p_list1','arith_grammar.py',84),
  ('ListIn -> numInt','ListIn',1,'p_list2','arith_grammar.py',94),
  ('Texto -> texto','Texto',1,'p_text_1','arith_grammar.py',100),
  ('Texto -> id','Texto',1,'p_text_2','arith_grammar.py',104),
  ('Texto -> id [ numInt ]','Texto',4,'p_text_3','arith_grammar.py',108),
  ('Texto -> Texto < > Texto','Texto',4,'p_text_concat','arith_grammar.py',112),
  ('V -> escrever ( Texto )','V',4,'p_esc','arith_grammar.py',125),
  ('V -> id = entrada ( )','V',5,'p_ent','arith_grammar.py',134),
  ('E -> E + T','E',3,'p_expr_soma','arith_grammar.py',141),
  ('E -> E - T','E',3,'p_expr_sub','arith_grammar.py',146),
  ('E -> T','E',1,'p_expr1','arith_grammar.py',151),
  ('T -> T / F','T',3,'p_expr_div','arith_grammar.py',155),
  ('T -> T * F','T',3,'p_expr_mult','arith_grammar.py',160),
  ('T -> F','T',1,'p_expr2','arith_grammar.py',165),
  ('F -> ( E )','F',3,'p_expr3','arith_grammar.py',169),
  ('F -> numInt','F',1,'p_expr4','arith_grammar.py',175),
  ('F -> numF','F',1,'p_expr5','arith_grammar.py',179),
  ('F -> id','F',1,'p_expr6','arith_grammar.py',183),
  ('F -> id [ numInt ]','F',4,'p_expr7','arith_grammar.py',187),
  ('F -> aleatorio ( numInt )','F',4,'p_rand','arith_grammar.py',191),
]
