import random
import math

# Función objetivo
def funcion_objetivo(x):
    return x**2 + 5*x + 6

# Generar una población inicial de anticuerpos (soluciones)
def generar_poblacion_inicial(tamano_poblacion):
    return [random.uniform(-10, 10) for _ in range(tamano_poblacion)]

# Calcular la aptitud de cada anticuerpo (solución)
def calcular_aptitud(solucion):
    return funcion_objetivo(solucion)

# Seleccionar los mejores anticuerpos para la siguiente generación
def seleccionar_mejores_anticuerpos(poblacion, num_seleccionados):
    return sorted(poblacion, key=calcular_aptitud)[:num_seleccionados]

# Operador de mutación para explorar el espacio de búsqueda
def mutacion(anticuerpo, tasa_mutacion):
    return anticuerpo + random.uniform(-tasa_mutacion, tasa_mutacion)

# Parámetros del algoritmo
tamano_poblacion = 10
num_generaciones = 50
tasa_mutacion = 0.1

# Algoritmo del sistema inmunitario
poblacion = generar_poblacion_inicial(tamano_poblacion)
for _ in range(num_generaciones):
    # Selección de los mejores anticuerpos
    mejores_anticuerpos = seleccionar_mejores_anticuerpos(poblacion, 2)
    
    # Mutación de los mejores anticuerpos
    nuevos_anticuerpos = [mutacion(anticuerpo, tasa_mutacion) for anticuerpo in mejores_anticuerpos]
    
    # Agregar los nuevos anticuerpos a la población
    poblacion.extend(nuevos_anticuerpos)

# Encontrar la mejor solución en la población final
mejor_solucion = min(poblacion, key=calcular_aptitud)

# Mostrar la mejor solución y su valor
print("La mejor solución encontrada es:", mejor_solucion)
print("El valor mínimo encontrado es:", calcular_aptitud(mejor_solucion))
