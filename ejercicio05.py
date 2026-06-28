class NaiveBayesDiagnostico:
    def __init__(self):
        # Datos de entrenamiento simplificados: (Tráfico, Alertas) -> Estado
        self.datos = [
            ('Alto', 'Si', 'Caido'),
            ('Alto', 'No', 'Caido'),
            ('Bajo', 'Si', 'Caido'),
            ('Bajo', 'No', 'Activo'),
            ('Bajo', 'No', 'Activo'),
            ('Alto', 'No', 'Activo')
        ]

    def diagnosticar(self, trafico, alertas):
        estados = ['Caido', 'Activo']
        total = len(self.datos)
        resultados = {}

        for est in estados:
            # Prior P(Estado)
            c_est = sum(1 for d in self.datos if d[2] == est)
            p_prior = c_est / total

            p_trafico = (sum(1 for d in self.datos if d[0] == trafico and d[2] == est) + 1) / (c_est + 2)
            p_alertas = (sum(1 for d in self.datos if d[1] == alertas and d[2] == est) + 1) / (c_est + 2)

            # Posterior proporcional
            resultados[est] = p_prior * p_trafico * p_alertas

        # Normalizar y retornar el de mayor probabilidad
        suma_prob = sum(resultados.values())
        return {k: v / suma_prob for k, v in resultados.items()}

# Uso del modelo (fuera de la clase, pegado a la izquierda)
nb = NaiveBayesDiagnostico()
print("Diagnóstico para ('Alto', 'Si'):", nb.diagnosticar('Alto', 'Si'))
