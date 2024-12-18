import numpy as np
import math
import matplotlib.pyplot as plt

def pregunta_1():
    # a) Método Gráfico
    def f(x):
        return math.exp(x) - 3 * x**2
    
    # Gráfica para visualizar raíz
    x = np.linspace(-1, 2, 200)
    y = [f(xi) for xi in x]
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='f(x) = e^x - 3x²')
    plt.title('Método Gráfico: Búsqueda de Raíz')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.axhline(y=0, color='r', linestyle='--')
    plt.grid(True)
    plt.legend()
    plt.show()
    
    # b) Newton-Raphson
    def newton_raphson(f, df, x0, tol=1e-3, max_iter=100):
        x = x0
        for i in range(max_iter):
            fx = f(x)
            if abs(fx) < tol:
                return x, i+1
            dfx = df(x)
            x = x - fx/dfx
        return None, max_iter
    
    def f(x):
        return math.exp(x) - 3 * x**2
    
    def df(x):
        return math.exp(x) - 6 * x
    
    x0 = 1
    root, iterations = newton_raphson(f, df, x0)
    
    print("\nPregunta 1 Resultados:")
    print(f"Raíz aproximada: {root}")
    print(f"Iteraciones: {iterations}")
    print(f"f(raíz) = {f(root)}")
    
    return root

pregunta_1()