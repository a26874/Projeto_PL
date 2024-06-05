import sys
from grammar import Grammar
from eval import Eval

if len(sys.argv) != 2:
        print("Uso: python main.py <nome.fca>")
        sys.exit(1)

fca = sys.argv[1]

with open(fca, 'r') as file:
    codigo = file.read()
lg = Grammar()
lg.build()
res = lg.parse(codigo)
resultado = Eval.evaluate(res)