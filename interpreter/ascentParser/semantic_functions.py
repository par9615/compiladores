import operator

from ascentParser.parser import InputToken

op = {
	'+'	: operator.pos,
	'-' : operator.neg,
	'~' : operator.invert,
	'**' : operator.pow,
	'/' : operator.truediv,
	'%' : operator.mod,
	'*' : operator.mul,
	'<<' : operator.lshift,
	'>>' : operator.rshift
}

def semantic44(head, poppedList):
	operator = poppedList[1].lexeme
	number = poppedList[2].value
	shift = poppedList[0].value
	return InputToken(head, op[operator](number, shift))

def semantic45(head, poppedList):
	operator = poppedList[1].lexeme
	number = poppedList[2].value
	shift = poppedList[0].value
	return InputToken(head, op[operator](number, shift))

def semantic46(head, poppedList):
	poppedList[0].lexeme = head
	return poppedList[0]

def semantic47(head, poppedList):
	sumand1 = poppedList[2].value
	sumand2 = poppedList[0].value
	return InputToken(head, sumand1 + sumand2)

def semantic48(head, poppedList):
	minuend = poppedList[2].value
	substraend = poppedList[0].value
	return InputToken(head, minuend - substraend)

def semantic49(head, poppedList):
	poppedList[0].lexeme = head
	return poppedList[0]

def semantic50(head, poppedList):
	operator = poppedList[1].lexeme
	factor1 = poppedList[2].value
	factor2 = poppedList[0].value
	return InputToken(head, op[operator](factor1, factor2))

def semantic51(head, poppedList):
	operator = poppedList[1].lexeme
	dividend = poppedList[2].value
	divisor = poppedList[0].value
	return InputToken(head, op[operator](dividend, divisor))

def semantic52(head, poppedList):
	operator = poppedList[1].lexeme
	dividend = poppedList[2].value
	divisor = poppedList[0].value
	return InputToken(head, op[operator](dividend, divisor))

def semantic53(head, poppedList):
	poppedList[0].lexeme = head
	return poppedList[0]

def semantic54(head, poppedList):
	operator = poppedList[1].lexeme
	base = poppedList[2].value
	exponent = poppedList[0].value
	return InputToken(head, op[operator](base, exponent))

def semantic55(head, poppedList):
	poppedList[0].lexeme = head
	return poppedList[0]

def semantic56(head, poppedList):    # In this instance poppedList must be [NUMBER,Si]
	number = poppedList[0].value
	lexeme = poppedList[0].lexeme
	result = InputToken(head, number)
	
	for operation in reversed(poppedList[1].value): 
		result.value = op[operation](result.value)
		
	return result

def semantic57(head, poppedList):
	poppedList[0].lexeme = head
	return  poppedList[0]

def semantic58(head, poppedList):
	print("pendiente")

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
