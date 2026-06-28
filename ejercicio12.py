def verificar_invariantes_isomorfismo(g1, g2):
    if len(g1) != len(g2): 
        return False

    aristas_g1 = sum(len(v) for v in g1.values())
    aristas_g2 = sum(len(v) for v in g2.values())
    if aristas_g1 != aristas_g2: 
        return False

    seq_grados_g1 = sorted([len(v) for v in g1.values()])
    seq_grados_g2 = sorted([len(v) for v in g2.values()])

    return seq_grados_g1 == seq_grados_g2

# Ejemplo de Grafos Isomorfos (fuera de la función, pegado a la izquierda)
g1 = {0: [1, 2], 1: [0], 2: [0]}
g2 = {0: [1], 1: [0, 2], 2: [1]}
print("¿Pasan los invariantes de isomorfismo?:", verificar_invariantes_isomorfismo(g1, g2))
