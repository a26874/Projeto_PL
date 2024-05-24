from arith_lexer import ArithLexer
import ply.yacc as pyacc


class ArithGrammar:
    # da prioridade dependendo do que escreve, gramatica com conlfito nao tem grande qualidade
    # maior nivel maior prioridade + -> *
    precedence = (
        ('left', '+','-'),  # level = 1 associativa = left
        ('left', '*','/')  # level = 2 associativa = left   
    )

    def __init__(self):
        self.yacc = None
        self.lexer = None
        self.tokens = None

    def build(self, **kwargs):
        self.lexer = ArithLexer()
        self.lexer.build(**kwargs)
        self.tokens = self.lexer.tokens
        self.yacc = pyacc.yacc(module=self, **kwargs)

    def parse(self, string):
        self.lexer.input(string)
        return self.yacc.parse(lexer=self.lexer.lexer)

    # especificação da gramática :
    # Rule 0     S' -> Z
	# Rule 1     Z -> LstV ;
    # def p_expr(self, p):
    # E → E '+' T 
    #    | E '-' T
    #    | T    
    #T → T '*' F 
    #    | F 
    #F → '(' E ')' 
    #    | numInt
    #    | numF    
    #    | id
    #    | id '[' numInt ']'
    #    | numInt / numInt

    def p_z(self, p): 
        """ Z :  LstV ';'"""
        p[0] =  p[1]
	
    def p_lstv_head(self, p): 
        """ LstV :  V          """
        p[0] = {'op': 'seq', "args": [ p[1] ] } 
					
    def p_lstv_tail(self, p): 
        """ LstV : LstV ';' V """
        lstArgs =  p[1]['args']
        lstArgs.append(p[3])
        p[0] = { "op": 'seq', 'args': lstArgs  }
		
    def p_atrib(self, p ):
        """ V : id '=' E """ 
        p[0] = { 'op': 'atr',
				 'args': [ p[1], p[3] ] }


    def p_expr_soma(self, p):
        """ E : E '+' T """
        print(f"[E : E '+' T {p[1] + p[3]}]")
        p[0] = p[1] + p[3]

    def p_expr_sub(self, p):
        """ E : E '-' T """
        print(f"[E : E '-' T {p[1] + p[3]}]")
        p[0] = p[1] - p[3]

    def p_expr1(self, p):
        """ E : T """
        print("[E->T]")
        p[0] = p[1]

    def p_expr_div(self, p):
        """ F : numInt '/' numInt """
        print(f"[F->numInt '/' numInt {p[1] / p[3]}]")
        p[0] = p[1] / p[3]

    def p_expr_mult(self, p):
        """ T : T '*' F """
        print(f"[T->T '*' F {p[1] * p[3]}]")
        p[0] = p[1] * p[3]

    def p_expr2(self, p):
        """ T : F """
        print("[T->F]")
        p[0] = p[1]

    def p_expr3(self, p):
        """  F : '(' E ')' """
        #    ^    ^  ^  ^
        #    0    1  2  3
        print("[F->'(' E ')']")
        p[0] = p[2]

    def p_expr4(self, p):
        """  F : numInt  """
        print(f"[F-> numInt {p[1]}]")
        p[0] = p[1]
        
    def p_expr5(self, p):
        """  F : numF  """
        print(f"[F-> numF {p[1]}]")
        p[0] = p[1]
        
    def p_expr6(self, p):
        """  F : id  """
        print(f"[F-> id {p[1]}]")
        p[0] = p[1]

    def p_expr7(self, p):
        """  F : id "[" numInt "]" """
        print(f"[F-> id '[' numInt ']' {p[1]}]")
        p[0] = p[1][p[3]]

# aula 22 ver eval

    def p_error(self, p):
        if p:
            print(f"Syntax error: unexpected '{p.type}'")
        else:
            print("Syntax error: unexpected end of file")
        exit(1)
