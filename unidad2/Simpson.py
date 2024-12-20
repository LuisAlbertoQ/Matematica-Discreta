def simpson_13(f, a, b, n):
    """
    Aproxima la integral de f(x) desde a hasta b usando la Regla de Simpson 1/3.
    
    :param f: Función a integrar.
    :param a: Límite inferior de integración.
    :param b: Límite superior de integración.
    :param n: Número de subintervalos (debe ser par).
    :return: Aproximación de la integral.
    """
    if n % 2 != 0:
        raise ValueError("El número de subintervalos n debe ser par.")
    
    h = (b - a) / n  # Ancho de cada subintervalo
    integral = f(a) + f(b)  # Sumar los extremos

    # Sumar los términos impares
    for i in range(1, n, 2):
        integral += 4 * f(a + i * h)

    # Sumar los términos pares
    for i in range(2, n-1, 2):
        integral += 2 * f(a + i * h)

    integral *= h / 3  # Multiplicar por h/3
    return integral

# Ejemplo de uso
if __name__ == "__main__":
    import numpy as np

    # Definimos la función a integrar
    def f(x):
        return np.tan(x) + x

    # Límites de integración
    a = 0
    b = 2 * np.pi

    # Número de subintervalos (debe ser par)
    n = 10

    # Calcular la integral
    resultado = simpson_13(f, a, b, n)
    print(f"La aproximación de la integral es: {resultado}")