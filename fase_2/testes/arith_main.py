from arith_grammar import ArithGrammar
from arith_eval import ArithEval
import sys
from pprint import PrettyPrinter

pp = PrettyPrinter(sort_dicts=False)

lg = ArithGrammar()
lg.build()

res = lg.parse("""a = 2; 
               b = 3; 
               c = a + b;
               ESCREVER(c);""")

resultado = ArithEval.evaluate(res)
