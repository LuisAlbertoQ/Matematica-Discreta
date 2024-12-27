import numpy as np

def jacobi_method(A, b, x0, tol=1e-6, max_iter=100):
    """
    Solves a system of linear equations using Jacobi method.
    
    Parameters:
    A: coefficient matrix
    b: right-hand side vector
    x0: initial guess
    tol: tolerance for convergence
    max_iter: maximum number of iterations
    
    Returns:
    x: solution vector
    iterations: number of iterations performed
    """
    
    n = len(A)
    x = x0.copy()
    x_new = x.copy()
    iterations = 0
    
    while iterations < max_iter:
        for i in range(n):
            sum_ax = 0
            for j in range(n):
                if i != j:
                    sum_ax += A[i,j] * x[j]
            x_new[i] = (b[i] - sum_ax) / A[i,i]
        
        # Check for convergence
        if np.allclose(x, x_new, rtol=tol):
            return x_new, iterations
        
        x = x_new.copy()
        iterations += 1
    
    return x, iterations

# Example usage
if __name__ == "__main__":
    # Example system 1: 
    # 4x + y + z = 6
    # x + 4y + z = 7
    # x + y + 4z = 7
    
    A = np.array([[3, 1],
                  [1, 4]])
    b = np.array([5, 6])
    x0 = np.zeros(2)
    
    solution, iters = jacobi_method(A, b, x0)
    print("First system:")
    print(f"Solution: {solution}")
    print(f"Iterations: {iters}")

    
    #Ejemplo 4
    B = np.array([[4, 1, 1],
                  [1, 3, 1],
                  [1, 1, 4]])
    b2 = np.array([7, -8, 6])
    x02 = np.zeros(3)
    
    solution2, iters2 = jacobi_method(B, b2, x02)
    print("\nSecond system:")
    print(f"Solution: {solution2}")
    print(f"Iterations: {iters2}")