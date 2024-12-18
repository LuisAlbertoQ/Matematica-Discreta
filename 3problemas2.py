import math

def newton_raphson(f, f_prime, x0, tol, max_iter):
    """
    Implementa el método de Newton-Raphson para resolver f(x) = 0.

    Parámetros:
    f: función objetivo.
    f_prime: derivada de la función objetivo.
    x0: aproximación inicial.
    tol: tolerancia aceptable para el error entre iteraciones consecutivas.
    max_iter: número máximo de iteraciones permitidas.

    Retorna:
    Una tupla con la raíz aproximada y el número de iteraciones realizadas.
    Si no converge, genera una excepción.
    """
    x_i = x0
    num_iter = 0
    
    while num_iter < max_iter:
        x_next = x_i - f(x_i) / f_prime(x_i)  # Fórmula del método de Newton-Raphson
        if abs(x_next - x_i) < tol:
            return x_next, num_iter + 1  # Retorna la raíz y el número de iteraciones
        elif abs(f_prime(x_i)) < 1e-10:
            raise ValueError("El método falla porque la pendiente de la tangente es casi horizontal.")
        x_i = x_next
        num_iter += 1
    
    raise ValueError("El método no convergió dentro del número máximo de iteraciones.")

# Resolver las ecuaciones dadas:
ecuaciones = [
    {
        "desc": "f(x) = x - cos(x)",
        "f": lambda x: x - math.cos(x),
        "f_prime": lambda x: 1 + math.sin(x),
        "x0": 0.5,
        "tol": 0.05,
        "max_iter": 100
    },
    {
        "desc": "f(x) = x^3 - x - 1",
        "f": lambda x: x**3 - x - 1,
        "f_prime": lambda x: 3 * x**2 - 1,
        "x0": 1.5,
        "tol": 0.05,
        "max_iter": 100
    },
    {
        "desc": "f(x) = x^2 - 2",
        "f": lambda x: x**2 - 2,
        "f_prime": lambda x: 2 * x,
        "x0": 1.5,
        "tol": 1e-5,
        "max_iter": 100
    },
    {
        "desc": "f(x) = x - 4 + ln(x)",
        "f": lambda x: x - 4 + math.log(x),
        "f_prime": lambda x: 1 + 1 / x,
        "x0": 0.5,
        "tol": 0.001,
        "max_iter": 100
    }
]

# Iterar sobre las ecuaciones y resolver
for eq in ecuaciones:
    try:
        root, num_iter = newton_raphson(eq["f"], eq["f_prime"], eq["x0"], eq["tol"], eq["max_iter"])
        print(f"{eq['desc']}:\n\tRaíz aproximada: {root:.6f}\n\tIteraciones realizadas: {num_iter}\n")
    except ValueError as e:
        print(f"{eq['desc']}:\n\t{e}\n")
