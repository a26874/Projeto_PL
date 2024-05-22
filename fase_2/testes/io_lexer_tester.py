from io_lexer import IOLexer

exemplos = ["ESCREVER(\"Ola, \"<> curso);","ESCREVER (\"Ola, #{escola} #{inst}!\");","valor = ENTRADA();","ate10 = ALEATORIO(10);"]

for frase in exemplos:
	print(f"----------------------")
	print(f"frase: '{frase}'")
	al = IOLexer()
	al.build()
	al.input(frase)
	print('tokens: \n',end="")
	while True:
		tk = al.token() 
		if not tk: 
			break
		print(tk,end="\n")
	print()	