class Tarea:
    def __init__(self, descripcion:str, prioridad:str, fecha_vencimiento:int):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = fecha_vencimiento
        self.siguiente= None
        self.completado= False

class ListaEnlazada:
    def __init__(self):
        self.cabeza=None
        self.tareas_completadas = []

    def agregar_tarea(self, tarea):
        if not self.cabeza:
            self.cabeza = tarea
        else:
            actual = self.cabeza
            while  actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = tarea 

    def mostrar_tarea(self):
        actual = self.cabeza
        tareas= []
        while actual:
            tareas.append(f'descripción:{actual.descripcion}, tarea proritaria: {actual.prioridad}, fecha de vencimiento: {actual.fecha_vencimiento}')
            actual= actual.siguiente
        return '\n'.join(tareas)
    

    def ordenar_prioridad(self):
        tareas = []
        actual = self.cabeza
        while actual:
            tareas.append(actual)
            actual = actual.siguiente
        tareas.sort(key=lambda x: x.prioridad)
        self.cabeza= tareas[0]
        for i in range(len(tareas)-1):
            tareas[i].siguiente = tareas[i+1]
        tareas[-1].siguiente=None
    def buscar_tarea(self, descripcion):
        actual = self.cabeza
        while actual:
            if actual.descripcion == descripcion:
                return actual
            actual= actual.siguiente
        return None
    

    def eliminar_tarea(self,descripcion):
        if self.cabeza.descripcion == descripcion:
            self.cabeza = self.cabeza.siguiente
        else:
            anterior= self.cabeza
            actual=self.cabeza.siguiente
            while actual:
                if actual.descripcion == descripcion:
                    anterior.siguiente = actual.siguiente
                    return
                anterior = actual
                actual = actual.siguiente

    def marcar_completado(self, descripcion):
        tarea = self.buscar_tarea(descripcion)
        if tarea:
            tarea.completado = True
            self.eliminar_tarea(descripcion)
            self.tareas_completadas.append(tarea)
            print(f'La tarea {descripcion} marcada como completada')
        else:
            print(f'La tarea {descripcion} no encontrada')

lista_tareas = ListaEnlazada()

tarea1 = Tarea('Comprar leche', 'Baja', '2024/03/14')
tarea2 = Tarea('estudiar', 'Alta', '2024/02/24')
tarea3 = Tarea('ayudar en la casa', 'Alta', '2024/04/14')
print()
lista_tareas.agregar_tarea(tarea1)
lista_tareas.agregar_tarea(tarea2)
lista_tareas.agregar_tarea(tarea3)
print()
print('tareas agragadas:')
print(lista_tareas.mostrar_tarea())

print('tareas ordenadas por prioridad:')
lista_tareas.ordenar_prioridad()
print(lista_tareas.mostrar_tarea())

print()
print("buscar tarea 'estudiar': ")
tarea_encontrada = lista_tareas.buscar_tarea('estudiar')
if tarea_encontrada:
    print(f'Descripcion de tarea: {tarea_encontrada.descripcion}, prioridad de tarea: {tarea_encontrada.prioridad}, fecha de vencimiento:  {tarea_encontrada.fecha_vencimiento}')

else:
    print('Tarea no encontrada')
print()
print("Eliminar tarea 'Comprar leche' :")
lista_tareas.eliminar_tarea("Comprar leche")
print('tareas recientes')
print(lista_tareas.mostrar_tarea())  
print()

print('se marca tarea estudiando como completada')
lista_tareas.marcar_completado('estudiar')
print('tareas restantes')
print(lista_tareas.mostrar_tarea())