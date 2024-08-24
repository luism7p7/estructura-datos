cantidad=int(input('escriba una cantidad para invertir'))
interez=float(input('escriba el interez anual'))
inversion=int(input('escriba el numero de años que desea invertir'))


for i in range(inversion):
    cantidad=cantidad+ (cantidad*interez/100)
    print(f'el monto de la inversion en el año {i+1} es, {round,{cantidad,2}}')
    



    




