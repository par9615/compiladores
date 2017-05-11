################### Imports ########################
from ascentParser.grammar import grammar
from ascentParser.matrix import matrix
from ascentParser.parser import Parser, InputToken
from lexicalAnalysis.lexicalAnalyzer import *
from ascentParser.semantic_functions import semantic_functions
####################################################


##################### Patterns #####################
languagePattern = r"""
(?P<drone>drone)
|(?P<string>((?P<quote>['"]).*?(?P=quote)))
|(?P<leftCurly>[{])
|(?P<rightCurly>[}])
|(?P<leftBracket>[(])
|(?P<rightBracker>[)])
|(?P<endStatement>[;])
|(?P<droneFunction>(move_to|rotate))
|(?P<updater>(\+=|-=|\*=|/=|%=|>>=|<<=|&=|\|=|\^=|\*\*=))
|(?P<comparatorLarger>(<=|>=|==|!=))
|(?P<operatorLarger>(\|\| | && | \*\*))
|(?P<operator>(\+ | - | ~ | \* | % | / | >> | << | & | \| | \^ | !))
|(?P<comma>[,])
|(?P<comparator>(< | >))
|(?P<list>list\()
|(?P<pointOfIntereset>poi\()
|(?P<float>[0-9]?\.[0-9]+)
|(?P<number>[0-9]+)
|(?P<reservedWord>(while|if|for|else|elif))
|(?P<identifier>[a-zA-Z_$][a-zA-Z_$0-9]*)
|(?P<whitespace>\s+)
|(?P<twoDots>[:])
|(?P<equal>[=])
"""
####################################################


##################### Functions ####################
def contains(l, filter):
    function = False
    for value in l:
        if filter(value):
            function = True
            break
    return function

def parseObjectsToString(objects):
    outputString = ""
    for item in objects:
        outputString += item.lexeme
    return outputString

def getInitial(grammar):
   index = grammar.keys()
   return min(index)

def pushNextState(top, token):  #Hace un push en la pila del estado en matrix[top][token] -> "S5" hace stack.append(5)
    global stack
    state = getState(top,token)
    stack.append(state)

def shift(top, token):
    """state  = getState(top,token)

    if(state == 126):
        semantic_functions["semanticIf"]()

    elif(state == 162):
        semantic_funtions["semanticElif"]()

    elif(state == 154):
        semantic_funtions["semanticElse"]()*/"""



    global stack

def reduce(top, token): #Hace todo el procedimiento del reduce
    global stack
    global symbols

    state = getState(top, token.lexeme)
    semantic_function = None
    poppedList = []
    production = grammar[state]

    head = production[0]
    result = None
    rules  = production[1]

    if (not(len(rules) == 1 and rules[0] == b'\xce\xb5')):
        for i in range(0, len(rules)):
            stack.pop()
            poppedList.append(symbols.pop())

    

    pushNextState(stack[-1], head)
    


    #Si tiene acción semántica
    if(production[2]):
        result = semantic_functions[state](head, poppedList)

    symbols.append(result)

    ruleString = ""
    for rule in rules:
        ruleString += rule.decode('utf-8')

    return [head, ruleString], semantic_function

def action(top, token):             #Retorna la accion en matrix[top][token] -> "S5" return "S"
    action = matrix[top][token]
    return action

def getState(top, token):           #Retorna el estado en matrix[top][token] -> "S5" return int(5)
    return int(matrix[top][token][1:])

def handleError(top):
    global stack
    global tokens
    global symbols

    inputToken = tokens[0]
    validState = False

    while not validState:
        try:
            s = stack[-1]
            values = list(matrix[s].values())

            while not 'G' in ''.join(values):
                values = list(matrix[stack[-2]].values())
                stack.pop()
                s = stack[-1]

            for i in range(len(matrix[s]) - 1, -1, -1):
                l = list(matrix[s].values())
                k = list(matrix[s].keys())

                if 'G' in l[i]:
                    currVal = int(l[i][1:])
                    currKey = InputToken(k[i])

                    if 'S' in ''.join(list(matrix[currVal].values())):
                        stack.append(currVal)
                        symbols.pop()
                        symbols.append(currKey)
                        validState = True
                        break
        except:
            raise Exception('Received: ', inputToken, ' when expected one of the following: ', ''.join(list(matrix[s].keys())))
    s = currVal
    while not tokens[0].lexeme in matrix[currVal]:
        try:
            tokens.pop(0)
        except:
            raise Exception('Received: ', inputToken, ' when expected one of the following: ', ''.join(list(matrix[s].keys())))




def algorithm(inputString):
    global tokens
    global symbolsTable
    tokens = parser.parseInput(inputString)

    stack.append(initial)

    formattedString = "{:<39}\t{:<37}\t{:<37}\t{:>12}"

    print(formattedString.format("Pila", "Simbolos", "Entrada", "Accion"))
    output = []
    token = tokens[0]
    semantic_function = None

    while(1):
        output.append(" ".join(map(str,stack)))

        output.append(parseObjectsToString(symbols))

        output.append(parseObjectsToString(tokens))

        top = stack[-1]

        if(token.lexeme in matrix[top]):
            act = action(top, token.lexeme)

            if("S" in act): #Shift
                pushNextState(top,token.lexeme)
                symbols.append(token)
                tokens.pop(0)
                token = tokens[0]
                output.append("Shift " + act[1:])

            elif("R" in act): #Reduce
                rule,semantic_function = reduce(top,token)
                output.append("Reduce " + rule[0] + " -> " + rule[1])

            elif("A" in act): #Aceptado
                output.append("Aceptado")

            else:
                handleError(top)
                token = tokens[0]
                output.append("Error T")

        else:
            handleError(top)
            token = tokens[0]
            output.append("Error T")
        #cambiar este print
        print(formattedString.format(output[0], output[1], output[2], output[3]))
        if (semantic_function):
            semantic_function()

        if (output[-1] == "Aceptado"):
            break;

        del output[:]
####################################################


################# Global variables #################
stack = []
symbols = []
tokens = []
parser = Parser(languagePattern)
initial = getInitial(grammar)
symbolsTable = {}
valueCondition = []
conditionsExecuted = []
####################################################
