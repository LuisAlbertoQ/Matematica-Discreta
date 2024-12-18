import numpy as np

def evaluar_polinomio(coeficientes, x):
    """Evalúa el polinomio en un punto x."""
    return sum(c * (x ** i) for i, c in enumerate(reversed(coeficientes)))

def encontrar_raiz_racional(coeficientes):
    """Encuentra una raíz racional usando el teorema de las raíces racionales."""
    divisores = [1, -1, 2, -2, 4, -4]  # Divisores de 4
    for raiz in divisores:
        if evaluar_polinomio(coeficientes, raiz) == 0:
            return raiz
    return None

def division_sintetica(coeficientes, raiz):
    """Realiza la división sintética del polinomio por (x - raiz)."""
    nuevo_coeficientes = [coeficientes[0]]  # Primer coeficiente
    for i in range(1, len(coeficientes)):
        nuevo_coeficientes.append(coeficientes[i] + nuevo_coeficientes[i-1] * raiz)
    return nuevo_coeficientes[:-1]  # Retorna los coeficientes del polinomio reducido

def encontrar_raices_cuadraticas(coeficientes):
    """Encuentra las raíces de un polinomio cuadrático."""
    a, b, c = coeficientes
    discriminante = b**2 - 4*a*c
    if discriminante >= 0:
        r1 = (-b + np.sqrt(discriminante)) / (2*a)
        r2 = (-b - np.sqrt(discriminante)) / (2*a)
        return r1, r2
    else:
        r1 = (-b + np.sqrt(-discriminante) * 1j) / (2*a)
        r2 = (-b - np.sqrt(-discriminante) * 1j) / (2*a)
        return r1, r2

# Coeficientes del polinomio f(x) = x^4 - 2x^3 - 4x^2 + 4x + 4
coeficientes = [1, -2, -4, 4, 4]

# a) Encontrar una raíz racional
raiz_racional = encontrar_raiz_racional(coeficientes)
print(f"Raíz racional encontrada: {raiz_racional}")

# b) Reducir el polinomio
if raiz_racional is not None:
    coeficientes_reducidos = division_sintetica(coeficientes, raiz_racional)
    print(f"Coeficientes del polinomio reducido: {coeficientes_reducidos}")

    # Encontrar las raíces del polinomio cuadrático resultante
    raices_cuadraticas = encontrar_raices_cuadraticas(coeficientes_reducidos)
    print(f"Raíces del polinomio cuadrático: {raices_cuadraticas}")
else:
    print("No se encontró una raíz racional.")

# c) Verificación de una raíz compleja
raiz_compleja = 1 + 1j  # Ejemplo de raíz compleja
verificacion = evaluar_polinomio(coeficientes, raiz_compleja)
print(f"Verificación de la raíz compleja {raiz_compleja}: f({raiz_compleja}) = {verificacion}")
