"""
	Processamento de Linguagens (ESI) 
	Trabalho Prático 1
	Exemplo de Apoio: er_main.py
	
	invocar como: python er_main.py exemplo01.er.json	
"""
from er_eval import ExpReg
import sys
import json


if len(sys.argv) == 2:
	with open(sys.argv[1], "r") as f:
		try:
			arvore = json.load(f)
			expression, transitions = ExpReg.execução(arvore)
			print(expression)
			print(transitions)
		except Exception as e:
			print(e, file=sys.stderr)
else:
	print("falta indicar o ficheiro de entrada:", file=sys.sterr)
