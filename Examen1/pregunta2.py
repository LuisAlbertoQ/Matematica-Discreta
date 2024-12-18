
def pregunta_2():
    # Pregunta 2a: División sintética y teorema del residuo
    def synthetic_division(coeffs, root):
        n = len(coeffs)
        new_coeffs = [coeffs[0]]
        for i in range(1, n):
            new_coeffs.append(new_coeffs[-1] * root + coeffs[i])
        return new_coeffs[:-1], new_coeffs[-1]  # Retorna coeficientes y residuo

    p = [1, -6, 11, -6]  # Coeficientes del polinomio
    roots = []
    candidates = [1, 2, 3]  # Raíces posibles por el teorema de las raíces racionales

    for r in candidates:
        _, residue = synthetic_division(p, r)
        if residue == 0:
            roots.append(r)
            p, _ = synthetic_division(p, r)

    print(f"Pregunta 2a: Las raíces reales son: {roots}")

    # Redefiniendo la función P(x) para verificar raíces y ajustar el método de bisección
    def P(x):
        return x**3 - 6*x**2 + 11*x - 6

    # Método de bisección ajustado
    def biseccion(f, a, b, tol):
        error_relativo = float('inf')
        c_old = a
        while error_relativo > tol:
            c = (a + b) / 2  # Punto medio
            if abs(f(c)) < 1e-6:  # Se alcanza una raíz aproximada
                break
            elif f(a) * f(c) < 0:
                b = c
            else:
                a = c
            error_relativo = abs((c - c_old) / c)
            c_old = c

        return c, error_relativo

    # Intervalo [2,3] y tolerancia
    a, b = 2, 3
    tolerancia = 1e-2

    # Ejecutamos el método de bisección
    raiz_biseccion, error_relativo = biseccion(P, a, b, tolerancia)
    print(f"Pregunta 2b: La raíz aproximada por bisección es {raiz_biseccion:.3f} con error relativo {error_relativo:.6f}")

pregunta_2()
