class NodoArbol:
    def __init__(self, val):
        self.val = val
        self.izq = None
        self.der = None

def nodo_valor_minimo(nodo):
    actual = nodo
    while actual.izq is not None:
        actual = actual.izq
    return actual

def eliminar_bst(raiz, clave):
    if not raiz: 
        return raiz

    if clave < raiz.val:
        raiz.izq = eliminar_bst(raiz.izq, clave)
    elif clave > raiz.val:
        raiz.der = eliminar_bst(raiz.der, clave)
    else:
        # Caso 1 y 2: Sin hijos o un solo hijo
        if not raiz.izq: 
            return raiz.der
        elif not raiz.der: 
            return raiz.izq

        # Caso 3: Dos hijos, encontrar el sucesor más pequeño a la derecha
        temporal = nodo_valor_minimo(raiz.der)
        raiz.val = temporal.val
        raiz.der = eliminar_bst(raiz.der, temporal.val)

    return raiz

def inorden(raiz):
    return inorden(raiz.izq) + [raiz.val] + inorden(raiz.der) if raiz else []

# Estructura de prueba 
#        5
#       / \
#      3   6
raiz = NodoArbol(5)
raiz.izq = NodoArbol(3)
raiz.der = NodoArbol(6)

print("BST inicial en Inorden:", inorden(raiz))
raiz = eliminar_bst(raiz, 3)
print("BST en Inorden luego de eliminar el 3:", inorden(raiz))
