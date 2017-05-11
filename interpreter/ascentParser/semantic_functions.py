import operator

from ascentParser.parser import InputToken

op = {
	'+'	: operator.pos,
	'-' : operator.neg,
	'~' : operator.invert
}


def semantic56(head, poppedList):    # In this instance poppedList must be [NUMBER,Si]
	number = poppedList[0].value
	lexeme = poppedList[0].lexeme
	result = InputToken(head, number)
	
	for operation in reversed(poppedList[1].value): 
		result.value = op[operation](result.value)
		
	return result

def semantic66(head, poppedList):
	poppedList[1].value.append("+")
	return poppedList[1]

def semantic67(head, poppedList):
	poppedList[1].value.append("-")
	return poppedList[1]

def semantic68(head, poppedList):
	poppedList[1].value.append("~")
	return poppedList[1]

def semantic69(head, poppedList):	
	return InputToken(head, [])



semantic_functions = {
	56: semantic56,
	66:	semantic66,
	67: semantic67,
	68: semantic68,
	69: semantic69
}
