import cmath

def muller(f, x0, x1, x2, tol=1e-6, max_iter=100):
    """
    Método de Muller para encontrar una raíz de la función f, con contador de iteraciones.
    
    Parámetros:
        f: Función cuyo cero se desea encontrar.
        x0, x1, x2: Tres valores iniciales cercanos a la raíz.
        tol: Tolerancia para el criterio de convergencia.
        max_iter: Máximo número de iteraciones.
        
    Retorna:
        Una tupla (raíz, iteraciones), donde:
        - raíz: Aproximación de la raíz de f.
        - iteraciones: Número de iteraciones realizadas.
    """
    for i in range(max_iter):
        # Calculamos los valores de la función en los puntos iniciales
        f0, f1, f2 = f(x0), f(x1), f(x2)
        
        # Coeficientes de la interpolación cuadrática
        h1, h2 = x1 - x0, x2 - x1
        δ1, δ2 = (f1 - f0) / h1, (f2 - f1) / h2
        a = (δ2 - δ1) / (h2 + h1)
        b = a * h2 + δ2
        c = f2
        
        # Calculamos las raíces del polinomio cuadrático
        discriminant = cmath.sqrt(b**2 - 4 * a * c)
        if abs(b + discriminant) > abs(b - discriminant):
            denominator = b + discriminant
        else:
            denominator = b - discriminant
        
        dx = -2 * c / denominator
        x3 = x2 + dx
        
        # Verificar convergencia
        if abs(dx) < tol:
            return x3.real if abs(x3.imag) < tol else x3, i + 1
        
        # Actualizamos los valores para la siguiente iteración
        x0, x1, x2 = x1, x2, x3
    
    raise ValueError("El método de Muller no convergió después de {} iteraciones.".format(max_iter))

# Ejemplo de uso
if __name__ == "__main__":
    def f(x):
        return x**3 - (3*x)**2 + x - 3  # Ejemplo: f(x) = x^3 - x - 1
    
    # Valores iniciales
    x0, x1, x2 = -1, 1, 0
    
    # Encontrar la raíz
    raiz, iteraciones = muller(f, x0, x1, x2)
    print(f"Raíz encontrada: {raiz}")
    print(f"Iteraciones: {iteraciones}")

#Ejemplo 6
"""
if __name__ == "__main__":
    def f(x):
        return x**5 - 2  # Ejemplo: f(x) = x^3 - x - 1
    
    # Valores iniciales
    x0, x1, x2 = 0, 2, 1
    
    # Encontrar la raíz
    raiz, iteraciones = muller(f, x0, x1, x2)
    print(f"Raíz encontrada: {raiz}, Iteraciones: {iteraciones}")
"""
#Ejemplo 7
"""
if __name__ == "__main__":
    
    def f(x):
        return x**3 - 3*x**2 + x - 3  # Ejemplo: f(x) = x^3 - x - 1
    
    # Valores iniciales
    x0, x1, x2 = -1, 1, 0
    
    # Encontrar la raíz
    raiz = muller(f, x0, x1, x2)
    print("Raíz encontrada:", raiz)
"""