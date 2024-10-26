import random

import string
longitud=int(input('cual es el parametro de caracterez para generar la contraseña aleatoria: '))
def generar(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for i in range(longitud))

print(generar(longitud))