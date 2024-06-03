from lexer import Lexer
import ply.yacc as pyacc


# esta gramatica junta a aritmetrica, Input e Output.
class Grammar:
    # da prioridade dependendo do que escreve, gramatica com conlfito nao tem grande qualidade
    # maior nivel maior prioridade + -> *
    precedence = (
        ('left', '+', '-'),  # level = 1 associativa = left
        ('left', '*', '/'),  # level = 2 associativa = left
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

    def p_s(self, p):
        """ S : LstI """
        p[0] = dict(op='seq', args=[p[1]])

    def p_lstI_tail(self, p):
        """ LstI : LstI Inst ';'
                 | LstI InstC"""
        lstArgs = p[1]['args']
        lstArgs.append(p[2])
        p[0] = {"op": 'seq', 'args': lstArgs}

    def p_lstI_head(self, p):
        """ LstI : Inst ';'
                 | InstC"""
        p[0] = dict(op='seq', args=[p[1]])

    def p_comment(self, p):
        """ InstC : comentarioOne
                  | comentarioMult"""
        p[0] = dict(op='seq', args=[p[1]])

    def p_Inst(self,p):
        """ Inst : V """
        p[0] = {'op': 'seq', "args": [p[1]]}

    def p_inst_se(self, p):
        """ Inst : se Comp fazer ':' S fim"""
        p[0] = dict(op= 'SE', args= [ p[2], p[5] ])


    # def p_inst_func2(self,p):
    #     """ Func : funcao id '(' ')' ':' LstI  fim """
    #     p[0] = dict(op= 'FUNCAO', args= [ p[2], "", p[6] ])
    #
    # def p_inst_func1(self, p):
    #     """ V : funcao id '(' LstFunc ')' ':' LstI fim """
    #     p[0] = dict(op= 'FUNCAO', args= [ p[2], p[4], p[7] ])
    #
    # def p_inst_func3(self, p):
    #     """ V : funcao id '(' LstFunc ')' ',' ':' V ';'"""
    #     p[0] = dict(op= 'FUNCAO', args= [ p[2], p[4], p[8] ])
    #
    # def p_lstFunc1(self,p):
    #     """ LstFunc : F """
    #
    # def p_lstFunc3(self,p):
    #     """ LstFunc : F ',' LstFunc """

    #def p_atribMap(self, p):
    #    """ V : id '=' map '(' id ',' Lista ')'"""

    #def p_atribFold(self, p):
    #    """ V : id '=' fold '(' id ',' Lista ',' numInt ')' """

    def p_atribArith(self, p):
        """ V : id '=' E """
        p[0] = {'op': 'atr',
                'args': [p[1], p[3]]}

    def p_atribTexto(self, p):
        """ V : id '=' texto """
        p[0] = {'op': 'atr',
                'args': [p[1], p[3]]}

    def p_atribList(self, p):
        """ V : id '=' Lista """
        p[0] = {'op': 'atr',
                'args': [p[1], p[3]]}

    def p_atribBoolT(self, p):
        """ V : id '=' true """
        p[0] = {'op': 'atr',
                'args': [p[1], p[3]]}

    def p_atribBoolF(self, p):
        """ V : id '=' false """
        p[0] = {'op': 'atr',
                'args': [p[1], p[3]]}
    # Lista

    def p_lista(self, p):
        """ Lista : '[' ListIn ']' """
        p[0] = p[2]
        
    def p_listaVazia(self, p):
        """ Lista : '[' ']' """
        p[0] = []
        
    def p_list1(self, p):
        """ ListIn : numInt ',' ListIn"""
        p[0] = []
        p[0].append(p[1])
        if isinstance(p[3],list):
            for num in p[3]:
                p[0].append(num)
        else:
            p[0].append(p[3])

    def p_list2(self, p):
        """ ListIn : numInt"""
        p[0] = p[1]

    # escrita na tela

    def p_text_0(self, p):
        """ Texto :  texto  """
        p[0] = p[1]

    def p_text_1(self, p):
        """ Texto :  E  """
        p[0] = p[1]

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

    # input

    def p_ent(self, p):
        """ V : id '=' entrada '(' ')'  """
        p[0] = {'op': 'atr',
                'args': [p[1], "input"]}

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

    # COMPARISON
    def p_comp_diff(self, p):
            """ Comp : CompF '!' '=' CompF """
            p[0] = dict(op='DIFF', args=[p[1], p[4]])

    def p_comp_and(self, p):
            """ Comp : Comp '/' backlash Comp """
            p[0] = dict(op='AND', args=[p[1], p[4]])

    def p_comp_or(self, p):
            """ Comp : Comp backlash '/' Comp """
            p[0] = dict(op='OR', args=[p[1], p[4]])

    def p_comp_equality(self, p):
            """ Comp : CompF '=' '=' CompF """
            p[0] = dict(op='EQUALITY', args=[p[1], p[4]])

    def p_comp_higher(self, p):
            """ Comp : CompF '>' CompF """
            p[0] = dict(op='HIGHER', args=[p[1], p[3]])

    def p_comp_highereq(self, p):
            """ Comp : CompF '>' '=' CompF """
            p[0] = dict(op='HIGHEREQ', args=[p[1], p[4]])

    def p_comp_lower(self, p):
            """ Comp : CompF '<' CompF """
            p[0] = dict(op='LOWER', args=[p[1], p[3]])

    def p_comp_lowereq(self, p):
            """ Comp : CompF '<' '=' CompF """
            p[0] = dict(op='LOWEREQ', args=[p[1], p[4]])

    def p_comp_factor(self, p):
            """ CompF : '(' Comp ')' """
            p[0] = p[1]

    def p_comp_valor1(self, p):
            """ CompF : true"""
            p[0] = p[1]

    def p_comp_valor2(self, p):
            """ CompF : false"""
            p[0] = p[1]

    def p_comp_valor3(self, p):
        """  CompF : E """
        p[0] = p[1]

    def p_error(self, p):
        if p:
            print(f"Syntax error: unexpected '{p.type}'")
        else:
            print("Syntax error: unexpected end of file")
        exit(1)
