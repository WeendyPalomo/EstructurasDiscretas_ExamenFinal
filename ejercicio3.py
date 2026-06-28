def confiabilidad_paralelo(probabilidades):
    Q = 1.0
    for p in probabilidades:
        Q *= (1.0 - p)  # Multiplica la probabilidad de falla de cada componente
    return 1.0 - Q

componentes = [0.90, 0.85, 0.95]  # Coniabilidad de cada línea de red/componente
print(f"Confiabilidad del sistema paralelo: {confiabilidad_paralelo(componentes):.5f}")
