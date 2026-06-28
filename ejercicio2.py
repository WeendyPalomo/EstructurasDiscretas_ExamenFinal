import random
import scipy.stats as stats

def p_red_analitico(n, k, p):
    # Probabilidad de recibir exactamente k paquetes de n disponibles
    return stats.binom.pmf(k, n, p)

def p_red_simulacion(n, k, p, simulaciones=100000):
    exitos = 0
    for _ in range(simulaciones):
        # Simula n paquetes independientes con probabilidad p
        paquetes_recibidos = sum(1 for _ in range(n) if random.random() < p)
        if paquetes_recibidos == k:
            exitos += 1
    return exitos / simulaciones

n, k, p = 10, 3, 0.3
print(f"Analítico P(A): {p_red_analitico(n, k, p):.5f}")
print(f"Simulación P(A): {p_red_simulacion(n, k, p):.5f}")
