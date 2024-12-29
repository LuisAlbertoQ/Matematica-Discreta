import numpy as np

def jacobi_method(A, b, x0, num_iter=2):
    """
    Solves a system of linear equations using Jacobi method for a specific number of iterations.
    
    Parameters:
    A: coefficient matrix
    b: right-hand side vector
    x0: initial guess
    num_iter: number of iterations to perform
    
    Returns:
    x_history: list of solutions for each iteration
    """
    
    n = len(A)
    x = x0.copy()
    x_history = [x0.copy()]  # Para guardar todas las iteraciones
    
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

# Definir el sistema
A = np.array([
    [10, 2, -1],
    [-3, -6, 2],
    [1, 1, 5]
])

b = np.array([27, -61.5, -21.5])
x0 = np.zeros(3)

# Resolver el sistema
soluciones = jacobi_method(A, b, x0)

# Mostrar resultados
print("Matriz A:")
print(A)
print("\nVector b:")
print(b)
print("Vector inicial (x0, y0, z0):", soluciones[0])
print("\nPrimera iteración (x1, y1, z1):", soluciones[1])
print("\nSegunda iteración (x2, y2, z2):", soluciones[2])

# Verificar los resultados calculando Ax = b para la última iteración
print("\nVerificación de la última iteración:")
print("Ax =", A @ soluciones[2])
print("b  =", b)