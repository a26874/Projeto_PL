from lexer import Lexer
import ply.yacc as pyacc


# esta gramatica junta a aritmetrica, Input e Output.
class ArithGrammar:
    # da prioridade dependendo do que escreve, gramatica com conlfito nao tem grande qualidade
    # maior nivel maior prioridade + -> *
    precedence = (
        ('left', '+', '-'),  # level = 1 associativa = left
        ('left', '*', '/')  # level = 2 associativa = left
    )

    def __init__(self):
        self.yacc = None
        self.lexer = None
        self.tokens = None

    def build(self, **kwargs):
        self.lexer = Lexer()
        self.lexer.build(**kwargs)
        self.tokens = self.lexer.tokens
        self.yacc = pyacc.yacc(module=self, **kwargs)

    def parse(self, string):
        self.lexer.input(string)
        return self.yacc.parse(lexer=self.lexer.lexer)

    # especificação da gramática :
    # Rule 0     S' -> Z
    # Rule 1     Z -> LstV ;
    # Rule 2     LstV -> V
    # Rule 3     LstV -> LstV ; V
    # Rule 4     V -> id = E
    # Rule 5     V -> escrever id
    # E → E '+' T
    #    | E '-' T
    #    | T
    # T → T '*' F
    #    | T '/' F
    #    | F
    # F → '(' E ')'
    #    | numInt
    #    | numF
    #    | id
    #    | id '[' numInt ']'
    def p_z(self, p):
        """ Z :  LstV ';'         """
        p[0] = p[1]

    def p_lstv_head(self, p):
        """ LstV :  V          """
        p[0] = {'op': 'seq', "args": [p[1]]}

    def p_lstv_tail(self, p):
        """ LstV : LstV ';' V """
        lstArgs = p[1]['args']
        lstArgs.append(p[3])
        p[0] = {"op": 'seq', 'args': lstArgs}

    def p_atribMap(self, p):
        """ V : id '=' map '(' id ',' Lista ')'"""

    def p_atribFold(self, p):
        """ V : id '=' fold '(' id ',' Lista ',' numInt ')' """

    def p_atribArith(self, p):
        """ V : id '=' E """
        p[0] = {'op': 'atr',
                'args': [p[1], p[3]]}

    def p_atribList(self, p):
        """ V : id '=' Lista """
        p[0] = {'op': 'atr',
                'args': [p[1], p[3]]}

    # Lista

    def p_lista(self, p):
        """ Lista : '[' ListIn ']' """
        p[0] = p[2]
    def p_list1(self, p):
        """ ListIn : numInt ',' ListIn"""
        p[0] = []
        p[0].append(p[1])
        if p[3] is list:
            for num in p[3]:
                p[0].append(num)
        else:
            p[0].append(p[3])

    def p_list2(self, p):
        """ ListIn : numInt"""
        p[0] = p[1]

    # escrita na tela

    def p_text_1(self, p):
        """ Texto :  texto  """
        p[0] = p[1]

    def p_text_2(self, p):
        """ Texto : id  """
        p[0] = {'var': p[1]}

    def p_text_3(self, p):
        """  Texto : id "[" numInt "]" """
        p[0] = {'var': p[1], 'index': p[3]}


    def p_text_concat(self, p):
        """ Texto : Texto "<" ">" Texto  """
        p[0] = list()
        if isinstance(p[1], list):
            p[0].extend(p[1])
        else:
            p[0].append(p[1])

        if isinstance(p[4], list):
            p[0].extend(p[4])
        else:
            p[0].append(p[4])

    def p_esc(self, p):
        """ V : escrever "(" Texto ")"  """
        if not isinstance(p[3], list):
            p[3] = [p[3]]
        p[0] = {'op': 'esc',
                'args': p[3]}

    # aritmetrica

    def p_expr_soma(self, p):
        """ E : E '+' T """
        p[0] = {'op': p[2],
                'args': [p[1], p[3]]}

    def p_expr_sub(self, p):
        """ E : E '-' T """
        p[0] = {'op': p[2],
                'args': [p[1], p[3]]}

    def p_expr1(self, p):
        """ E : T """
        p[0] = p[1]

    def p_expr_div(self, p):
        """ T : T '/' F """
        p[0] = {'op': p[2],
                'args': [p[1], p[3]]}

    def p_expr_mult(self, p):
        """ T : T '*' F """
        p[0] = {'op': p[2],
                'args': [p[1], p[3]]}

    def p_expr2(self, p):
        """ T : F """
        p[0] = p[1]

    def p_expr3(self, p):
        """  F : '(' E ')' """
        #    ^    ^  ^  ^
        #    0    1  2  3
        p[0] = p[2]

    def p_expr4(self, p):
        """  F : numInt  """
        p[0] = p[1]

    def p_expr5(self, p):
        """  F : numF  """
        p[0] = p[1]

    def p_expr6(self, p):
        """  F : id  """
        p[0] = {'var': p[1]}

    def p_expr7(self, p):
        """  F : id "[" numInt "]" """
        p[0] = {'var': p[1], 'index': p[3]}

    def p_rand(self, p):
        """ F : aleatorio "(" numInt ")" """
        p[0] = {'op': 'al',
                'args': [p[3]]}

    # comentario
    # def p_comentarioOne(self,p):
    #    """ Comentario : comentarioOne """
    #    p[0] = p[1]

    # def p_comentarioMult(self,p):
    #    """ Comentario : comentarioMult """
    #    p[0] = p[1]

    def p_error(self, p):
        if p:
            print(f"Syntax error: unexpected '{p.type}'")
        else:
            print("Syntax error: unexpected end of file")
        exit(1)
