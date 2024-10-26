factorial=int(input('digite un numero para hallarle su  factorial:'))

   
def calculo(factorial):
    if factorial == 0:
        return f'tu factorial de {factorial} es : {1}'
    else:
         
     numero=1
     for i in range(1,factorial+1):
        numero *=i
     return f'tu factorial de {factorial} es: {numero} '

        
    
print(calculo (factorial))
    