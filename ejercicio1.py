def coeficiente_binomial(n, k):
 if k > n: return 0
 if k == 0 or k == n: return 1
 # Optimización: C(n, k) = C(n, n-k)
 k = min(k, n - k)

 dp = [0] * (k + 1)
 dp[0] = 1 # Caso base

 for i in range(1, n + 1):
 for j in range(min(i, k), 0, -1):
 dp[j] = dp[j] + dp[j - 1]
 return dp[k]
print(f"C(5, 2) = {coeficiente_binomial(5, 2)}") # Output: 10
