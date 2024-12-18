import numpy as np

def f(x):
    """Función f(x) = (x-3)(x²+1) = x³ - 3x² + x - 3"""
    return x**3 - 3*x**2 + x - 3

def find_multiple_roots(f, initial_guesses=None):
    """
    Encuentra múltiples raíces de una función usando diferentes métodos de inicialización
    
    Parámetros:
    f: función a la que se le buscan las raíces
    initial_guesses: lista de puntos iniciales para comenzar la búsqueda
    """
    # Si no se proporcionan puntos iniciales, usar un conjunto predeterminado
    if initial_guesses is None:
        initial_guesses = [-2, 0, 2, 3, -1, 1]
    
    # Conjunto para almacenar raíces únicas
    roots = set()
    
    # Tolerancia para considerar raíces cercanas
    tolerance = 1e-6
    
    for guess in initial_guesses:
        # Usar el método de Newton para encontrar la raíz
        root = newton_method(f, guess)
        
        # Verificar si la raíz ya no ha sido encontrada previamente
        if not any(abs(root - existing_root) < tolerance for existing_root in roots):
            roots.add(root)
    
    return sorted(roots)

def newton_method(f, x0, max_iter=100, tolerance=1e-6):
    """
    Método de Newton para encontrar raíces
    
    Parámetros:
    f: función a la que se le busca la raíz
    x0: punto inicial
    max_iter: máximo número de iteraciones
    tolerance: tolerancia para convergencia
    """
    def df(x, h=1e-5):
        """Derivada numérica"""
        return (f(x + h) - f(x)) / h
    
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        
        # Criterio de convergencia
        if abs(fx) < tolerance:
            return x
        
        # Método de Newton
        dfx = df(x)
        
        # Evitar división por cero
        if abs(dfx) < tolerance:
            break
        
        x = x - fx / dfx
    
    return x

# Encontrar las raíces
roots = find_multiple_roots(f)

# Imprimir resultados
print("Raíces encontradas:")
for i, root in enumerate(roots, 1):
    print(f"Raíz {i}: {root}")
    print(f"Valor de f(x) en la raíz: {f(root)}\n")

# Verificación usando numpy para comparación
poly_roots = np.roots([1, -3, 1, -3])
print("Raíces de numpy para comparación:")
for root in poly_roots:
    print(f"{root.real}")