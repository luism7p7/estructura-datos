class Pila: 

    def  __init__(self, maxTamaño:int):
        self.maxTamaño = maxTamaño
        self.tope=-1
        self.pila=[None]*maxTamaño

    def esVacia(self):
        return self.tope == -1
    

    def esLlena(self):
        return self.tope == self.maxTamaño -1
    
    def push(self,elemento):
        if self.esLlena():
            print("Sintax Error:La pila está llena, no se puede llenar mas elementos")
        else:
            self.tope+=1
            self.pila[self.tope]=elemento
            return f'Elemento {elemento} agregado a la pila.'
        


    def pop(self):
        if self.esVacia():
            print('Sintax Error:La pila está vacia, no se puede eliminar elementos')
            return 0 
              
        else:
            elemento= self.pila[self.tope]
            self.tope-=1
            print('Elemento',elemento,'eliminado de la fila')
            return elemento
    

    def peek(self):
        if  self.esVacia():
            print('Sintax Error:La pila está vacia, no se puede ver el elemento')
            return 0 
        else:
            elemento = self.pila[self.tope]
            print('mostrando el elmento superior de la cima:',elemento)
            return elemento
        
pila= Pila(5)

print('iniciando las operaciones de la pila ')

pila.push(1)
pila.push(2)
pila.push(3)
pila.push(4)
pila.push(5)
pila.push(8)
pila.push(10)
pila.pop()

pila.peek()

        