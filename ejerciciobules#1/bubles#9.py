numero=int(input(('escribe un numero: ')))

for i in  range(1,numero):
  fila=[]
  for j in range (i,0,-1):
    fila.append(2*j-1)

  print('  '.join(map(str,fila)))
  