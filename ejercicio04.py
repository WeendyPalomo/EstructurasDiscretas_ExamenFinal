def teorema_bayes():
    # Probabilidades a priori de los servidores
    P_S1 = 0.6
    P_S2 = 0.4

    # Probabilidades condicionales P(Spam | Servidor)
    P_Spam_dado_S1 = 0.05
    P_Spam_dado_S2 = 0.12

    # # 1. Ley de Probabilidad Total
    P_Spam = (P_Spam_dado_S1 * P_S1) + (P_Spam_dado_S2 * P_S2)

    # # 2. Teorema de Bayes
    P_S1_dado_Spam = (P_Spam_dado_S1 * P_S1) / P_Spam

    return P_Spam, P_S1_dado_Spam

p_total, p_bayes = teorema_bayes()
print(f"Probabilidad Total de Spam: {p_total:.4f}")
print(f"P(Servidor 1 | Spam): {p_bayes:.4f}")
