import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Funkcja sd(n) zwraca sumę cyfr binarnych liczby n
def sd(n):
    return sum(int(digit) for digit in bin(n)[2:])

# Funkcja s(n) zwraca sumę funkcji sd(k) od 1 do n
def s(n):
    return sum(sd(k) for k in range(1, n + 1))

# Obliczamy wartości funkcji s dla zakresu od 1 do 1024
n_values = np.arange(1, 1025)
s_values_cumulative = [s(n) for n in n_values]

# Zadanie 1 - Wykres funkcji s(n)
plt.figure(figsize=(10, 6))
plt.plot(n_values, s_values_cumulative, label='s(n)', color='blue')
plt.xlabel('n')
plt.ylabel('s(n)')
plt.title('Wykres funkcji s(n)')
plt.legend()
plt.grid(True)
plt.show()

# Zadanie 2 - Znalezienie optymalnego współczynnika skalującego dla funkcji n log n
def fit_function(n, scale):
    return scale * n * np.log(n)

params, _ = curve_fit(fit_function, n_values[1:], s_values_cumulative[1:])
optimal_scale_n_log_n = params[0]

# Oblicz różnice s(n) - a(n) dla funkcji n log n
a_values = [fit_function(n, optimal_scale_n_log_n) for n in n_values[1:]]
differences_n_log_n = [s_values_cumulative[n-1] - a_values[n-2] for n in n_values[1:]]

# Wykres różnicy s(n) - a(n) dla n log n
plt.figure(figsize=(10, 6))
plt.plot(n_values[1:], differences_n_log_n, label='s(n) - c*n log n', color='orange')
plt.xlabel('n')
plt.ylabel('Różnica')
plt.title('Wykres różnicy s(n) - c*n log n')
plt.legend()
plt.grid(True)
plt.show()

# Znalezienie optymalnego współczynnika skalującego dla funkcji liniowej n
params_linear, _ = curve_fit(lambda n, scale: scale * n, n_values[1:], s_values_cumulative[1:])
optimal_scale_linear = params_linear[0]

# Oblicz różnice s(n) - c*n dla funkcji liniowej
linear_scaled_values = [optimal_scale_linear * n for n in n_values[1:]]
differences_linear = [s_values_cumulative[n-1] - linear_scaled_values[n-2] for n in n_values[1:]]

# Wykres różnicy s(n) - c*n dla funkcji liniowej
plt.figure(figsize=(10, 6))
plt.plot(n_values[1:], differences_linear, label='s(n) - c*n', color='green')
plt.xlabel('n')
plt.ylabel('Różnica')
plt.title('Wykres różnicy s(n) - c*n')
plt.legend()
plt.grid(True)
plt.show()

# Wyświetlenie współczynników skalujących
print(f"Optymalny współczynnik skalujący dla funkcji liniowej: {optimal_scale_linear:.4f}")
print(f"Optymalny współczynnik skalujący dla funkcji n log n: {optimal_scale_n_log_n:.4f}")
