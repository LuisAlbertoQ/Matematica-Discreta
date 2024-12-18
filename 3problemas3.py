import math

def metodo_secante(f, x0, x1, tol, max_iter):
    """
    Implementa el método de la secante para resolver f(x) = 0.

    Parámetros:
    f: función objetivo.
    x0, x1: dos aproximaciones iniciales.
    tol: tolerancia aceptable para el error entre iteraciones consecutivas.
    max_iter: número máximo de iteraciones permitidas.

    Retorna:
    Una tupla con la raíz aproximada y el número de iteraciones realizadas.
    Si no converge, genera una excepción.
    """
    for i in range(max_iter):
        # Calcula el siguiente punto usando la fórmula de la secante
        if f(x1) - f(x0) == 0:
            raise ValueError("División por cero en el método de la secante.")
        
        x_next = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        
        # Verifica la tolerancia
        if abs(x_next - x1) < tol:
            return x_next, i + 1  # Retorna la raíz y el número de iteraciones
        
        # Actualiza los puntos
        x0, x1 = x1, x_next
    
    raise ValueError("El método no convergió dentro del número máximo de iteraciones.")

# Resolver las ecuaciones dadas:
ecuaciones = [
    {
        "desc": "f(x) = x - cos(x)",
        "f": lambda x: x - math.cos(x),
        "x0": 0.5,
        "x1": 1.0,
        "tol": 0.05,
        "max_iter": 100
    },
    {
        "desc": "f(x) = x^3 - x - 1",
        "f": lambda x: x**3 - x - 1,
        "x0": 1.0,
        "x1": 1.5,
        "tol": 0.05,
        "max_iter": 100
    },
    {
        "desc": "f(x) = x^2 - 2",
        "f": lambda x: x**2 - 2,
        "x0": 1.0,
        "x1": 2.0,
        "tol": 1e-5,
        "max_iter": 100
    },
    {
        "desc": "f(x) = x - 4 + ln(x)",
        "f": lambda x: x - 4 + math.log(x),
        "x0": 2.0,
        "x1": 3.0,
        "tol": 0.001,
        "max_iter": 100
    }
]

# Iterar sobre las ecuaciones y resolver
for eq in ecuaciones:
    try:
        root, num_iter = metodo_secante(eq["f"], eq["x0"], eq["x1"], eq["tol"], eq["max_iter"])
        print(f"{eq['desc']}:\n\tRaíz aproximada: {root:.6f}\n\tIteraciones realizadas: {num_iter}\n")
    except ValueError as e:
        print(f"{eq['desc']}:\n\t{e}\n")
