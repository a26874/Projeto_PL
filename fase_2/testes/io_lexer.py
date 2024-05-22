
import ply.lex as plex

class IOLexer:
    
    tokens= ("escrever","texto","id","numInt","numF","aleatorio","entrada")
    literals = ['<','>','#','*', '+', '(', ')','-','/',',',':',';','=']
    t_ignore = " \n"
    
    def __init__(self):
        self.lexer = None
        
    t_aleatorio = r"ALEATORIO"
    t_escrever = r"ESCREVER"
    t_entrada = r"ENTRADA"
    
    def t_id(self,t):
        r"[a-z][a-z0-9]*"
        return t

    def t_texto(self,t):
        r"\"[^\"]*\""
		#t.value = t.value[1:-1]
        return t
       
    def t_numF(self, t):
        r"[0-9]+\.[0-9]+"
        t.value = float (t.value)
        return t
   
    def t_numInt(self, t):
        r"[0-9]+"
        t.value = int (t.value)
        return t
    
    def build(self, **kwargs):
        self.lexer = plex.lex(module=self, **kwargs)

    def input(self, string):
        self.lexer.input(string)

    def token(self):
        token = self.lexer.token()
        return token
	    #return token if token is None else token.type

    def t_error(self, t):
        print(f"Unexpected token: [{t.value[:10]}]")
        exit(1)


