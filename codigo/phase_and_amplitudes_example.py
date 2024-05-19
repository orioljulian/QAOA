# Ejemplo del funcionamiento de QAOA dado en la sección B del apéndice
# También resulta útil para ver cómo realizar operaciones típicas en cuántica
# utilizando la librería de numpy
# (Ej: np.kron() == producto tensorial, @ == producto escalar)

from math import cos, sin
import numpy as np
import sys


def print_arr(arr: np.ndarray, string: str = ""):
    np.set_printoptions(precision=4)
    print("-"*79)
    print(string + " " + "-"*5)
    print(arr)
    print()


####################
# Definiciones
####################
g = 0.1
print_arr(g, "Gamma: g")
b = - 0.1
print_arr(b, "Beta: b")

# Estado en superposición
v_0 = np.asarray([1, 1, 1, 1]) * 1/2
print_arr(v_0, "Estado inicial: v_0")

# Pauli-X
x = np.asarray([[0, 1],
                [1, 0]])

# Identidad
i = np.asarray([[1, 0],
                [0, 1]])

# Hamiltoniano del sistema
H = np.asarray([[3, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 2, 0],
                [0, 0, 0, 4]])
print_arr(H, "Hamiltoniano: H")

# Hamiltoniano del problema: H es diagonal en la b.c, se hace exp(...) de ella
U_p = np.diag(np.exp(-1.j * g * np.diag(H)))
print_arr(U_p, "Hamiltoniano del problema: U(H, g) = exp(-i * g * H)")

# Aplicacion de U_p
v_1 = U_p @ v_0
print_arr(v_1, "Modificacion de fases: v_1 = U(H, g) @ v_0")

# Hamiltoniano de mezcla: kron(x, i)^2 == kron(i, x)^2 == i
# exp(-i * b * B) = exp(-i * b * kron(x, I)) @ exp(-i * b * kron(I, x))
U_m = (cos(b) * np.kron(i, i) - 1.j*sin(b)*np.kron(x, i)) @ \
    (cos(b) * np.kron(i, i) - 1.j*sin(b)*np.kron(i, x))
print_arr(U_m, "Hamiltoniano de mezcla: U(B, b) = exp(-i * b * B)")

# Aplicacion de U_m
v_2 = U_m @ v_1
print_arr(v_2, "Modificacion de probabilidades: v_2 = U(B, b) @ v_1")

# Calculo de las probabilidades:
for i in range(0, 4):
    mod = v_2[i].real**2 + v_2[i].imag**2
    print(f"P({'{0:02b}'.format(i)}) = {mod}")

print()
sys.exit(0)
