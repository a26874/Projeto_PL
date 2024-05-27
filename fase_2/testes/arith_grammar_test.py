from arith_grammar import ArithGrammar

ag = ArithGrammar()
ag.build()

#res = ag.parse("2+3*4")
#print(f"Resultado: {res}")
#res = ag.parse("(2+3)*4")
#print(f"Resultado: {res}")
#res = ag.parse("1+3/5")
#print(f"Resultado: {res}")
#res = ag.parse("2+3*4/4")
res = ag.parse("{-- texto --}")
print(f"Resultado: {res}")
