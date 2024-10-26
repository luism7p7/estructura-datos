correo=input('por favor escribe tu correo institucional:')

nombre,dominio=correo.split('@')

nuevo_correo= f'{nombre}@ceu.es'
print(f'el correo institucional es: {nuevo_correo}')# La f antes de la cadena indica que es una cadena f, y las expresiones dentro de las llaves {} se evalúan y reemplazan con sus valores.
