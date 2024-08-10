edad=22

edad= int(input("ingrese su edad: "))
#crear una condicion donde los menores de 18 no puedan entrar
if edad <= 18:
    print("no puedes entrar")
else:
    print("puedes entrar")
#edad=2

#preguntar el nombre y mostrar por panalla la edad y el nombre
nombre = input("ingrese su nombre: ")
print("Su nombre es " + nombre + " y su edad es " + str(edad))
181