# arith_eval

class ArithEval:

	symbols = {}

	operators = {
		"+": lambda args: args[0] + args[1],
		"-": lambda args: args[0] - args[1],
		"*": lambda args: args[0] * args[1],
  		"/": lambda args: args[0] / args[1],
		"seq": lambda args: args[-1],
		"atr": lambda args: ArithEval._attrib(args),
		"esc": lambda args: print(args[0]),
	}

	@staticmethod
	def _attrib(args): # A=10   {'op':'atr'  args: [ "A", 10 ]} 
		value = args[1]
		ArithEval.symbols[args[0]] = value   # symbols['A'] = 10
		#return None
		return value
    
	@staticmethod
	def evaluate(ast):
		if type(ast) is int:  # constant value, eg in (int, str)
			return ast
		if type(ast) is dict: # { 'op': ... , 'args': ...}
			return ArithEval._eval_operator(ast)
		if type(ast) is str: 
			return ast
		raise Exception(f"Unknown AST type")
        
	@staticmethod
	def _eval_operator(ast):
		if 'op' in ast:
			op = ast["op"]
			args = [ArithEval.evaluate(a) for a in ast['args']]
			if op in ArithEval.operators:
				func = ArithEval.operators[op]
				if(op in "+-/*" ):
					i = 0
					for i,arg in enumerate(args):
						if(arg in ArithEval.symbols):
							args[i] = ArithEval.symbols[arg]
				return func(args)
			else:
				raise Exception(f"Unknown operator {op}")

		if 'var' in ast:
			varid = ast["var"]
			if varid in ArithEval.symbols:
				return ArithEval.symbols[varid]
			raise Exception(f"error: local variable '{varid}' referenced before assignment") 
			#

		raise Exception('Undefined AST')

