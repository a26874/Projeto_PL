from arith_grammar import ArithGrammar
from arith_eval import ArithEval

lg = ArithGrammar()
lg.build()

#res = lg.parse("""a = 2;
#               b = 3;
#               c = 2 + 3;
#               ESCREVER("Ola" <> " " <> b <> c);""");

res = lg.parse("""a = ENTRADA();
               b = 2;
               c = a + b;
               ESCREVER(c);
               """
)

resultado = ArithEval.evaluate(res)
