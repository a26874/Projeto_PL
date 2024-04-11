"""
	Processamento de Linguagens (ESI) 
	Trabalho Prático 1
	Exemplo de Apoio: er_main.py
	
	invocar como: python er_main.py exemplo01.er.json	
"""
from er_eval import ExpReg
import sys
import json


if len(sys.argv) >= 2:
	with open(sys.argv[1], "r") as f:
		try:
			Q = []
			q0 = []
			F = []
			arvore = json.load(f)
			expression, transitions,alfabeto = ExpReg.execução(arvore)
			for key in transitions[expression].keys():
				if key == 'final' or key == 'inicial':
					continue
				Q.append(key)
			for estado in transitions[expression]['inicial']:
				q0.append(estado)
			for estado in transitions[expression]['final']:
				F.append(estado)
			json = '{\n'
			alfabeto_with_quotes = [f'"{value}"' for value in alfabeto]
			json += f'"V": [{", ".join(alfabeto_with_quotes)}],\n'
			Q_with_quotes = [f'"{value}"' for value in Q]
			json += f'"Q": [{", ".join(Q_with_quotes)}],\n'
			json += '"delta" :{\n'
			transições_ordem = dict(sorted(transitions[expression].items()))
			for key,value in transições_ordem.items():
				if key == 'final' or key == 'inicial':
					continue
				key_with_quotes = f'"{key}":'
				key_with_quotes += "{"
				json += f"	{key_with_quotes}"
				for key_in, value_in in value.items():
					value_in_with_quotes = [f'"{value}"' for value in value_in]
					json += f'"{key_in}": [{", ".join(value_in_with_quotes)}]'
				json += "},\n"
					
			json = json[:-2]
			json += '\n},\n'
			q0_with_quotes = [f'"{value}"' for value in q0]
			F_with_quotes = [f'"{value}"' for value in F]
			json += f'"q0" :[{", ".join(q0_with_quotes)}],\n'
			json += f'"F" :[{", ".join(F_with_quotes)}]\n'
			json += "}"
			if len(sys.argv) == 3:
				nome = sys.argv[2]
				with open(f"./json_novos/{nome}.json", "w", encoding="utf-8") as ficheiro:
					ficheiro.write(json)
			else:
				with open("./json_novos/AFND.json","w",encoding="utf-8") as ficheiro:
					ficheiro.write(json)
		except Exception as e:
			print(e, file=sys.stderr)
else:
	print("falta indicar o ficheiro de entrada:", file=sys.sterr)
	print("Uso: python er_main.py <ARQUIVO_JSON> [nome_ficheiro]")
