import math
import random

def funcion_objetivo(solucion):
    # Define tu función objetivo que quieres minimizar
    # En este ejemplo, se utiliza la función cuadrática f(x) = x^2
    return solucion**2

def recocido_simulado(solucion_inicial, temperatura_inicial, factor_enfriamiento, iteraciones):
    solucion_actual = solucion_inicial
    temperatura_actual = temperatura_inicial

    for i in range(iteraciones):
        # Genera una solución vecina
        solucion_vecina = solucion_actual + random.uniform(-1, 1)

        # Calcula la diferencia en la función objetivo
        delta_objetivo = funcion_objetivo(solucion_vecina) - funcion_objetivo(solucion_actual)

        # Decide si aceptar la solución vecina
        if delta_objetivo < 0 or random.uniform(0, 1) < math.exp(-delta_objetivo / temperatura_actual):
            solucion_actual = solucion_vecina

        # Enfría la temperatura
        temperatura_actual *= factor_enfriamiento

    return solucion_actual

# Parámetros del algoritmo
solucion_inicial = 2.0
temperatura_inicial = 100.0
factor_enfriamiento = 0.95
iteraciones = 1000

# Ejecuta el algoritmo de Recocido Simulado
solucion_optima = recocido_simulado(solucion_inicial, temperatura_inicial, factor_enfriamiento, iteraciones)

print("Solución óptima encontrada:", solucion_optima)
print("Valor de la función objetivo en la solución óptima:", funcion_objetivo(solucion_optima))
