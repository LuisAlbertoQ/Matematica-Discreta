import numpy as np
import matplotlib.pyplot as plt

def regresion_lineal(x, y):
    """
    Calcula la regresión lineal usando el método de mínimos cuadrados.
    
    Parámetros:
    x: array de variables independientes
    y: array de variables dependientes
    
    Retorna:
    m: pendiente
    b: intersección
    y_pred: valores predichos
    r2: coeficiente de determinación
    """
    n = len(x)
    
    # Calcular las sumas necesarias
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(x * y)
    sum_x2 = np.sum(x**2)
    
    # Calcular pendiente (m) y punto de intersección (b)
    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
    b = (sum_y - m * sum_x) / n
    
    # Calcular la línea de regresión
    y_pred = m * x + b
    
    # Calcular el coeficiente de determinación R^2
    r2 = np.sum((y_pred - np.mean(y))**2) / np.sum((y - np.mean(y))**2)
    
    return m, b, y_pred, r2

def resolver_ejemplo():
    # Nuevos datos del problema
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2.1, 4.3, 6.5, 8.0, 10.1])
    
    # # 1. Calcular medias
    # x_media = np.mean(x)
    # y_media = np.mean(y)
    
    # print("1. Cálculo de medias:")
    # print(f"Media de x (𝑥᪄): {x_media}")
    # print(f"Media de y (𝑦᪄): {y_media}")
    
    print("Datos del problema:")
    print("x:", x)
    print("y:", y)
    # 2. Calcular regresión lineal
    m, b, y_pred, r2 = regresion_lineal(x, y)
    
    print("\n1. Parámetros de la regresión:")
    print(f"b (pendiente): {m:.4f}")
    print(f"a (intersección): {b:.4f}")
    print(f"R²: {r2:.4f}")
    
    print("\n2. Ecuación de la recta:")
    print(f"y = {b:.4f} + {m:.4f}x")
    
    # Crear la visualización
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color='blue', label='Datos originales')
    plt.plot(x, y_pred, color='red', label='Línea de regresión')
    
    # Añadir elementos a la gráfica
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Regresión Lineal por Mínimos Cuadrados')
    plt.legend()
    plt.grid(True)
    
    # Añadir la ecuación en la gráfica
    ecuacion = f'y = {b:.4f} + {m:.4f}x\nR² = {r2:.4f}'
    plt.text(0.05, 0.95, ecuacion, transform=plt.gca().transAxes,
            bbox=dict(facecolor='white', alpha=0.8))
    
    plt.show()

if __name__ == "__main__":
    resolver_ejemplo()