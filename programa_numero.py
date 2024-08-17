peso=input('introduce el peso de tu cuerpo por kilo')
altura=input('introduce el peso de tu altura por metros')



imc=round(float(peso)/float(altura)**2,2)##para dejar el resultado en decimales es necesario copiarlo de la manera en que se muestra en esta linea


print('tu indice de masa corporal es',imc ,'donde',imc,'es el indice de masa corporal')