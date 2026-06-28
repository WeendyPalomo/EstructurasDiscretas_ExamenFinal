import math

def teorema_maestro(a, b, fn_str, c):
    """
    Evalúa la complejidad asumiendo f(n) = O(n^c)
    Para recurrencias de la forma: T(n) = a * T(n/b) + O(n^c)
    """
    log_b_a = math.log(a, b)

    print(f"Ecuación: T(n) = {a}T(n/{b}) + O(n^{c})")
    print(f"log_b(a) = {log_b_a:.2f} vs c = {c}")

    if log_b_a > c:
        return f"Caso 1: Complejidad es Theta(n^{log_b_a:.2f})"
    elif math.isclose(log_b_a, c):
        return f"Caso 2: Complejidad es Theta(n^{c} * log(n))"
    else:
        return f"Caso 3: Complejidad es Theta({fn_str})"

# Ejemplo de MergeSort: T(n) = 2T(n/2) + O(n^1) -> a=2, b=2, c=1
a, b, fn_str, c = 2, 2, "n", 1
resultado = teorema_maestro(a, b, fn_str, c)
print("Resultado:", resultado)
