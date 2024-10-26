class Animal:
    def __init__(self, nombre:str, edad:int, tipo:str ):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo

       
    def __str__(self):
        return f"El nombre del animal es {self.nombre}, su tipo es {self.tipo} y su edad es {self.edad} " 

class Aguila (Animal):
    def  __init__(self, nombre:str, edad:int, tipo:str ):
      super().__init__(nombre, edad, 'aguila')

class Pantera (Animal):
    def  __init__(self, nombre:str, edad:int, tipo:str ):
      super().__init__(nombre, edad, 'pantera')

class Vaca (Animal):
    def  __init__(self, nombre:str, edad:int, tipo:str ):
      super().__init__(nombre, edad, 'vaca')

aguila= Aguila('lina',6,'Aguila'  )
pantera= Pantera('Rodolfo',12,'Pantera'  )
vaca= Vaca('valija',8,'Vaca'  )

print(aguila)
print(type(aguila))
print(pantera)
print(type(pantera))
print(vaca)
print(type(vaca))

class Node:
    def __init__(self, animal):
        self.animal = animal
        self.next = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_animal(self, animal):
        if not self.contiene(animal.nombre):
            nuevo_node = Node(animal)
            if self.cabeza is None:
                self.cabeza = nuevo_node
            else:
                current = self.cabeza
                while current.next:
                    current = current.next
                current.next = nuevo_node

    def contiene(self, nombre):
        actual = self.cabeza
        while actual:
            if actual.animal.nombre == nombre:
                return True
            actual = actual.next
        return False

    def Lista(self, node):
        if node:
            print(node.animal)
            self.Lista(node.next)

    def impresion(self):
        actual = self.cabeza
        while actual:
            print(actual.animal)
            actual = actual.next

# Creamos la lista enlazada
lista_animales = ListaEnlazada()

# Agregamos animales a la lista
lista_animales.agregar_animal((aguila))
lista_animales.agregar_animal((pantera))
lista_animales.agregar_animal((vaca))

lista_animales.agregar_animal(Aguila('bella', 44, 'pajaro'))
lista_animales.agregar_animal(Pantera('mopri', 12, 'leonn'))
lista_animales.agregar_animal(Vaca('anastacio', 8, 'toro'))
lista_animales.agregar_animal(Aguila('coliflor', 6, 'buo'))  # Este animal ya existe, no se agregará

# Mostramos los animales en la lista utilizando recursividad
print("animales de la lista:")
lista_animales.Lista(lista_animales.cabeza)

# Mostramos los animales en la lista utilizando un bucle
print("animales agregados:")
lista_animales.impresion()





