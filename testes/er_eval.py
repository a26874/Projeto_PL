class ExpReg:
    #recebe 2 dicionarios de transição,renumeia os estados e coloca um novo estado atras deles e a frente com fecho €.
    char = 65
    transições_global = {}
    def single_simbol(simbol):
        transição = {'q0':{f'{simbol}':['q1']},'inicial':["q0"],'final':["q1"]}
        return transição

    def cria_altera_dicionario(transição,estados,nome_transição):
        keysdicionario = {}
        for key in transição.keys():
            if key != 'final' and key != 'inicial':
                if key not in keysdicionario.keys():
                    keysdicionario[key] = f'{nome_transição}{estados}'
                    estados += 1
            else:
                for valor in transição[key]:
                    if valor not in keysdicionario.keys():
                        keysdicionario[valor] = f'{nome_transição}{estados}'
                        estados += 1
        return  keysdicionario,estados

    def alt(args):      
        estados = 0
        novo_dicionario_um = {}
        novo_dicionario_dois = {}
        if args[0].count("(") > (args[0].count("*")+ args[0].count("+")+args[0].count("|")):
            if f'{args[0]}'.lstrip('(').rstrip(')') in ExpReg.transições_global.keys():
                transições_um = ExpReg.transições_global[f'{args[0]}'.lstrip('(').rstrip(')')]
            else:
                transições_um = ExpReg.single_simbol(args[0])
        else:
            if f'{args[0]}' in ExpReg.transições_global.keys():
                transições_um = ExpReg.transições_global[f'{args[0]}']
            else:
                transições_um = ExpReg.single_simbol(args[0])

        if args[1].count("(") > (args[1].count("*")+ args[1].count("+")+args[1].count("|")):
            if f'{args[1]}'.lstrip('(').rstrip(')') in ExpReg.transições_global.keys():
                transições_dois = ExpReg.transições_global[f'{args[1]}'.lstrip('(').rstrip(')')]
            else:
                transições_dois = ExpReg.single_simbol(args[1])
        else:
            if f'{args[1]}' in ExpReg.transições_global.keys():
                transições_dois = ExpReg.transições_global[f'{args[1]}']
            else:
                transições_dois = ExpReg.single_simbol(args[1])

        nome_transição = chr(ExpReg.char)
        ExpReg.char += 1
        keys_dicionario_um,estados = ExpReg.cria_altera_dicionario(transições_um,estados,nome_transição)
        keys_dicionario_dois,estados = ExpReg.cria_altera_dicionario(transições_dois, estados, nome_transição)
        transitor = {}

        novo_dicionario_final = {}
        #" ----------------------       um       -------------------------------------------"
        for key, value in transições_um.items():
            if key != 'final' and key != 'inicial':
                chave = keys_dicionario_um[key]
                for simbolo, lista in value.items():
                    transitor[simbolo] = []
                    for estado in lista:
                        transitor[simbolo].append(keys_dicionario_um[estado])
                    novo_dicionario_um[chave] = transitor.copy()
                    transitor.clear()
        novo_dicionario_um['inicial'] = []
        novo_dicionario_um['final'] = []
        for value in transições_um['inicial']:
            chave = keys_dicionario_um[value]
            novo_dicionario_um['inicial'].append(chave)
            novo_dicionario_um[chave]
        for value in transições_um['final']:
            chave = keys_dicionario_um[value]
            novo_dicionario_um['final'].append(chave)
        novo_dicionario_final.update(novo_dicionario_um)

    # " ---------------------------------------------------------------------------"

    #" ----------------------      dois        -------------------------------------------"
        for key, value in transições_dois.items():
            if key != 'final' and key != 'inicial':
                chave = keys_dicionario_dois[key]
                for simbolo, lista in value.items():
                    transitor[simbolo] = []
                    for estado in lista:
                        transitor[simbolo].append(keys_dicionario_dois[estado])
                    novo_dicionario_dois[chave] = transitor.copy()
                    transitor.clear()
        novo_dicionario_dois['inicial'] = []
        novo_dicionario_dois['final'] = []
        for value in transições_dois['inicial']:
            chave = keys_dicionario_dois[value]
            novo_dicionario_dois['inicial'].append(chave)
        for value in transições_dois['final']:
            chave = keys_dicionario_dois[value]
            novo_dicionario_dois['final'].append(chave)
        novo_dicionario_final.update(novo_dicionario_dois)
    #" ---------------------------------------------------------------------------"
        novo_dicionario_final.pop('inicial')
        novo_dicionario_final.pop('final')
        novo_dicionario_final['inicial'] = ['q0']
        novo_dicionario_final['final'] = ['q1']
        novo_dicionario_final['q0'] = {}
        novo_dicionario_final['q0']['€'] = []
        for value in novo_dicionario_um['inicial']:
            novo_dicionario_final['q0']['€'].append(value)
        for value in novo_dicionario_dois['inicial']:
            novo_dicionario_final['q0']['€'].append(value)
        for value in novo_dicionario_um['final']:
            if value not in novo_dicionario_final:
                novo_dicionario_final[value] = {}
                novo_dicionario_final[value]['€'] = []
            elif '€' not in novo_dicionario_final[value]:
                novo_dicionario_final[value]['€'] = []
            novo_dicionario_final[value]['€'].append('q1')
        for value in novo_dicionario_dois['final']:
            if value not in novo_dicionario_final:
                novo_dicionario_final[value] = {}
                novo_dicionario_final[value]['€'] = []
            elif '€' not in novo_dicionario_final[value]:
                novo_dicionario_final[value]['€'] = []
            novo_dicionario_final[value]['€'].append('q1')
        ExpReg.transições_global[f'{args[0]}|{args[1]}'] = {}
        ExpReg.transições_global[f'{args[0]}|{args[1]}'] = novo_dicionario_final
        return f'{args[0]}|{args[1]}'


    def seq(args):
        estados = 0
        novo_dicionario_um = {}
        novo_dicionario_dois = {}
        if args[0].count("(") > (args[0].count("*")+ args[0].count("+")+args[0].count("|")):
            if f'{args[0]}'.lstrip('(').rstrip(')') in ExpReg.transições_global.keys():
                transições_um = ExpReg.transições_global[f'{args[0]}'.lstrip('(').rstrip(')')]
            else:
                transições_um = ExpReg.single_simbol(args[0])
        else:
            if f'{args[0]}' in ExpReg.transições_global.keys():
                transições_um = ExpReg.transições_global[f'{args[0]}']
            else:
                transições_um = ExpReg.single_simbol(args[0])

        if args[1].count("(") > (args[1].count("*")+ args[1].count("+")+args[1].count("|")):
            if f'{args[1]}'.lstrip('(').rstrip(')') in ExpReg.transições_global.keys():
                transições_dois = ExpReg.transições_global[f'{args[1]}'.lstrip('(').rstrip(')')]
            else:
                transições_dois = ExpReg.single_simbol(args[1])
        else:
            if f'{args[1]}' in ExpReg.transições_global.keys():
                transições_dois = ExpReg.transições_global[f'{args[1]}']
            else:
                transições_dois = ExpReg.single_simbol(args[1])

        nome_transição = chr(ExpReg.char)
        ExpReg.char += 1
        keys_dicionario_um, estados = ExpReg.cria_altera_dicionario(transições_um, estados, nome_transição)
        keys_dicionario_dois, estados = ExpReg.cria_altera_dicionario(transições_dois, estados, nome_transição)
        transitor = {}

        novo_dicionario_final = {}
        # " ----------------------       um       -------------------------------------------"
        for key, value in transições_um.items():
            if key != 'final' and key != 'inicial':
                chave = keys_dicionario_um[key]
                for simbolo, lista in value.items():
                    transitor[simbolo] = []
                    for estado in lista:
                        transitor[f'{simbolo}'].append(keys_dicionario_um[estado])
                    novo_dicionario_um[chave] = transitor.copy()
                    transitor.clear()
        novo_dicionario_um['inicial'] = []
        novo_dicionario_um['final'] = []
        for value in transições_um['inicial']:
            chave = keys_dicionario_um[value]
            novo_dicionario_um['inicial'].append(chave)
            novo_dicionario_um[chave]
        for value in transições_um['final']:
            chave = keys_dicionario_um[value]
            novo_dicionario_um['final'].append(chave)
        novo_dicionario_final.update(novo_dicionario_um)

        # " ---------------------------------------------------------------------------"

        # " ----------------------      dois        -------------------------------------------"
        for key, value in transições_dois.items():
            if key != 'final' and key != 'inicial':
                chave = keys_dicionario_dois[key]
                for simbolo, lista in value.items():
                    transitor[simbolo] = []
                    for estado in lista:
                        transitor[simbolo].append(keys_dicionario_dois[estado])
                    novo_dicionario_dois[chave] = transitor.copy()
                    transitor.clear()
        novo_dicionario_dois['inicial'] = []
        novo_dicionario_dois['final'] = []
        for value in transições_dois['inicial']:
            chave = keys_dicionario_dois[value]
            novo_dicionario_dois['inicial'].append(chave)
        for value in transições_dois['final']:
            chave = keys_dicionario_dois[value]
            novo_dicionario_dois['final'].append(chave)
        novo_dicionario_final.update(novo_dicionario_dois)
        # " ---------------------------------------------------------------------------"

        for keys_one in novo_dicionario_um['final']:
            if keys_one not in novo_dicionario_final:
                novo_dicionario_final[keys_one] = {}
            novo_dicionario_final[keys_one]['€'] = []
            for keys_two in novo_dicionario_dois['inicial']:
                novo_dicionario_final[keys_one]['€'].append(keys_two)
        novo_dicionario_final.pop('inicial')
        novo_dicionario_final.pop('final')
        novo_dicionario_final['inicial'] = ['q0']
        novo_dicionario_final['final'] = ['q1']
        novo_dicionario_final['q0'] = {}
        novo_dicionario_final['q0']['€'] = []
        for value in novo_dicionario_um['inicial']:
            novo_dicionario_final['q0']['€'].append(value)
        for value in novo_dicionario_dois['final']:
            if value not in novo_dicionario_final:
                novo_dicionario_final[value] = {}
                novo_dicionario_final[value]['€'] = []
            elif '€' not in novo_dicionario_final[value]:
                novo_dicionario_final[value]['€'] = []
            novo_dicionario_final[value]['€'].append('q1')
        ExpReg.transições_global[f'{args[0]}{args[1]}'] = {}
        ExpReg.transições_global[f'{args[0]}{args[1]}'] = novo_dicionario_final
        return f'{args[0]}{args[1]}'


    def kle(args):
        if args[0].count("(") > (args[0].count("*")+ args[0].count("+")+args[0].count("|")):
            if f'{args[0]}'.lstrip('(').rstrip(')') in ExpReg.transições_global.keys():
                transições_um = ExpReg.transições_global[f'{args[0]}'.lstrip('(').rstrip(')')]
            else:
                transições_um = ExpReg.single_simbol(args[0])
        else:
            if f'{args[0]}' in ExpReg.transições_global.keys():
                transições_um = ExpReg.transições_global[f'{args[0]}']
            else:
                transições_um = ExpReg.single_simbol(args[0])

        estados = 0
        keysdicionario = {}
        novo_dicionario = {}
        if type(transições_um) is dict:
            nome_transição = chr(ExpReg.char)
            ExpReg.char += 1
            keysdicionario,estados = ExpReg.cria_altera_dicionario(transições_um,estados,nome_transição)
            #pode virar função
            transitor = {}
            for key, value in transições_um.items():
                if key != 'final' and key != 'inicial':
                    chave = keysdicionario[key]
                    for simbolo,lista in value.items():
                        transitor[simbolo] = []
                        for estado in lista:
                            transitor[simbolo].append(keysdicionario[estado])
                        novo_dicionario[chave] = transitor.copy()
                        transitor.clear()
            #a cima
            for value in transições_um['inicial']:
                chave = keysdicionario[value]
                novo_dicionario['q0'] = {'€': [chave]}
            for value in transições_um['final']:
                chave = keysdicionario[value]
                if chave not in novo_dicionario:
                    novo_dicionario[chave] = {}
                    novo_dicionario[chave]['€'] = []
                    for value in transições_um['inicial']:
                        chaveinicial = keysdicionario[value]
                        novo_dicionario[chave]['€'].append(chaveinicial)
                    novo_dicionario[chave]['€'].append('q1')
                else:
                    novo_dicionario[chave]['€'] = []
                    novo_dicionario[chave]['€'].append('q1')
            novo_dicionario['inicial'] = ['q0']
            novo_dicionario['final'] = ['q1']
            novo_dicionario['q0']['€'].append('q1')
            ExpReg.transições_global[f'{args[0]}*'] = {}
            ExpReg.transições_global[f'{args[0]}*'] = novo_dicionario
            return f'{args[0]}*'
        else:
            transições_um = {'q0':{'€':['q1','q3']},'q1':{f'{args[0]}':['q2']},'q2':{'€':['q3','q1']},'inicial':["q0"],'final':["q3"]}
            ExpReg.transições_global[f'{args[0]}*'] = {}
            ExpReg.transições_global[f'{args[0]}*'] = transições_um
            return f'{args[0]}*'



    def trans(args):
        if args[0].count("(") > (args[0].count("*")+ args[0].count("+")+args[0].count("|")):
            if f'{args[0]}'.lstrip('(').rstrip(')') in ExpReg.transições_global.keys():
                transições_um = ExpReg.transições_global[f'{args[0]}'.lstrip('(').rstrip(')')]
            else:
                transições_um = ExpReg.single_simbol(args[0])
        else:
            if f'{args[0]}' in ExpReg.transições_global.keys():
                transições_um = ExpReg.transições_global[f'{args[0]}']
            else:
                transições_um = ExpReg.single_simbol(args[0])

        estados = 0
        keysdicionario = {}
        novo_dicionario = {}
        if type(transições_um) is dict:
            nome_transição = chr(ExpReg.char)
            ExpReg.char += 1
            keysdicionario,estados = ExpReg.cria_altera_dicionario(transições_um,estados,nome_transição)
            transitor = {}
            for key, value in transições_um.items():
                if key != 'final' and key != 'inicial':
                    chave = keysdicionario[key]
                    for simbolo,lista in value.items():
                        transitor[simbolo] = []
                        for estado in lista:
                            transitor[simbolo].append(keysdicionario[estado])
                        novo_dicionario[chave] = transitor.copy()
                        transitor.clear()
            for value in transições_um['inicial']:
                chave = keysdicionario[value]
                novo_dicionario['q0'] = {'€': [chave]}
            for value in transições_um['final']:
                chave = keysdicionario[value]
                if chave not in novo_dicionario:
                    novo_dicionario[chave] = {}
                    novo_dicionario[chave]['€'] = []
                    for value in transições_um['inicial']:
                        chaveinicial = keysdicionario[value]
                        novo_dicionario[chave]['€'].append(chaveinicial)
                    novo_dicionario[chave]['€'].append('q1')
                else:
                    novo_dicionario[chave]['€'] = []
                    novo_dicionario[chave]['€'].append('q1')
            novo_dicionario['inicial'] = ['q0']
            novo_dicionario['final'] = ['q1']
            ExpReg.transições_global[f'{args[0]}+'] = {}
            ExpReg.transições_global[f'{args[0]}+'] = novo_dicionario
            return f'{args[0]}+'
        else:
            transições_um = {'q0':{'€':['q1']},'q1':{f'{args[0]}':['q2']},'q2':{'€':['q3','q1']},'inicial':["q0"],'final':["q3"]}
            ExpReg.transições_global[f'{args[0]}+'] = {}
            ExpReg.transições_global[f'{args[0]}+'] = transições_um
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

    def execução(arv):
        expression, _ = ExpReg.evaluate(arv)
        return expression,ExpReg.transições_global
