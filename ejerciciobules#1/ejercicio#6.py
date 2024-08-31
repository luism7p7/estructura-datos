class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(valor, self.raiz)

    def _insertar(self, valor, nodo):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar(valor, nodo.izquierda)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar(valor, nodo.derecha)

    def imprimir(self):
        if self.raiz is not None:
            self._imprimir(self.raiz)

    def _imprimir(self, nodo):
        if nodo is not None:
            self._imprimir(nodo.izquierda)
            print(nodo.valor)
            self._imprimir(nodo.derecha)

    def buscar(self, valor):
        return self._buscar(valor, self.raiz)

    def _buscar(self, valor, nodo):
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor:
            return self._buscar(valor, nodo.izquierda)
        else:
            return self._buscar(valor, nodo.derecha)

    def eliminar(self, valor):
        self.raiz = self._eliminar(valor, self.raiz)

    def _eliminar(self, valor, nodo):
        if nodo is None:
            return nodo
        if valor < nodo.valor:
            nodo.izquierda = self._eliminar(valor, nodo.izquierda)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar(valor, nodo.derecha)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            else:
                min_val = self._obtener_minimo(nodo.derecha)
                nodo.valor = min_val
                nodo.derecha = self._eliminar(min_val, nodo.derecha)
        return nodo

    def _obtener_minimo(self, nodo):
        while nodo.izquierda is not None:
            nodo = nodo.izquierda
        return nodo.valor

    def obtener_maximo(self):
        return self._obtener_maximo(self.raiz)

    def _obtener_maximo(self, nodo):
        while nodo.derecha is not None:
            nodo = nodo.derecha
        return nodo.valor

    def obtener_minimo(self):
        return self._obtener_minimo(self.raiz)

# Crear un árbol binario
arbol = ArbolBinario()

# Insertar valores en el árbol
arbol.insertar(5)
arbol.insertar(3)
arbol.insertar(7)
arbol.insertar(2)
arbol.insertar(4)
arbol.insertar(6)
arbol.insertar(8)

# Imprimir el árbol
arbol.imprimir()

# Buscar un valor en el árbol
print("Buscar 4:", arbol.buscar(4))

# Eliminar un valor del árbol
arbol.eliminar(4)

# Imprimir el árbol después de eliminar
arbol.imprimir()

# Obtener el máximo y mínimo valor del árbol
print("Máximo:", arbol.obtener_maximo())
print("Mínimo:", arbol.obtener_minimo())