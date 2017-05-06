from lexicalAnalysis.lexicalAnalyzer import *

class Parser(object):
	def __init__(self, pattern):
		self.tokenizer = Token(pattern)

	def parseInput(self, text):
		parsedLanguage = []
		for tupleToken in self.tokenizer.tokenizeText(text):
			if (tupleToken[0] == 'identifier'):
				parsedLanguage.append('ID')
			elif (tupleToken[0] == 'number' or tupleToken[0] == 'float'):
				parsedLanguage.append('NUMBER')
			elif (tupleToken[0] == 'string'):
				parsedLanguage.append('STRING')
			elif (tupleToken[0] == 'whitespace'):
				continue
			else:
				parsedLanguage.append(tupleToken[1])
		parsedLanguage.append('$')
		return parsedLanguage
