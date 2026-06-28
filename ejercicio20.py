class NodoAST:
    def __init__(self, val, izq=None, der=None):
        self.val = val  # Operador ('+', '*') o número entero
        self.izq = izq
        self.der = der

def evaluar_ast(raiz):
    if not raiz: 
        return 0
    if not raiz.izq and not raiz.der: 
        return int(raiz.val)

    val_izq = evaluar_ast(raiz.izq)
    val_der = evaluar_ast(raiz.der)

    if raiz.val == '+': 
        return val_izq + val_der
    if raiz.val == '*': 
        return val_izq * val_der
    return 0

# Ejemplo de estructura: (4 * 5) + 3 (fuera de las funciones, pegado a la izquierda)
ast = NodoAST('+', NodoAST('*', NodoAST(4), NodoAST(5)), NodoAST(3))
print("Evaluación AST:", evaluar_ast(ast))
