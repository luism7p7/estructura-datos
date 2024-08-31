numeros=int(input('numero'))
for i in range (1,numeros):
    fila=[]    
    for j in range (i,0-1):
        fila.append(2*j-1)

    print('  '.join(map(str,fila)))
 