def combinaciones_con_repeticion(n, k):
    # Equivalente a calcular el coeficiente binomial de (n + k - 1) sobre k
    N = n + k - 1
    if k > N: 
        return 0
    
    resultado = 1
    for i in range(1, k + 1):
        resultado = resultado * (N - i + 1) // i
    return resultado

# Elegir 3 sabores de helado de 5 disponibles (permitiendo repetir sabores)
print(f"CR(5, 3) = {combinaciones_con_repeticion(5, 3)}")  # Output: 35
