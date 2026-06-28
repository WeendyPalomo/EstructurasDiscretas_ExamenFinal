from collections import deque

class NodoArbol:
    def __init__(self, val):
        self.val = val
        self.izq = None
        self.der = None

def level_order(raiz):
    if not raiz: 
        return []
    
    resultado = []
    cola = deque([raiz])

    while cola:
        nodo = cola.popleft()
        resultado.append(nodo.val)
        
        if nodo.izq: 
            cola.append(nodo.izq)
        if nodo.der: 
            cola.append(nodo.der)
            
    return resultado

# Estructura de prueba 
raiz = NodoArbol(1)
raiz.izq = NodoArbol(2)
raiz.der = NodoArbol(3)
raiz.izq.izq = NodoArbol(4)

print("Recorrido por Niveles:", level_order(raiz))
