import math

def g(x):
    """Función trascendental g(x) = ln(x) + x^2 - 4"""
    return math.log(x) + x**2 - 4

def falsa_posicion(f, a, b, tolerancia=1e-3, max_iter=100):
    """Método de la falsa posición para encontrar raíz"""
    fa = f(a)
    fb = f(b)
    
    if fa * fb > 0:
        raise ValueError("La función no cambia de signo en el intervalo")
    
    iteraciones = []
    
    for i in range(max_iter):
        # Calcular punto de intersección
        x = b - fb * (b - a) / (fb - fa)
        
        fx = f(x)
        iteraciones.append(x)
        
        # Criterio de parada
        if abs(fx) < tolerancia:
            return x, iteraciones
        
        # Actualizar intervalo
        if fa * fx < 0:
            b = x
            fb = fx
        else:
            a = x
            fa = fx
    
    raise ValueError("Método no convergió")

def metodo_secante(f, x0, x1, tolerancia=1e-3, max_iter=100):
    """Método de la secante para encontrar raíz"""
    iteraciones = [x0, x1]
    
    for i in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)
        
        # Calcular siguiente punto
        x = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        iteraciones.append(x)
        
        # Criterio de parada
        if abs(f(x)) < tolerancia:
            return x, iteraciones
        
        # Actualizar puntos
        x0, x1 = x1, x
    
    raise ValueError("Método no convergió")

def resolver_ecuacion_trascendental():
    # a) Método de la falsa posición
    print("a) Método de la Falsa Posición:")
    raiz_falsa_posicion, iter_falsa = falsa_posicion(g, 1, 2)
    print(f"Raíz: {raiz_falsa_posicion}")
    print(f"Número de iteraciones: {len(iter_falsa)}")
    print(f"Valor de la función en la raíz: {g(raiz_falsa_posicion)}")
    
    # b) Método de la secante
    print("\nb) Método de la Secante:")
    raiz_secante, iter_secante = metodo_secante(g, 1.5, 1.6)
    print(f"Raíz: {raiz_secante}")
    print(f"Número de iteraciones: {len(iter_secante)}")
    print(f"Valor de la función en la raíz: {g(raiz_secante)}")
    
    # Comparación
    print("\nc) Comparación:")
    print(f"Diferencia entre métodos: {abs(raiz_falsa_posicion - raiz_secante)}")

# Ejecutar la resolución
resolver_ecuacion_trascendental()