palin=str(input('digita una palabra para verificar si es un palindromo o no: '))

def verificar(palin):
    
    if palin==palin[::-1]:
        print('la palabra es un palindromo')
    else :
        print('la palabra no es un palindromo')
print(verificar(palin))

    

