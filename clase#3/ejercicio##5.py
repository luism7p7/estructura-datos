num=int(input('igresa numero'))
resultado=1
for i in range(1,num+1):
    resultado *=i
    print('el factorial de',num,'es:',resultado)