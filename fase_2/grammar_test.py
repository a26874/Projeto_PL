from grammar import Grammar

ag = Grammar()
ag.build()

#res = ag.parse("2+3*4")
#print(f"Resultado: {res}")
#res = ag.parse("(2+3)*4")
#print(f"Resultado: {res}")
#res = ag.parse("1+3/5")
#print(f"Resultado: {res}")
#res = ag.parse("2+3*4/4")
res = ag.parse("""FUNCAO amor():
                ESCREVER("OLA");
                FIM
                a = 2;
                ESCREVER(2);
               """)
print(f"Resultado: {res}")
