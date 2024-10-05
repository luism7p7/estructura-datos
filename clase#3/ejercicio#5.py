
import random

arreglo=[]

import random
arreglo = []
for i in range(100):
    arreglo.append(random.randint(1, 100))
prom = sum(arreglo) / len(arreglo)

print("Arreglo:", arreglo)
print("Promedio:", prom)