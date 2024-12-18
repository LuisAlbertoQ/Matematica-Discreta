def f(x):
    return math.exp(-x) - x

import math

def newton_raphson(f, x0, x1, tol, max_iter):
    i = 0
    while True:
        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
        if abs(x2 - x1) < tol:
            return x2, i
        if abs(f(x2)) < 1e-10:
            return x2, i
        if i >= max_iter:
            raise Exception("El método no converge")
        x0, x1 = x1, x2
        i += 1

root, iterations = newton_raphson(f, 0.0, 1.0, 1e-6, 100)
print(f"Raíz aproximada: {root:.6f}")
print(f"Número de iteraciones: {iterations}")