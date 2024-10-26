class Animal:
    def __init__(self,nombre:str,edad:int,tipo:str):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo

    def __str__ (self):
        return f'El nombre del animal es {self.nombre}, su edad es {self.edad}, y el tipo de animal es {self.tipo}'
    
class Aguila(Animal):
    def __init__(self,nombre:str,edad:int):
        super().__init__(nombre,edad,'aguila')


class Pantera(Animal):
    def __init__(self,nombre:str,edad:int):
        super().__init__(nombre,edad,'pantera')


class Vaca(Animal):
    def __init__(self,nombre:str,edad:int):
        super().__init__(nombre,edad,'vaca')

aguila=Aguila('pepito',19)
pantera=Pantera('rollito',6)
vaca=Vaca('valen',5)

print(aguila)
print(pantera)
print(vaca)

class Node:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente=None

class lista_enlazada:
    def __init__(self):
        self.cabeza = None
    
    def agregar(self,animal):
        if not self.contiene(animal.nombre):
            nuevo_node = Node(animal)
            if self.cabeza is None:
                self.cabeza = nuevo_node
            else:
                actual = self.cabeza
                while actual.siguiente:
                    actual = actual.siguiente
                actual.siguiente = nuevo_node

    def contiene(self,nombre):
        actual = self.cabeza
        while actual:
            if actual.dato.nombre == nombre:
                return True
            actual = actual.siguiente
        return False
    
    def lista(self,node):
        if node:
            print(node.dato)
            self.lista(node.siguiente)
    
    def impresion(self):
        actual = self.cabeza
        while actual:
            print(actual.dato)
            actual = actual.siguiente 

# ...

lista_animales = lista_enlazada()

lista_animales.agregar(Aguila('bella', 44))
lista_animales.agregar(Pantera('puertica', 34))
lista_animales.agregar(Vaca('rollo', 24))