class NodoArbol:
    def __init__(self, val):
        self.val = val
        self.izq = None
        self.der = None

def metricas_arbol(raiz):
    if not raiz: 
        return 0, 0  # (altura, hojas)
    if not raiz.izq and not raiz.der: 
        return 1, 1

    alt_izq, hojas_izq = metricas_arbol(raiz.izq)
    alt_der, hojas_der = metricas_arbol(raiz.der)

    altura = 1 + max(alt_izq, alt_der)
    hojas = hojas_izq + hojas_der
    return altura, hojas

# Prueba (fuera de las funciones, pegado a la izquierda)
raiz = NodoArbol(1)
raiz.izq = NodoArbol(2)
raiz.der = NodoArbol(3)
raiz.izq.izq = NodoArbol(4)

altura, hojas = metricas_arbol(raiz)
print(f"Altura: {altura}, Número de Hojas: {hojas}")
