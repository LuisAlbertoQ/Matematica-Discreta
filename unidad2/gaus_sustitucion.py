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

def print_substitution_step(i, equation_parts, result):
    """
    Imprime los pasos de la sustitución hacia atrás
    """
    print(f"\nPaso de sustitución para x{i+1}:")
    print("  " + " + ".join(equation_parts) + f" = {result:.4f}")

def gauss_elimination(A, b):
    """
    Resuelve un sistema de ecuaciones lineales usando el método de eliminación de Gauss
    con visualización paso a paso completa
    """
    # Convertir a matrices numpy si no lo son ya
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(A)
    
    # Concatenar A y b para formar la matriz aumentada
    Ab = np.concatenate((A, b.reshape(n,1)), axis=1)
    
    print_matrix(Ab, "Matriz inicial aumentada:")
    
    # Eliminación hacia adelante
    for i in range(n):
        # Encontrar el pivote máximo en la columna actual
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
        
        # Hacer ceros debajo del pivote
        for k in range(i + 1, n):
            factor = Ab[k][i] / Ab[i][i]
            Ab[k] = Ab[k] - factor * Ab[i]
            print_matrix(Ab, f"Eliminación en fila {k+1}:")
    
    print_matrix(Ab, "Matriz triangular superior:")
    
    print("\nIniciando sustitución hacia atrás:")
    # Sustitución hacia atrás
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        # Preparar la ecuación para mostrarla
        equation_parts = []
        sum_val = Ab[i][n]
        
        # Mostrar los términos conocidos
        for j in range(i+1, n):
            if Ab[i][j] != 0:
                term_val = Ab[i][j] * x[j]
                equation_parts.append(f"{Ab[i][j]:.4f}·{x[j]:.4f}")
                sum_val -= term_val
        
        # Agregar el término que estamos calculando
        if len(equation_parts) > 0:
            equation = f"{Ab[i][i]:.4f}·x{i+1} + " + " + ".join(equation_parts) + f" = {Ab[i][n]:.4f}"
        else:
            equation = f"{Ab[i][i]:.4f}·x{i+1} = {Ab[i][n]:.4f}"
        
        print(f"\nEcuación para x{i+1}:")
        print(equation)
        
        # Calcular x[i]
        x[i] = sum_val / Ab[i][i]
        print(f"Despejando: x{i+1} = {sum_val:.4f} / {Ab[i][i]:.4f} = {x[i]:.4f}")
    
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
    print("\nResolviendo...")
    
    try:
        solution = gauss_elimination(A, b)
        print("\nSolución final del sistema:")
        for i, val in enumerate(solution):
            print(f"x{i+1} = {val:.4f}")
    except Exception as e:
        print("Error al resolver el sistema:", str(e))