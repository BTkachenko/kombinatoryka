import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definicja zakresów dla r i t
r_range = np.linspace(0, 1, 100)
t_range = np.linspace(0, 4 * np.pi, 200)

# Tworzenie siatki
R, T = np.meshgrid(r_range, t_range)

# Sr
X_sr = R * np.cos(T)
Y_sr = R * np.sin(T)
Z_sr = np.sqrt(R) * np.cos(T / 2)

# Sc
Z_sc = np.sqrt(R) * np.sin(T / 2)

# Tworzenie wykresu dla Sc
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X_sr, Y_sr, Z_sc, rstride=5, cstride=5, color='r', alpha=0.7)
ax.set_title('Powierzchnia Sc')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.savefig("742.png")


plt.savefig("742.png")

#Wolfram
#parametric plot3D {r*cos(t), r*sin(t), sqrt(r)*sin(t/2)} for r from 0 to 1 and t from 0 to 4*pi
