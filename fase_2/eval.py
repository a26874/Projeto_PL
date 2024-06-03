# eval
import random


class Eval:
    symbols = {}
    functions = {}
    se = True
    operators = {
        "+": lambda args: args[0] + args[1],
        "-": lambda args: args[0] - args[1],
        "*": lambda args: args[0] * args[1],
        "/": lambda args: args[0] / args[1],
        "seq": lambda args: args[-1],
        "atr": lambda args: Eval._attrib(args),
        "esc": lambda args: Eval._escrever(args),
        "al": lambda args: random.randint(1, args[0]),
        "ent": lambda: input(),
        "ou": lambda args: args[0] or args[1],
        "e": lambda args: args[0] and args[1],
        "SE": lambda args: args[-1],
        'HIGHER':   lambda args: Eval.compare_and_assign(args[0], args[1], '>'),
        'HIGHEREQ': lambda args: Eval.compare_and_assign(args[0], args[1], '>='),
        'LOWER':    lambda args: Eval.compare_and_assign(args[0], args[1], '<'),
        'LOWEREQ':  lambda args: Eval.compare_and_assign(args[0], args[1], '<='),
        'EQUALITY': lambda args: Eval.compare_and_assign(args[0], args[1], '=='),
        'DIFF':     lambda args: Eval.compare_and_assign(args[0], args[1], '!='),

        'AND': lambda args: Eval.compare_and_assign(args[0], args[1], 'and'),
        'OR': lambda args: Eval.compare_and_assign(args[0], args[1], 'or'),

        # "FUNCAO": lambda args: Eval.funcao(args),
    }

    comparators = {
        '>': lambda args: args[0] > args[1],
        '>=': lambda args: args[0] >= args[1],
        '<': lambda args: args[0] < args[1],
        '<=': lambda args: args[0] <= args[1],
        '==': lambda args: args[0] == args[1],
        '!=': lambda args: args[0] != args[1],
        'and': lambda args: args[0] and args[1],
        'or': lambda args: args[0] or args[1],
    }

    @staticmethod
    def compare_and_assign(x, y, comparator_name):
        if comparator_name in Eval.comparators:
            comparator = Eval.comparators[comparator_name]
            Eval.se = comparator([x, y])
            return Eval.se
        else:
            raise ValueError(f"Invalid variables")

    @staticmethod
    def _escrever(args):
        formatted_str = ''.join(map(str, args))
        formatted_str = Eval.replace_placeholders(formatted_str)
        print(formatted_str)
        
    def replace_placeholders(s):
        start = 0
        while True:
            start = s.find("#{", start)
            if start == -1:
                break
            end = s.find("}", start)
            if end == -1:
                break
            var_name = s[start+2:end]
            var_value = str(Eval.symbols.get(var_name, f"{{{var_name}}}"))
            s = s[:start] + var_value + s[end+1:]
            start += len(var_value)
        return s

    @staticmethod
    def _eval_se(args):
        return

    # def funcao(args):
    #     function = {}
    #     function[args[0]] = {}
    #     function[args[0]]['args'] = []
    #     for v in args[1]:
    #         function[args[0]]['args'][v] = ""
    #     function[args[0]]['body'] = args[2]
    #     print(Eval.functions)

    def convert_input(input):
        # Try to convert to int
        try:
            return int(input)
        except ValueError:
            pass
        try:
            return float(input)
        except ValueError:
            pass
        return input
    @staticmethod
    def _attrib(args):  # A=10   {'op':'atr'  args: [ "A", 10 ]}
        value = args[1]
        Eval.symbols[args[0]] = value  # symbols['A'] = 10
        return value

    @staticmethod
    def evaluate(ast):
        if type(ast) is int:  # constant value, eg in (int, str)
            return ast
        if type(ast) is dict:  # { 'op': ... , 'args': ...}
            return Eval._eval_operator(ast)
        if type(ast) is bool:
            return ast
        if ast == "input":
            func = Eval.operators["ent"]
            input = Eval.convert_input(func())
            return input
        if type(ast) is str:
            return ast
        if type(ast) is list:
            return ast
        raise Exception(f"Unknown AST type")

    @staticmethod
    def _eval_operator(ast):
        if Eval.se:
            if 'op' in ast:
                op = ast["op"]
                args = [Eval.evaluate(a) for a in ast['args']]
                if op in Eval.operators:
                    func = Eval.operators[op]
                    return func(args)
                else:
                    raise Exception(f"Unknown operator {op}")

            if 'var' in ast:
                varid = ast["var"]
                if 'index' in ast:
                    index = ast["index"]
                    if varid in Eval.symbols:
                        return Eval.symbols[varid][index]
                if varid in Eval.symbols:
                    return Eval.symbols[varid]
                raise Exception(f"error: local variable '{varid}' referenced before assignment")
        else:
            Eval.se = True
            return 'not exec'
        #

        raise Exception('Undefined AST')

