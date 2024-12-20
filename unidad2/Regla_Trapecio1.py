import numpy as np

def trapezoidal_rule(f, a, b, n):
    """
    Calcula la integral definida usando la regla del trapecio
    
    Parámetros:
    f: función a integrar
    a: límite inferior
    b: límite superior
    n: número de subintervalos
    
    Retorna:
    float: aproximación de la integral
    """
    try:
        # Verifica que los límites sean válidos
        if a >= b:
            raise ValueError("El límite inferior debe ser menor que el superior")
            
        # Calcula el tamaño del paso
        h = (b - a) / n
        
        # Crea los puntos x
        x = np.linspace(a, b, n+1)
        
        # Evalúa la función en todos los puntos
        try:
            y = f(x)
            
            # Verifica si hay valores infinitos o NaN
            if np.any(np.isnan(y)) or np.any(np.isinf(y)):
                raise ValueError("La función produce valores indefinidos o infinitos en el intervalo dado")
                
            # Aplica la regla del trapecio
            integral = h * (y[0]/2 + np.sum(y[1:-1]) + y[-1]/2)
            
            return integral
            
        except Exception as e:
            raise ValueError(f"Error al evaluar la función: {str(e)}")
            
    except Exception as e:
        raise ValueError(f"Error en el cálculo: {str(e)}")

def f(x):
    return x**2 + 3*x + 1

# Parámetros de la integral
a = -2  # límite inferior
b = 2   # límite superior
n = 100  # número de subintervalos (aumentado para mejor precisión)

try:
    # Intentamos calcular la integral
    print("Intentando calcular la integral...")
    resultado = trapezoidal_rule(f, a, b, n)
    print(f"La integral aproximada es: {resultado}")
    
except ValueError as e:
    print(f"No se puede calcular la integral: {str(e)}")
    print("La integral no está definida en todo el intervalo [-2, 2] porque:")
    print("1. ln(x) no está definido para x ≤ 0")
    print("2. 2/x tiene una singularidad en x = 0")