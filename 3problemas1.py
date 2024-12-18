import math

def metodo_iterativo(g, x0, tol, max_iter):
    """
    Implementa el método iterativo para resolver x = g(x).

    Parámetros:
    g: función iterativa g(x) que define el problema.
    x0: aproximación inicial.
    tol: tolerancia aceptable para el error entre iteraciones consecutivas.
    max_iter: número máximo de iteraciones permitidas.

    Retorna:
    Una tupla con la raíz aproximada y el número de iteraciones realizadas.
    Si no converge, genera una excepción.
    """
    xn = x0  # Aproximación inicial
    for i in range(max_iter):
        xn1 = g(xn)  # Calcula el siguiente valor iterativo
        # Verifica la tolerancia
        if abs(xn1 - xn) < tol:
            return xn1, i + 1  # Retorna la raíz aproximada y el número de iteraciones
        xn = xn1  # Actualiza xn para la siguiente iteración

    # Si no converge dentro del máximo de iteraciones, lanza un error
    raise ValueError("El método no converge después de {} iteraciones".format(max_iter))


# Ejemplo de uso:
if __name__ == "__main__":
    ecuaciones = [
        {"func": lambda x: math.cos(x), "x0": 0.5, "tol": 0.05, "max_iter": 100, "desc": "f(x) = x - cos(x)"},
        {"func": lambda x: (x + 1)**(1/3), "x0": 1.5, "tol": 0.05, "max_iter": 100, "desc": "f(x) = x^3 - x - 1"},
        {"func": lambda x: math.sqrt(2), "x0": 1.5, "tol": 1e-5, "max_iter": 100, "desc": "f(x) = x^2 - 2"},
        {"func": lambda x: 4 - math.log(x), "x0": 2, "tol": 0.001, "max_iter": 100, "desc": "f(x) = x - 4 + ln(x)"}
    ]

    for eq in ecuaciones:
        try:
            raiz, iteraciones = metodo_iterativo(eq["func"], eq["x0"], eq["tol"], eq["max_iter"])
            print(f"{eq['desc']}:\n\tRaíz aproximada: {raiz}\n\tIteraciones realizadas: {iteraciones}\n")
        except ValueError as e:
            print(f"{eq['desc']}:\n\t{e}\n")
