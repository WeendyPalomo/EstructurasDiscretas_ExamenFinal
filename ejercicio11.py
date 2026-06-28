def calcular_grados(lista_adyacencia, es_dirigido=False):
    grados_salida = {nodo: len(vecinos) for nodo, vecinos in lista_adyacencia.items()}
    grados_entrada = {nodo: 0 for nodo in lista_adyacencia}

    for nodo, vecinos in lista_adyacencia.items():
        for vecino in vecinos:
            if vecino in grados_entrada:
                grados_entrada[vecino] += 1

    if not es_dirigido:
        # En grafos no dirigidos, grado entrada = grado salida = grado total
        grado_total = {nodo: grados_salida[nodo] for nodo in lista_adyacencia}
        return grado_total

    return {"entrada": grados_entrada, "salida": grados_salida}

# Ejemplo Grafo No Dirigido (fuera de la función, pegado a la izquierda)
grafo = {0: [1, 2], 1: [0, 2], 2: [0, 1], 3: []}
print("Grados (No Dirigido):", calcular_grados(grafo))
