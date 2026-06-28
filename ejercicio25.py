from collections import deque

class NodoAVL:
    def __init__(self, val):
        self.val = val
        self.izq = None
        self.der = None
        self.altura = 1

class AVLTree:
    def obtener_altura(self, nodo):
        return nodo.altura if nodo else 0

    def obtener_balance(self, nodo):
        return self.obtener_altura(nodo.izq) - self.obtener_altura(nodo.der) if nodo else 0

    # Tipo 1: Rotación Simple a la Derecha (Caso Izquierda-Izquierda)
    def rotacion_derecha(self, y):
        x = y.izq
        T2 = x.der
        x.der = y
        y.izq = T2
        y.altura = 1 + max(self.obtener_altura(y.izq), self.obtener_altura(y.der))
        x.altura = 1 + max(self.obtener_altura(x.izq), self.obtener_altura(x.der))
        return x

    # Tipo 2: Rotación Simple a la Izquierda (Caso Derecha-Derecha)
    def rotacion_izquierda(self, x):
        y = x.der
        T2 = y.izq
        y.izq = x
        x.der = T2
        x.altura = 1 + max(self.obtener_altura(x.izq), self.obtener_altura(x.der))
        y.altura = 1 + max(self.obtener_altura(y.izq), self.obtener_altura(y.der))
        return y

    # Tipo 3 y 4: Rotaciones Dobles (Manejadas lógicamente en la inserción)
    def insertar(self, nodo, clave):
        if not nodo: 
            return NodoAVL(clave)

        if clave < nodo.val:
            nodo.izq = self.insertar(nodo.izq, clave)
        else:
            nodo.der = self.insertar(nodo.der, clave)

        nodo.altura = 1 + max(self.obtener_altura(nodo.izq), self.obtener_altura(nodo.der))
        balance = self.obtener_balance(nodo)

        # Caso Izquierda-Izquierda -> Rotación Derecha
        if balance > 1 and clave < nodo.izq.val:
            return self.rotacion_derecha(nodo)

        # Caso Derecha-Derecha -> Rotación Izquierda
        if balance < -1 and clave > nodo.der.val:
            return self.rotacion_izquierda(nodo)

        # Tipo 3: Caso Izquierda-Derecha -> Doble Rotación (Izquierda-Derecha)
        if balance > 1 and clave > nodo.izq.val:
            nodo.izq = self.rotacion_izquierda(nodo.izq)
            return self.rotacion_derecha(nodo)

        # Tipo 4: Caso Derecha-Izquierda -> Doble Rotación (Derecha-Izquierda)
        if balance < -1 and clave < nodo.der.val:
            nodo.der = self.rotacion_derecha(nodo.der)
            return self.rotacion_izquierda(nodo)

        return nodo

    def level_order(self, raiz):
        if not raiz: 
            return []
        resultado, cola = [], deque([raiz])
        while cola:
            nodo = cola.popleft()
            resultado.append(nodo.val)
            if nodo.izq: 
                cola.append(nodo.izq)
            if nodo.der: 
                cola.append(nodo.der)
        return resultado

# Estructura de prueba 
arbol = AVLTree()
raiz = None

elementos = [10, 20, 30, 40, 50, 25]
for elem in elementos:
    raiz = arbol.insertar(raiz, elem)

print("Recorrido por Niveles del Árbol AVL balanceado:", arbol.level_order(raiz))
