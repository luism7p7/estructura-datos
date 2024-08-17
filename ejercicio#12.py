numero=int(input('numero de barras que no son del dia'))

barras_de_pan=float(3.49)
descuento=0.6
total=numero*barras_de_pan
des=total*descuento
total=total-des

print('precio habitual de barras de pan frescas:',barras_de_pan,'€')
print('_____________________________')
print('descuento de barras que no son frescas con el 60% es:',descuento,'€')
print('_____________________________')
print('coste final con descuento y cantidad es:',round(total),2)
print('_____________________________')
print('coste final con descuento y cantidad es:',str(round(total,2)))

