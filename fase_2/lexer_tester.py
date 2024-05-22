from lexer import Lexer
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

exemplos = ["""FUNCAO somatorio( [] ),: 0 ;
FUNCAO somatorio( x:xs ),: x + somatorio(xs) ;
resultado = somatorio([1,2,3]);
""",
"""
lista1 = map( mais2, [] );  -- []
lista2 = map( mais2, [ 1, 2, 3 ] );
 -- [ mais2(1),mais2(2),mais2(3)] = [3,4,5]
lista3 = fold( soma, [ 1, 2, 3 ], 0 );
{--  exemplo interpolacao de strings
Ola, EST IPCA! --}
"""]

for frase in exemplos:
	print(f"----------------------")
	print(f"frase: '{frase}'")
	al = Lexer()
	al.build()
	al.input(frase)
	print('tokens: \n',end="")
	while True:
		tk = al.token() 
		if not tk: 
			break
		print(tk,end="\n")
	print()	