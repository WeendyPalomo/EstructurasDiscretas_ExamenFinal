class NodoArbol:
    def __init__(self, val):
        self.val = val
        self.izq = None
        self.der = None

def insertar_bst(raiz, clave):
    if not raiz:
        return NodoArbol(clave)
    if clave < raiz.val:
        raiz.izq = insertar_bst(raiz.izq, clave)
    else:
        raiz.der = insertar_bst(raiz.der, clave)
    return raiz

def inorden(raiz):
    return inorden(raiz.izq) + [raiz.val] + inorden(raiz.der) if raiz else []

# Arbol inicial con la raíz en 4
raiz = NodoArbol(4)
insertar_bst(raiz, 2)
insertar_bst(raiz, 5)
insertar_bst(raiz, 3)

# En inorden, los elementos de un BST siempre salen ordenados de menor a mayor
print("BST en Inorden luego de las inserciones:", inorden(raiz))
