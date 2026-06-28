class NodoArbol:
    def __init__(self, val):
        self.val = val
        self.izq = None
        self.der = None

def preorden(raiz):
    return [raiz.val] + preorden(raiz.izq) + preorden(raiz.der) if raiz else []

def inorden(raiz):
    return inorden(raiz.izq) + [raiz.val] + inorden(raiz.der) if raiz else []

# Estructura de prueba (fuera de las funciones, pegado a la izquierda)
raiz = NodoArbol(1)
raiz.izq = NodoArbol(2)
raiz.der = NodoArbol(3)
raiz.izq.izq = NodoArbol(4)

print("Preorden:", preorden(raiz))
print("Inorden:", inorden(raiz))
