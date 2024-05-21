from arith_lexer import ArithLexer

exemplos = ["2 + 3","-a","y + a","-a + 42"]

for frase in exemplos:
	print(f"----------------------")
	print(f"frase: '{frase}'")
	al = ArithLexer()
	al.build()
	al.input(frase)
	print('tokens: ',end="")
	while True:
		tk = al.token() 
		if not tk: 
			break
		print(tk,end="\n")
	print()	