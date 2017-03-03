stack = []
tokens = ["id","*","id","+","id","$"]
symbols = []
terminals = []
nonTerminals = []
initial = 0

matrix = {

    0 : {
        "id":   "S5",
        "(" :   "S4" ,
        "E" :   "G1",
        "T" :   "G2",
        "F" :   "G3"
    },

    1: {
        "+":    "S6",
        "$":    "AC"
    },

    2: {
        "+":    "R2",
        "*":    "S7",
        ")":    "R2",
        "$":    "R2"
    },

    3: {
        "+":    "R4",
        "*":    "R4",
        ")":    "R4",
        "$":    "R4"
    },

    4: {
        "id":   "S5",
        "(" :   "S4",
        "E" :   "G8",
        "T" :   "G2",
        "F" :   "G3"
    },

    5: {
        "+":    "R6",
        "*":    "R6",
        ")":    "R6",
        "$":    "R6"
    },

    6: {
        "id":   "S5",
        "(" :   "S4",
        "T" :   "G9",
        "F" :   "G3"
    },

    7: {
        "id":   "S5",
        "(" :   "S4",
        "F" :   "G10"
    },

    8:  {
        "+":    "S6",
        ")":    "S11"
    },

    9:  {
        "+":    "R1",
        "*":    "S7",
        ")":    "R1",
        "$":    "R1"
    },

    10: {
        "+":    "R3",
        "*":    "R3",
        ")":    "R3",
        "$":    "R3"
    },

    11: {
        "+":    "R5",
        "*":    "R5",
        ")":    "R5",
        "$":    "R5"
    }
}

grammar = {
        1: ("E", ["E", "+", "T"]),
        2:  ("E",["T"]),
        3: ("T",["T", "*", "F"]),
        4: ("T", ["F"]),
        5: ("F", ["(", "E", ")"]),
        6: ("F",["id"])
}

def pushNextState(top, token):  #Hace un push en la pila del estado en matrix[top][token] -> "S5" hace stack.append(5)
    global stack
    state = getState(top,token)
    stack.append(state)

def shift(top, token):   #No hace nada
    global stack


def reduce(top, token): #Hace todo el procedimiento del reduce
    global stack
    global symbols

    rule  = grammar[getState(top,token)][1]
    head = grammar[getState(top,token)][0]

    for i in range(0, len(rule)):
        stack.pop()
        symbols.pop()

    pushNextState(stack[-1], head)
    symbols.append(head)


def action(top, token):             #Retorna la acción en matrix[top][token] -> "S5" return "S"
    action = matrix[top][token]
    return action[0]

def getState(top, token):           #Retorna el estado en matrix[top][token] -> "S5" return int(5)
    return int(matrix[top][token][1:])





####################################

stack.append(initial)
token = tokens.pop(0)

while(1):


    top = stack[-1]

    if(token in matrix[top]):
        act = action(top, token)

        if(act == "S"): #Shift
            pushNextState(top,token)
            symbols.append(token)
            token = tokens.pop(0)

        elif(act == "R"): #Reduce
            reduce(top,token)

        elif(act == "A"): #Aceptado
            print ("SIMON")
            break;

        else:
            print ("NELSON")

    else:
        print ("NELSON")
        break
