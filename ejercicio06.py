class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size=5):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        idx = self._hash(key)
        if not self.table[idx]:
            self.table[idx] = Node(key, value)
        else:
            # Colisión detectada: recorrer o añadir al inicio de la lista
            curr = self.table[idx]
            while curr:
                if curr.key == key:
                    curr.value = value  # Actualizar si ya existe
                    return
                if not curr.next: 
                    break
                curr = curr.next
            curr.next = Node(key, value)

    def get(self, key):
        idx = self._hash(key)
        curr = self.table[idx]
        while curr:
            if curr.key == key: 
                return curr.value
            curr = curr.next
        return None

# Uso de la tabla hash (fuera de las clases, pegado al extremo izquierdo)
ht = HashTable()
ht.insert("IP_1", "192.168.1.1")
ht.insert("IP_2", "10.0.0.1")  # Puede colisionar dependiendo del hash interno
print("Buscar IP_1:", ht.get("IP_1"))
