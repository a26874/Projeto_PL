from grammar import Grammar
from eval import Eval

lg = Grammar()
lg.build()

## EXEMPLO A 1
res = lg.parse("""tmp_01 = 2*3+4 ;
a1_ = 12345 - (5191 * 15) ;
idade_valida? = 1;
mult_3! = a1_ * 3 ;
ESCREVER(mult_3!);""")

resultado = Eval.evaluate(res)
print("\n=_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_=\n")

## EXEMPLO B 1

res = lg.parse("""valor = "ola";
ESCREVER(valor); -- conteúdo de valor é apresentado
ESCREVER(365 * 2); -- 730
ESCREVER("Ola Mundo"); -- Ola, Mundo!
curso = "ESI";
ESCREVER("Ola, "<> curso);""")

resultado = Eval.evaluate(res)
print("\n=_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_=\n")

## EXEMPLO B 2

res = lg.parse("""{-- exemplo interpolação de strings
   Olá, EST IPCA! --}
escola ="EST";
inst = "IPCA";
ESCREVER ("Ola, #{escola} #{inst}!");""")

resultado = Eval.evaluate(res)
print("\n=_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_=\n")

# EXEMPLO B 3

res = lg.parse("""valor = ENTRADA();
ate10 = ALEATORIO(10);
ESCREVER ("#{valor}! #{ate10}!");""")

resultado = Eval.evaluate(res)
print("\n=_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_=\n")

## EXEMPLO D 1

res = lg.parse("""
lista = [ 1, 2, 3 ] ;
ESCREVER( lista ); -- [1,2,3]
vazia = [] ;
ESCREVER( vazia );""")

resultado = Eval.evaluate(res)
print("\n=_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_=\n")

# SE ==

res = lg.parse("""SE True == False FAZER:
               ESCREVER("ola1");
               FIM;
               SE True == True FAZER:
               ESCREVER("ola2");
               FIM;
               a = 1;
               b = 1;
               SE a == b FAZER:
               ESCREVER("ola3");
               FIM;
               a = 2;
               b = 3;
               SE a == b FAZER:
               ESCREVER("ola4");
               FIM;
               SE True != False FAZER:
               ESCREVER("adeus1");
               FIM;
               SE True != True FAZER:
               ESCREVER("adeus2");
               FIM;
               a = 1;
               b = 1;
               SE a != b FAZER:
               ESCREVER("adeus3");
               FIM;
               a = 2;
               b = 3;
               SE a != b FAZER:
               ESCREVER("adeus4");
               FIM;
               """)

resultado = Eval.evaluate(res)

print("\n=_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_=\n")

# SE > >= < <=

res = lg.parse("""a = 1;
               b = 1;
               SE a > b FAZER:
               ESCREVER("ola1");
               FIM;
               SE a >= b FAZER:
               ESCREVER("ola2");
               FIM;
               SE a < b FAZER:
               ESCREVER("ola3");
               FIM;
               SE a <= b FAZER:
               ESCREVER("ola4");
               FIM;
               a = 2;
               b = 3;
               SE a > b FAZER:
               ESCREVER("oi1");
               FIM;
               SE a >= b FAZER:
               ESCREVER("oi2");
               FIM;
               SE a < b FAZER:
               ESCREVER("oi3");
               FIM;
               SE a <= b FAZER:
               ESCREVER("oi4");
               FIM;
               a = 4;
               b = 2;
               SE a > b FAZER:
               ESCREVER("adeus1");
               FIM;
               SE a >= b FAZER:
               ESCREVER("adeus2");
               FIM;
               SE a < b FAZER:
               ESCREVER("adeus3");
               FIM;
               SE a <= b FAZER:
               ESCREVER("adeus4");
               FIM;""")

resultado = Eval.evaluate(res)

print("\n=_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_=\n")

# SE /\ \/

res = lg.parse("""a = 1;
               b = 2;
               c = True;
               d = False;
               SE a < b /\ c == d FAZER:
               ESCREVER("ola1");
               FIM;
               SE a < b \/ c == d FAZER:
               ESCREVER("ola2");
               FIM;
               SE a < b /\ c != d FAZER:
               ESCREVER("ola1");
               FIM;
               SE 3 < 2 /\ (1 != 2 \/ 1 == 2)  FAZER:
               ESCREVER("adeus1");
               FIM;
               SE (1 < 2 /\ 1 != 2) \/ 1 == 2 FAZER:
               ESCREVER("adeus2");
               FIM;
               SE 3 < 2 \/ (2 != 2 \/ 3 == 2) FAZER:
               ESCREVER("adeus3");
               FIM;
               """)

resultado = Eval.evaluate(res)

print("\n=_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_==_=\n")