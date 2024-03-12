from mpmath import taylor, power

# Zdefiniowanie funkcji tworzącej
def f(z):
    return 1 / power(1 - z, z)

# Obliczanie współczynników rn dla n = 1, ..., 100
coefficients = taylor(f, 0, 100)

# Wyświetlenie pierwszych 20 współczynników
print("Pierwsze 20 współczynników:")
for i, coeff in enumerate(coefficients[:20], start=1):
    print(f"r_{i} = {coeff}")

# Wyświetlenie ostatnich 20 współczynników
print("\nOstatnie 20 współczynników:")
for i, coeff in enumerate(coefficients[-20:], start=81):
    print(f"r_{i} = {coeff}")

