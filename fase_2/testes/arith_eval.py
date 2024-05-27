# arith_eval
import random


class ArithEval:
    symbols = {}

    operators = {
        "+": lambda args: args[0] + args[1],
        "-": lambda args: args[0] - args[1],
        "*": lambda args: args[0] * args[1],
        "/": lambda args: args[0] / args[1],
        "seq": lambda args: args[-1],
        "atr": lambda args: ArithEval._attrib(args),
        "esc": lambda args: print(''.join(map(str, args))),
        "al": lambda args: random.randint(1, args[0]),
        "ent": lambda: input(),
    }

    @staticmethod
    def _attrib(args):  # A=10   {'op':'atr'  args: [ "A", 10 ]}
        value = args[1]
        ArithEval.symbols[args[0]] = value  # symbols['A'] = 10
        # return None
        return value

    def convert_input(input):
        # Try to convert to int
        try:
            return int(input)
        except ValueError:
            pass

        # Try to convert to float (to handle cases where user input might be a decimal number)
        try:
            return float(input)
        except ValueError:
            pass

        # If both conversions fail, return the input as a string
        return input

    @staticmethod
    def evaluate(ast):
        if type(ast) is int:  # constant value, eg in (int, str)
            return ast
        if type(ast) is dict:  # { 'op': ... , 'args': ...}
            return ArithEval._eval_operator(ast)
        if ast == "input":
            func = ArithEval.operators["ent"]
            input = ArithEval.convert_input(func())
            return input
        if type(ast) is str:
            return ast
        if type(ast) is list:
            return ast
        raise Exception(f"Unknown AST type")

    @staticmethod
    def _eval_operator(ast):
        if 'op' in ast:
            op = ast["op"]
            args = [ArithEval.evaluate(a) for a in ast['args']]
            if op in ArithEval.operators:
                func = ArithEval.operators[op]
                return func(args)
            else:
                raise Exception(f"Unknown operator {op}")

        if 'var' in ast:
            varid = ast["var"]
            if 'index' in ast:
                index = ast["index"]
                if varid in ArithEval.symbols:
                    return ArithEval.symbols[varid][index]
            if varid in ArithEval.symbols:
                return ArithEval.symbols[varid]
            raise Exception(f"error: local variable '{varid}' referenced before assignment")

        #

        raise Exception('Undefined AST')

