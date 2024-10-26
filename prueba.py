import time
import random

# Clase Tarea que contiene el id, la duración y la prioridad
class Tarea:
    def __init__(self, id_tarea, duracion, prioridad):
        self.id_tarea = id_tarea  # Identificador único de la tarea
        self.duracion = duracion  # Tiempo de ejecución de la tarea
        self.prioridad = prioridad  # Nivel de prioridad de la tarea

    def __str__(self):
        # Representación de la tarea para imprimir
        return f"Tarea {self.id_tarea}: Duración {self.duracion}, Prioridad {self.prioridad}"

# Simulación con el algoritmo SJF (Shortest Job First)
def sjf_simulacion(tareas):
    # Ordenamos las tareas por su duración (tiempo de ejecución más corto primero)
    tareas.sort(key=lambda t: t.duracion)

    print("\n--- Simulación SJF ---")
    tiempo_total = 0
    for tarea in tareas:
        print(f"Procesando {tarea}...")
        time.sleep(0.5)  # Simula el tiempo de procesamiento
        tiempo_total += tarea.duracion
        print(f"Tarea completada. Tiempo total: {tiempo_total} segundos")

# Simulación con el algoritmo de Prioridad
def prioridad_simulacion(tareas):
    # Ordenamos las tareas por prioridad (las de mayor prioridad se ejecutan primero)
    tareas.sort(key=lambda t: t.prioridad)

    print("\n--- Simulación por Prioridad ---")
    tiempo_total = 0
    for tarea in tareas:
        print(f"Procesando {tarea}...")
        time.sleep(1)  # Simula el tiempo de procesamiento
        tiempo_total += tarea.duracion
        print(f"Tarea completada. Tiempo total: {tiempo_total} segundos")

# Función principal para simular ambos escenarios
def simular_escenarios():
    # Creamos una lista de tareas con id, duración aleatoria y prioridad aleatoria
    tareas = [Tarea(i, random.randint(1, 10), random.randint(1, 5)) for i in range(1, 6)]

    # Simulación con el algoritmo SJF
    print("Escenario 1: Simulación con algoritmo SJF")
    sjf_simulacion(tareas)

    # Simulación con el algoritmo de Prioridad
    print("\nEscenario 2: Simulación con algoritmo de Prioridad")
    prioridad_simulacion(tareas)

# Ejecutar la simulación
if __name__ == "__main__":
    simular_escenarios()
