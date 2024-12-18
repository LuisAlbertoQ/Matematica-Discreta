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
    # Definir la función g(x)
    def g(x):
        return math.exp(-x)  # Ejemplo de función iterativa

    # Parámetros iniciales
    x0 = 0  # Aproximación inicial
    tol = 1e-6  # Tolerancia
    max_iter = 100  # Número máximo de iteraciones

    try:
        raiz, iteraciones = metodo_iterativo(g, x0, tol, max_iter)
        print(f"Raíz aproximada: {raiz}")
        print(f"Iteraciones realizadas: {iteraciones}")
    except ValueError as e:
        print(e)