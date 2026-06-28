class Grafo:
    def __init__(self, num_vertices):
        self.V = num_vertices
        # Matriz de adyacencia inicializada en 0
        self.matriz = [[0] * num_vertices for _ in range(num_vertices)]
        # Lista de adyacencia inicializada con diccionarios/listas vacías
        self.lista = {i: [] for i in range(num_vertices)}

    # Operación: Añadir Arista -> Matriz: O(1) | Lista: O(1)
    def agregar_arista(self, u, v):
        self.matriz[u][v] = 1
        self.lista[u].append(v)

    # Operación: Eliminar Arista -> Matriz: O(1) | Lista: O(V) o O(E) en el peor caso
    def eliminar_arista(self, u, v):
        self.matriz[u][v] = 0
        if v in self.lista[u]:
            self.lista[u].remove(v)

    # Operación: Verificar si existe arista -> Matriz: O(1) | Lista: O(Grado(u))
    def tiene_arista(self, u, v):
        es_matriz = self.matriz[u][v] == 1
        es_lista = v in self.lista[u]
        return es_matriz, es_lista

# Pruebas e inicialización (fuera de la clase, pegado al extremo izquierdo)
g = Grafo(3)
g.agregar_arista(0, 1)
g.agregar_arista(1, 2)
print("¿Existe arista (0->1)?[Matriz, Lista]:", g.tiene_arista(0, 1))
print("Matriz resultante:", g.matriz)
print("Lista resultante:", g.lista)
