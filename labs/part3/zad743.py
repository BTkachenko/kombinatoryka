import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definicja nowego zakresu dla r i t dla L
r_range_L = np.linspace(0.1, 10, 100)
t_range_L = np.linspace(0, 8 * np.pi, 200)

# Tworzenie siatki dla L
R_L, T_L = np.meshgrid(r_range_L, t_range_L)

# L
X_L = R_L * np.cos(T_L)
Y_L = R_L * np.sin(T_L)
Z_L = np.sqrt(np.log(R_L)**2 + T_L**2)

# Tworzenie wykresu dla L
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X_L, Y_L, Z_L, rstride=5, cstride=5, color='g', alpha=0.7)
ax.set_title('Powierzchnia L')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.show()



#Wolfram 
#parametric plot3D {r*cos(t), r*sin(t), sqrt((ln(r))^2 + t^2)} for r from 0.1 to 10 and t from 0 to 8*pi
