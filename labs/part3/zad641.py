from sympy import symbols, series

# Definiujemy zmienną symboliczną
z = symbols('z')

# Funkcja generująca
f_z = 1 / ((1 - z)**z)

# Obliczamy rozwinięcie w szereg Taylora do określonego rzędu
n_terms = 14  # Liczba wyrazów szeregu, którą chcemy obliczyć
taylor_series = series(f_z, z, 0, n_terms + 1).removeO()

# Wypisujemy współczynniki
for n in range(1, n_terms + 1):
    coefficient = taylor_series.coeff(z, n)
    print(f'r_{n} = {coefficient}')
