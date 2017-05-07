################### Imports ########################
import re
from ascentParser.grammar import grammar
from ascentParser.matrix import matrix
from ascentParser.parser import Parser
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

def getInitial(grammar):
   index = grammar.keys()
   return min(index)

def pushNextState(top, token):  #Hace un push en la pila del estado en matrix[top][token] -> "S5" hace stack.append(5)
    global stack
    state = getState(top,token)
    stack.append(state)

def shift(top, token):   #No hace nada
    global stack

def reduce(top, token): #Hace todo el procedimiento del reduce
    global stack
    global symbols

    state = getState(top, token)
    semantic_function = None

    production = grammar[state]

    rules  = production[1]
    head = production[0]

    if (not(len(rules) == 1 and rules[0] == b'\xce\xb5')):
        for i in range(0, len(rules)):
            stack.pop()
            symbols.pop()
    symbols.append(head)

    pushNextState(stack[-1], head)

    if(production[2]):
        semantic_function = semantic_functions[state]

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

    print('stack',stack)
    print('entrada', tokens)

    #  Pop states from stack, until one with shift is found
    while not validState:
        try:
            last = -1
            s = stack[-1]

            values = list(matrix[s].values())
            print(''.join(values))
            # Pop states until we get a state that has a goto
            while not 'G' in ''.join(values) or s == last:
                last = s
                s = stack.pop()
                values = list(matrix[s].values())
            print(''.join(values))
            print('stack af', stack)
            print('top af', s)
            print('entrada af', tokens)

            #checar todos los goto's
            for i in range(len(matrix[s]) - 1, -1, -1):
                l = list(matrix[s].values())
                print('ele', l)
                curr = int(l[i][1:])
                #print('curr', curr)
                #print(''.join(list(matrix[curr].values())))
                if 'S' in ''.join(list(matrix[curr].values())):
                    #print('succ')
                    stack.append(curr)
                    validState = True
                    print(stack)
            last = s
            s = stack.pop()
        except:
            raise Exception('Parsing aborted, expected elements:', ''.join(list(matrix[s].keys())), ' Received:', inputToken)
    print('recovered state', stack)
    s = stack[-1]

    while not inputToken in matrix[s]:
        try:
            inputToken = tokens.pop()
        except:
            raise Exception('Parsing aborted, expected elements:', ''.join(list(matrix[s].keys())) , ' Received:', inputToken)





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

        output.append("".join(symbols))

        output.append("".join(tokens))

        top = stack[-1]

        if(token in matrix[top]):
            act = action(top, token)

            if("S" in act): #Shift
                pushNextState(top,token)
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
####################################################