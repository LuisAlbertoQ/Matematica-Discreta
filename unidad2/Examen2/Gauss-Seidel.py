import numpy as np

def jacobi_method(A, b, x0, num_iter=2):
    """
    Método de Jacobi para un número específico de iteraciones
    """
    n = len(A)
    x = x0.copy()
    x_history = [x0.copy()]
    
    for iteration in range(num_iter):
        x_new = x.copy()
        for i in range(n):
            sum_ax = 0
            for j in range(n):
                if i != j:
                    sum_ax += A[i,j] * x[j]
            x_new[i] = (b[i] - sum_ax) / A[i,i]
        
        x = x_new.copy()
        x_history.append(x.copy())
    
    return x_history

def gauss_seidel(A, b, x0, num_iter=2):
    """
    Método de Gauss-Seidel para un número específico de iteraciones
    """
    n = len(A)
    x = x0.copy()
    x_history = [x0.copy()]
    
    for iteration in range(num_iter):
        x_old = x.copy()
        for i in range(n):
            sum1 = sum(A[i][j] * x[j] for j in range(i))
            sum2 = sum(A[i][j] * x_old[j] for j in range(i + 1, n))
            x[i] = (b[i] - sum1 - sum2) / A[i,i]
        x_history.append(x.copy())
    
    return x_history

# Definir el sistema
A = np.array([
    [10, 2, -1],
    [-3, -6, 2],
    [1, 1, 5]
])

b = np.array([27, -61.5, -21.5])
x0 = np.zeros(3)

# Resolver usando ambos métodos
jacobi_soluciones = jacobi_method(A, b, x0)
gauss_soluciones = gauss_seidel(A, b, x0)

# Mostrar resultados
print("=== Comparación de Métodos ===")
print("\nVector inicial (x0, y0, z0):", x0)

print("\n=== Método de Jacobi ===")
print("Primera iteración:", jacobi_soluciones[1])
print("Segunda iteración:", jacobi_soluciones[2])
print("Error en última iteración:", np.linalg.norm(A @ jacobi_soluciones[2] - b))

print("\n=== Método de Gauss-Seidel ===")
print("Primera iteración:", gauss_soluciones[1])
print("Segunda iteración:", gauss_soluciones[2])
print("Error en última iteración:", np.linalg.norm(A @ gauss_soluciones[2] - b))

# Comparar la diferencia entre los métodos
diff = np.abs(jacobi_soluciones[2] - gauss_soluciones[2])
print("\n=== Diferencia entre métodos en la segunda iteración ===")
print("Diferencia absoluta:", diff)
print("Diferencia relativa:", diff / np.abs(gauss_soluciones[2]) * 100, "%")