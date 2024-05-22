from func_lexer import FuncLexer

exemplos = ["""FUNCAO soma(a,b),: a+b ;
FUNCAO soma2(c) :
c = c+1 ;
c+1 ;
FIM
seis = soma(4,2);
oito = soma2(seis);
"""]

for frase in exemplos:
	print(f"----------------------")
	print(f"frase: '{frase}'")
	al = FuncLexer()
	al.build()
	al.input(frase)
	print('tokens: ',end="")
	while True:
		tk = al.token() 
		if not tk: 
			break
		print(tk,end="\n")
	print()	