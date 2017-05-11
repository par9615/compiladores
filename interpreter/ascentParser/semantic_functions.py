import operator

from ascentParser.parser import InputToken

op = {
	
	

}


def sematic56(head, poppedList):
	number = poppedList[0].value
	result = InputToken(number, number)
	
	for i in len(poppedList[1].value):
		result.value = op[poppedList[1].value[i]](result.value)

	return result

def semantic66(head, poppedList):
	return poppedList[1].value.append("-")

def semantic67(head, poppedList):
	return poppedList[1].value.append("+")

def semantic68(head, poppedList):
	return poppedList[1].value.append("~")

def semantic69(head, poppedList):	
	return InputToken(head, [])



semantic_functions = {
	66:	semantic66,
	67: semantic67,
	68: semantic68,
	69: semantic69
}
