import numpy as np

def gauss_seidel(A, b, x0, tol=1e-6, max_iter=100):
    """
    Solves the system Ax = b using Gauss-Seidel method
    A: coefficient matrix
    b: right hand side vector
    x0: initial guess
    tol: tolerance for convergence
    max_iter: maximum number of iterations
    """
    n = len(A)
    x = x0.copy()
    
    for iter in range(max_iter):
        x_old = x.copy()
        
        for i in range(n):
            sum1 = sum(A[i][j] * x[j] for j in range(i))
            sum2 = sum(A[i][j] * x_old[j] for j in range(i + 1, n))
            x[i] = (b[i] - sum1 - sum2) / A[i][i]
        
        # Check convergence
        if np.allclose(x, x_old, rtol=tol):
            print(f"Convergido en {iter + 1} iteraciones")
            return x
    
    print("El método no convergió")
    return x

# Ejemplo de uso
if __name__ == "__main__":
    # Sistema de ejemplo: 
    # 4x + y - z = 7
    # -x + 3y + z = 3
    # 2x + y + 5z = 10
    
    A = np.array([[4, 1, 1],
                  [1, 3, 1],
                  [1, 1, 4]])
    
    b = np.array([7, -8, 6])
    x0 = np.zeros(3)
    
    solution = gauss_seidel(A, b, x0)
    print("Solución:", solution)