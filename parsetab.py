
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASIGNAR COMDOB CORDER CORIZQ DISTINTO DIV DOSPUNTO ENDL ENTERO FOR GET IDENTIFICADOR IGUAL INCLUDE INT LLADER LLAIZQ MAYORDER MAYORIGUAL MAYORIZQ MAYORQUE MENORIGUAL MENORQUE MIENTRAS MINUSMINUS MODULO MULT NAMESPACE NOT NUMERAL OR PARDER PARIZQ PLUSPLUS POTENCIA PUNTO PUNTOCOMA RESERVADA RESTA RETURN SI SINO STD SUMA SYSTEM USING VOID\n    expresion : RESERVADA PARIZQ IDENTIFICADOR IDENTIFICADOR ASIGNAR ENTERO PUNTOCOMA IDENTIFICADOR MENORIGUAL ENTERO PUNTOCOMA IDENTIFICADOR PLUSPLUS PARDER LLAIZQ SYSTEM PUNTO IDENTIFICADOR PUNTO IDENTIFICADOR PARIZQ COMDOB IDENTIFICADOR DOSPUNTO COMDOB SUMA IDENTIFICADOR PARDER PUNTOCOMA LLADER LLADER\n              | SYSTEM PUNTO IDENTIFICADOR PUNTO IDENTIFICADOR PARIZQ COMDOB IDENTIFICADOR DOSPUNTO COMDOB SUMA IDENTIFICADOR PARDER PUNTOCOMA LLADER\n              | LLADER LLADER\n    '
    
_lr_action_items = {'RESERVADA':([0,],[2,]),'SYSTEM':([0,32,],[3,34,]),'LLADER':([0,4,31,47,48,],[4,7,33,48,49,]),'$end':([1,7,33,49,],[0,-3,-2,-1,]),'PARIZQ':([2,13,38,],[5,15,39,]),'PUNTO':([3,9,34,36,],[6,11,35,37,]),'IDENTIFICADOR':([5,6,8,11,16,17,24,25,35,37,40,44,],[8,9,10,13,18,19,26,27,36,38,41,45,]),'ASIGNAR':([10,],[12,]),'ENTERO':([12,20,],[14,22,]),'PUNTOCOMA':([14,22,29,46,],[16,24,31,47,]),'COMDOB':([15,21,39,42,],[17,23,40,43,]),'MENORIGUAL':([18,],[20,]),'DOSPUNTO':([19,41,],[21,42,]),'SUMA':([23,43,],[25,44,]),'PLUSPLUS':([26,],[28,]),'PARDER':([27,28,45,],[29,30,46,]),'LLAIZQ':([30,],[32,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expresion':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expresion","S'",1,None,None,None),
  ('expresion -> RESERVADA PARIZQ IDENTIFICADOR IDENTIFICADOR ASIGNAR ENTERO PUNTOCOMA IDENTIFICADOR MENORIGUAL ENTERO PUNTOCOMA IDENTIFICADOR PLUSPLUS PARDER LLAIZQ SYSTEM PUNTO IDENTIFICADOR PUNTO IDENTIFICADOR PARIZQ COMDOB IDENTIFICADOR DOSPUNTO COMDOB SUMA IDENTIFICADOR PARDER PUNTOCOMA LLADER LLADER','expresion',31,'p_expresion','analizador_sintactico.py',10),
  ('expresion -> SYSTEM PUNTO IDENTIFICADOR PUNTO IDENTIFICADOR PARIZQ COMDOB IDENTIFICADOR DOSPUNTO COMDOB SUMA IDENTIFICADOR PARDER PUNTOCOMA LLADER','expresion',15,'p_expresion','analizador_sintactico.py',11),
  ('expresion -> LLADER LLADER','expresion',2,'p_expresion','analizador_sintactico.py',12),
]
