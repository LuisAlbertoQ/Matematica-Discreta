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
    """
    Función tan(x) + x
    """
    return np.tan(x) + x

# Parámetros de la integral
a = 0       # límite inferior
b = 2*np.pi # límite superior
n = 100   # número de subintervalos (aumentado para mejor precisión)

# Dividimos el intervalo para evitar las asíntotas de la tangente
# La tangente tiene asíntotas en x = π/2, 3π/2
# Vamos a dividir la integral en tres partes

def integrate_piecewise():
    try:
        # Primera parte: de 0 a π/2 - ε
        result1 = trapezoidal_rule(f, 0, np.pi/2 - 0.01, n//3)
        
        # Segunda parte: de π/2 + ε a 3π/2 - ε
        result2 = trapezoidal_rule(f, np.pi/2 + 0.01, 3*np.pi/2 - 0.01, n//3)
        
        # Tercera parte: de 3π/2 + ε a 2π
        result3 = trapezoidal_rule(f, 3*np.pi/2 + 0.01, 2*np.pi, n//3)
        
        total = result1 + result2 + result3
        return total
        
    except ValueError as e:
        print(f"Error en el cálculo por partes: {str(e)}")
        return None

try:
    print("Calculando la integral por partes...")
    resultado = integrate_piecewise()
    if resultado is not None:
        print(f"La integral aproximada es: {resultado}")
        print("\nNota: Este resultado es una aproximación debido a que:")
        print(f"1. La función tan(x) tiene asíntotas en x = π/2 y x = 3π/2")
        print("2. Hemos evitado las asíntotas usando pequeños intervalos de exclusión")
    
except Exception as e:
    print(f"No se puede calcular la integral: {str(e)}")