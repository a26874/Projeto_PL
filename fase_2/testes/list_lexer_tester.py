from list_lexer import ListLexer

exemplos = ["lista = [ 1, 2, 3 ] ;","ESCREVER( lista );  [1,2,3]","vazia = [] ;","lista2 = map( mais2, [ 1, 2, 3 ] );","lista3 = fold( soma, [ 1, 2, 3 ], 0 );"]

for frase in exemplos:
	print(f"----------------------")
	print(f"frase: '{frase}'")
	al = ListLexer()
	al.build()
	al.input(frase)
	print('tokens: \n',end="")
	while True:
		tk = al.token() 
		if not tk: 
			break
		print(tk,end="\n")
	print()	