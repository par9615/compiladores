pila = []
token = ["id", "+" , "id"]
matriz = {
    "E": {
        "id" : "TE'" ,
        "("  : "TE'"
    },
    "E'": {
        "+"  : "TE'",
        ")"  : "#",
        "$"  : "#"
    },
    "T": {
        "id" : "FT'",
        "("  : "FT'"
    },
    "T'" : {
        "+"  : "#",
        "*"  : "*FT'",
        ")"  : "#",
        "$"  : "#"
        },
    "F" : {
        "id" : "id",
        "("  : "(E)"
    }
}


"""
E -> TE'
E'-> +TE' | eps
T -> FU
U -> *FU | eps
F -> (E) | id

"""


########################


#analisis sintactico

pila += "$"
pila += "E"

coincidencia = ''

"""
$          id+id$
TE'$
matriz[E][id]
"""

def predAnalysis(token):
    while( pila[-1] != '$'):
        print(coincidencia, end = " \t\t")

        for i in pila:
            print(i, end = "")

        print("\t\t", end = "")

        for i in token:
            print(i, end = "")

        print("\t\t", end = "")

        top = pila.pop()
        nextToken = token[-1]

        if(top == nextToken):
            token.pop()
            coincidencia += nextToken
            print('Coincidencia ' + nextToken)

        elif (not (nextToken in matriz[top])):
            print('Error')

        elif (matriz[top][nextToken] != '#'):
                pila += (matriz[top][nextToken])
                print('Salida ' + top + ' ->' + matriz[top][nextToken])

        elif (matriz[top][nextToken] == '#'):
                continue

        else:
            print('Error')


class Stack(object):

    def __init__(self):
        self.storage = []

    def isEmpty(self):
        return len(self.storage) == 0

    def push(self,p):
        self.storage[:0] = p

    def pop(self):
        """issue: throw exception?"""
        return None


 $E              id+id           Salida E ->TE'
                 $TE'            id+id           Traceback (most recent call last):
  File "C:\Users\simio\Desktop\IDE´s Projects\Python\AnalisisDescendente.py", line 78, in <module>
    elif (not (nextToken in matriz[top])):
KeyError: "'"
