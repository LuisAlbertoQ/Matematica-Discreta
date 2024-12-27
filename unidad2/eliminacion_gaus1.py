import numpy as np

def print_matrix(Ab, step=""):
    """
    Imprime la matriz aumentada de manera formateada
    """
    if step:
        print(f"\n{step}")
    
    n = len(Ab)
    for i in range(n):
        for j in range(n + 1):
            if j == n:
                print(f"| {Ab[i][j]:8.4f}", end=" ")
            else:
                print(f"{Ab[i][j]:8.4f}", end=" ")
        print()
    print()

def gauss_jordan(A, b):
    """
    Resuelve un sistema de ecuaciones lineales usando el método de Gauss-Jordan
    con visualización paso a paso
    """
    # Convertir a matrices numpy
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(A)
    
    # Crear matriz aumentada
    Ab = np.concatenate((A, b.reshape(n,1)), axis=1)
    print_matrix(Ab, "Matriz inicial aumentada:")
    
    # Proceso de Gauss-Jordan
    for i in range(n):
        # Paso 1: Encontrar el pivote máximo en la columna actual
        pivot = abs(Ab[i][i])
        pivot_row = i
        for k in range(i + 1, n):
            if abs(Ab[k][i]) > pivot:
                pivot = abs(Ab[k][i])
                pivot_row = k
        
        # Intercambiar filas si es necesario
        if pivot_row != i:
            Ab[i], Ab[pivot_row] = Ab[pivot_row].copy(), Ab[i].copy()
            print_matrix(Ab, f"Intercambio de filas {i+1} y {pivot_row+1}:")
        
        # Paso 2: Hacer 1 el pivote
        pivot = Ab[i][i]
        if pivot != 1:
            Ab[i] = Ab[i] / pivot
            print_matrix(Ab, f"Normalización de fila {i+1} (dividir por {pivot:.4f}):")
        
        # Paso 3: Hacer ceros en toda la columna (arriba y abajo del pivote)
        for k in range(n):
            if k != i:
                factor = Ab[k][i]
                if factor != 0:
                    Ab[k] = Ab[k] - factor * Ab[i]
                    print_matrix(Ab, f"Eliminación en fila {k+1}:")
    
    print_matrix(Ab, "Matriz final (forma escalonada reducida):")
    
    # Extraer la solución
    x = Ab[:,n]
    
    return x

# Ejemplo con matriz 3x3
if __name__ == "__main__":
    # Sistema ejemplo:
    # 2x + y + z = 9
    # x + 3y + z = 13
    # x + y + 4z = 17
    
    A = np.array([
        [1, 1, 2],
        [1, 0, 3],
        [1, -1, 1]
    ])
    
    b = np.array([2, 5, 1])
    
    print("Sistema de ecuaciones:")
    print("2x + y + z = 9")
    print("x + 3y + z = 13")
    print("x + y + 4z = 17")
    print("\nResolviendo usando el método de Gauss-Jordan...")
    
    try:
        solution = gauss_jordan(A, b)
        print("\nSolución final del sistema:")
        for i, val in enumerate(solution):
            print(f"x{i+1} = {val:.4f}")
    except Exception as e:
        print("Error al resolver el sistema:", str(e))