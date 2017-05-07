def semantic10(popedList):
	print(popedList)	

def sematic79(args):
	print(args)

def semanticIf(expression):
	global conditionsExecuted
	global valueCondition

	conditionsExecuted.append(0)	
	valueCondition.append(bool(expression))

def semanticElse(expression):
	global valueCondition

	valueCondition[-1] = not valueCondition[-1]

def semanticElif(expression):
	global valueCondition

	valueCondition[-1] = bool(expression)

def semantic69():
	Node("", list())





semantic_functions = {
	# "semanticIf" : semanticIf,
	# "semanticElse" : semanticElse,
	# "semanticElif" : semanticElif
}