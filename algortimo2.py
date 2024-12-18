import math

def f(x):
    # Función objetivo f(x) = e^(-x) - x
    return math.exp(-x) - x

def f_prime(x):
    # Derivada de f(x)
    return -math.exp(-x) - 1

def newton_raphson(f, f_prime, x0, tol, max_iter):
    x_i = x0
    num_iter = 0
    
    while num_iter < max_iter:
        x_next = x_i - f(x_i) / f_prime(x_i)
        if abs(x_next - x_i) < tol:
            return x_next, num_iter
        elif abs(f_prime(x_i)) < 1e-10:
            raise ValueError("El método falla porque la pendiente de la tangente es casi horizontal.")
        x_i = x_next
        num_iter += 1
    
    raise ValueError("El método no convergió dentro del número máximo de iteraciones.")

# Valores para el ejercicio
x0 = 0
tol = 1e-6
max_iter = 100

root, num_iter = newton_raphson(f, f_prime, x0, tol, max_iter)
print(f"Raíz aproximada: {root:.6f}")
print(f"Número de iteraciones: {num_iter}")