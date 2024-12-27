import numpy as np

def cholesky(A):
    """
    Performs Cholesky decomposition of a symmetric positive-definite matrix A
    Returns lower triangular matrix L such that A = L * L.T
    """
    n = len(A)
    L = np.zeros((n, n))

    for i in range(n):
        for j in range(i + 1):
            if i == j:
                # Diagonal elements
                sum_k = sum(L[i][k] * L[i][k] for k in range(j))
                L[i][j] = np.sqrt(A[i][i] - sum_k)
            else:
                # Non-diagonal elements
                sum_k = sum(L[i][k] * L[j][k] for k in range(j))
                L[i][j] = (A[i][j] - sum_k) / L[j][j]
    
    return L

# Example usage
if __name__ == "__main__":
    # Example matrix
    A = np.array([[4, 12, -16],
                  [12, 37, -43],
                  [-16, -43, 98]], dtype=float)
    
    L = cholesky(A)
    print("Original matrix 1:")
    print(A)
    print("\nCholesky decomposition (L):")
    print(L)
    print("\nVerification (L * L.T):")
    print(np.dot(L, L.T))
    
    #Ejemplo4
    B = np.array([[4, 1, 1],
                  [1, 3, 1],
                  [1, 1, 4]], dtype=float)
    
    b = np.array([7, -8, 6])
    
    
    L = cholesky(B)
    print("\nOriginal matrix 2:")
    print(B)
    print("\nCholesky decomposition (L):")
    print(L)
    print("\nVerification (L * L.T):")
    print(np.dot(L, L.T))
    
    #Solucion

    y = np.linalg.solve(L, b)
    x = np.linalg.solve(L.T, y)
    print("\nSolution:")
    print(f"x = {x}")