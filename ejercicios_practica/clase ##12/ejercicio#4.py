peso=int(input('pon en pantalla tu peso'))
altura=float(input('pon en pantalla tu altura'))

imc= peso/(altura)**2

print('tu IMC (Indice de Masa Corporal es: )', imc)

if imc<18.5:
    print('tienes un peso delgado')

if imc > 18.5 and imc <= 24.9:
    print('tienes un peso aceptable')

if imc >=25.0 and imc <= 29.9:
    print('tienes un peso sobrepeso')

if imc >= 30.0 and imc <=34.9:
    print('tienes un peso obesidad grado 1')

if imc >= 35.0 and imc <= 39.9:
    print('tienes un peso obesidad grado 2')

if imc >= 40.0:
    print('tienes un peso obesidad grado 3')  