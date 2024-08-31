num1=int(input('digite el primer numero :'))
num2=int(input('digite el segundo numero :'))
oper=input('que operacion deseas hacer  (+, -, *, /):')

def operacion (num1,num2):
    if oper=='+':
    
     return num1+num2
    elif oper=='-':
       return  num1-num2
    elif  oper=='*':
       return  num1*num2
    elif oper=='/':
       return   num1/num2
    else:
       
       return None

print(operacion(num1,num2))    
    
       
    
               