import operator

from parser import *

op = {
	'+'	: operator.pos
}


def semantic56(head, poppedList):
	number = poppedList[0].value
	result = InputToken(number, number)
	
	for i in len(poppedList[1].value):
		result.value = op[poppedList[1].value[i]](result.value)

	return result

def semantic66(head, poppedList):
	poppedList[1].value.append("-")
	return poppedList[1]

def semantic67(head, poppedList):
	poppedList[1].value.append("+")
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
