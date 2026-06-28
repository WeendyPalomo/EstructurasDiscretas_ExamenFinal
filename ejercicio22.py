class NodoArbol:
    def __init__(self, val):
        self.val = val
        self.izq = None
        self.der = None

def buscar_bst(raiz, clave):
    if not raiz or raiz.val == clave:
        return raiz
    if clave < raiz.val:
        return buscar_bst(raiz.izq, clave)
    return buscar_bst(raiz.der, clave)

# Estructura de prueba: un BST balanceado (fuera de las funciones, pegado a la izquierda)
#        4
#       / \
#      2   5
raiz = NodoArbol(4)
raiz.izq = NodoArbol(2)
raiz.der = NodoArbol(5)

# Búsqueda del valor 5
resultado = buscar_bst(raiz, 5)
if resultado:
    print(f"¡Clave encontrada!: Nodo con valor {resultado.val}")
else:
    print("La clave no existe en el árbol.")
