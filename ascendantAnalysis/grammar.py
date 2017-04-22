from lexicalAnalysis.lexicalAnalyzer import *

##################### Functions ####################
def semantic9():
	print('Semantic 9')

def semantic8():
	print('Semantic 8')

def semantic46():
	print('Semantic 46')

####################################################

rules = {
	'Sx' : {
		'A_aug;Sx' : 0,
		'A_sim;Sx' : 1,
		'A_dro;Sx' : 2,
		'A_aug;' : 3,
		'A_sim;' : 4,
		'A_dro;' : 5,
		'CtrlSx' : 6,
		'Ctrl' : 7
	},
	'A_aug' : {
		'IDAoEx': 8
	},
	'A_sim' : {
		'ID=Ex' : {
			'number': 9,
			'semantic': semantic9
		}
	},
	'A_dro' : {
		'IDDc' : 10
	},
	'Ao' : {
		'+=' : 11,
		'-=' : 12,
		'*=' : 13,
		'/=' : 14,
		'%=' : 15,
		'>>=' : 16,
		'<<=' : 17,
		'&=' : 18,
		'|=' : 19,
		'^=' : 20,
		'**=' : 21
	},
	'Ex' : {
		'Or_l' : 22
	},
	'Or_l' : {
		'Or_l||And_l' : 23,
		'And_l' : 24
	},
	'And_l' : {
		'And_l&&Not_l' : 25,
		'Not_l' : 26
	},
	'Not_l' : {
		'!Not_l' : 27,
		'Lx' : 28
	},
	'Lx' : {
		'LxLoOr_b' : 29,
		'Or_b' : 30
	},
	'Lo' : {
		'<' : 31,
		'>' : 32,
		'<=' : 33,
		'>=' : 34,
		'==' : 35,
		'!=' : 36
	},
	'Or_b' : {
		'Or_b|Xor_b' : 37,
		'Xor_b' : 38
	},
	'Xor_b' : {
		'Xor_b^And_b' : 39,
		'And_b' : 40
	},
	'And_b' : {
		'And_b&Shift' : 41,
		'Shift' : 42
	},
	'Shift': {
		'Shift>>Ax' : 43,
		'Shift<<Ax' : 44,
		'Ax' : 45
	},
	'Ax' : {
		'Ax+Af' : 46,
		'Ax-Af' : 47,
		'Af' : 48
	},
	'Af' : {
		'Af*Ap' : 49,
		'Af%Ap' : 50,
		'Af/Ap' : 51,
		'Ap' : 52
	},
	'Ap' : {
		'At**Ap' : 53,
		'At' : 54
	},
	'At' : {
		'-NUMBER' : 55,
		'NUMBER' : 56,
		'STRING' : 57,
		'-ID': 58,
		'ID' : 59,
		'-(Ex)': 60,
		'(Ex)' : 61,
	},
	'Dc' : {
		'=**(STRING,NUMBER)**' : 62,
		'-<(Ex,Ex,Ex)' : 63,
		'-)(Ex,Ex,Ex)' : 64
	},
	'Ctrl' : {
		'For' : 65,
		'While' : 66,
		'If' : 67
	},
	'For' : {
		'for(ID:(Ex,Ex)){Sx}' : 68
	},
	'While' : {
		'while(Ex){Sx}' : 69
	},
	'If' : {
		'if(Ex){Sx}' : 70,
		'if(Ex)else{Sx}' : 71
	}
}

class Singleton(type):
	_instances = {}
	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
		return cls._instances[cls]

class Grammar(object):
	__metaclass__ = Singleton

	def __init__(self, grammarPattern):
		self.grammar = {}
		tokenizer = Token(grammarPattern)
		for rule in rules:
			for production in rules[rule]:
				#print("Production : \n" , production)
				#print("rules[rule]: \n", rules[rule])
				#print("rules[rule][production]: \n", rules[rule][production])
				tokens = []
				for tupleToken in tokenizer.tokenizeText(production):
					tokens.append(tupleToken[1])

				hasSemantic = True if (type(rules[rule][production]) is dict and 'semantic' in rules[rule][production]) else False
				indexRule, semantic = None, None
				if (hasSemantic):
					indexRule = rules[rule][production]['number']
					semantic = rules[rule][production]['semantic']
					self.grammar[indexRule] = rule, tokens, semantic
				else:
					indexRule = rules[rule][production]
					self.grammar[indexRule] = rule, tokens
				#print("IndexRule : \n" , indexRule)
				#print("Tokens : \n" , tokens)
				#print("\n\n")

	def getGrammar(self):
		return self.grammar