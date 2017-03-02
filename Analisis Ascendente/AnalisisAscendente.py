stack = []
tokens = []
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

gramatic = {
    "E": {
        1:  ["E", "+", "T"],
        2:  ["T"]
    },

    "T": {
        3: ["T", "*", "F"],
        4: ["F"]
    },

    "F": {
        5: ["(", "E", ")"],
        6: ["id"]
    }
}


def shift(top, token):
    global stack


def reduce(top, token):
    global stack


def action(top, token):
    action = matrix[top][token]
    return action[0]

def pushNextState(top, token):
    global stack
    state = matrix[top][token]
    state.pop(0)
    stack.append(state)



####################################
# TODO: Reduce
# TODO: check errors

stack.append(initial)
token = tokens.pop(0)

while(1):
    top = stack.pop()

    if(token in matrix[top]):
        if(action(top, token) == "S"): #Shift
            pushNextState(top,token)
            symbols.append(token)
            token = tokens.pop(0)

        elif(action(top, token) == "R"): #Reduce
            for i in range(0, len())

        elif(action(top, token) == "A"): #Aceptado

        else:

    else:
