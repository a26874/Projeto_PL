class ExpReg:
    #recebe 2 dicionarios de transição,renumeia os estados e coloca um novo estado atras deles e a frente com fecho €.

    def alt(args):
        return f'{args[0]}|{args[1]}'

    def seq(args):
        return f'{args[0]}{args[1]}'

    def kle(args):
        return f'{args[0]}*'

    def trans(args):
        return f'{args[0]}+'

    def opc(args):
        return f'{args[0]}?'

    operadores = {
		"alt": (alt, 0),
		"seq": (seq, 1),
		"kle": (kle, 2),
		"trans": (trans, 2),
		"opc": (opc, 2)
    }

    def evaluate(arv: dict) -> (str, int):
        if type(arv) is dict:
            return ExpReg._eval_operator(arv)
        raise Exception("O tipo de dados encontrado na árvore da expressão regular é desconhecido")

    def _eval_operator(arv: dict) -> (str, int):
        if 'op' in arv:
            op = arv["op"]
            args = [ExpReg.evaluate(a) for a in arv['args']]
            if op in ExpReg.operadores:
                op_func = ExpReg.operadores[op][0]
                op_priority = ExpReg.operadores[op][1]
                args_res = list(map(
                    lambda a: a[0] if (op_priority < a[1]) else f'({a[0]})',
                    args))
                return (op_func(args_res), op_priority)
            else:
                raise Exception(f"operador desconhecido {op}")
        if 'simb' in arv: #mudar para devolver o valor da função, isto sera a transição
            simbolo = arv['simb']
            return (simbolo, 3)
        if 'epsilon' in arv:
            return ('ε', 3)
        raise Exception('A árvore da expressão regular não é válida!')

    