from arith_grammar import ArithGrammar
from arith_eval import ArithEval

lg = ArithGrammar()
lg.build()

#res = lg.parse("""a = 2;
#               b = 3;
#               c = 2 + 3;
#               ESCREVER("Ola" <> " " <> b <> c);""");

res = lg.parse("""a = [1,2];
               ESCREVER(a[0]);
               """
)

resultado = ArithEval.evaluate(res)
