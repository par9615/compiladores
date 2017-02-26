pila = []
token = ["id", "+" , "id","$"]
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


#lista[::-1]    ->  invierte la lista
#''.join(list)  ->  convierte la lista en un solo string

pila += "$"
pila += "E"

coincidencia = ''


while( pila[-1] != '$'):
    print(coincidencia, end = " \t\t")

    for i in pila:
        print(i, end = "")

    print("\t\t", end = "")

    for i in token:
        print(i, end = "")

    print("\t\t", end = "")

    top = pila.pop()                            #se obtiene el primero de la pila
    if(pila[-1] == "'"):
        top+=pila.pop()                         #si el que sigue es ' entonces se hace otro pop para sacar la regla completa  E'$  -> $

    nextToken = token[0]                        #se obtiene el token del principio

    if(top == nextToken):
        token.pop(0)
        coincidencia += nextToken
        print('Coincidencia ' + nextToken)

    elif (not (nextToken in matriz[top])):
        print('Error')

    elif (matriz[top][nextToken] != '#'):
            pila += (matriz[top][nextToken])[::-1]
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
