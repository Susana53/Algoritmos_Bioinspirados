import random  # Se importa el módulo random para generar números aleatorios.

# Parámetros del algoritmo genético de conejos
tamaño_poblacion = 20  
tasa_mutacion = 0.1  
generaciones = 30  

# Función para inicializar la población de conejos
def inicializar_poblacion():
    
    return [[random.randint(1, 10)] for _ in range(tamaño_poblacion)]

# Función para evaluar la aptitud de un conejo (en este caso, su tamaño)
def evaluar_aptitud(conejo):
    
    return conejo[0]

# Función para seleccionar conejos para la reproducción (ruleta)
def seleccionar_padres(poblacion):
    
    total_aptitudes = sum(evaluar_aptitud(conejo) for conejo in poblacion)
    probabilidades_seleccion = [evaluar_aptitud(conejo) / total_aptitudes for conejo in poblacion]
    padres = random.choices(poblacion, weights=probabilidades_seleccion, k=2)
    
    return padres

# Función para realizar el cruce entre dos padres
def cruzar(padre1, padre2):
    
    if len(padre1) == 1:
        punto_cruce = 0
    else:
        punto_cruce = random.randint(1, len(padre1) - 1)
    hijo1 = [padre1[0] + padre2[0]]
    hijo2 = [padre2[0] + padre1[0]]
    return hijo1, hijo2

# Función para aplicar mutación a un conejo
def mutar(conejo):
    
    if random.random() < tasa_mutacion:
        conejo[0] += random.randint(-1, 1)
    return conejo

# Función principal del algoritmo genético de conejos
def algoritmo_genetico_conejos():
    
    poblacion = inicializar_poblacion()

    for generacion in range(generaciones): #Se inicia un bucle que itera a través de cada generación
        poblacion = sorted(poblacion, key=evaluar_aptitud, reverse=True) # Se ordena la población en función de la aptitud de los conejos de mayor a menor. 

        nueva_poblacion = [] # Se crea una nueva lista vacía que contendrá la población de la siguiente generación.

        for _ in range(tamaño_poblacion // 2):
            padre1, padre2 = seleccionar_padres(poblacion)
            hijo1, hijo2 = cruzar(padre1, padre2)
            hijo1 = mutar(hijo1)
            hijo2 = mutar(hijo2)
            nueva_poblacion.extend([hijo1, hijo2])
            

        poblacion = nueva_poblacion
        

    mejor_conejo = max(poblacion, key=evaluar_aptitud)
    
    print("Mejor conejo:", mejor_conejo) # Se imprime en la consola el mejor conejo encontrado al final de todas las generaciones.
    

# Ejecutar el algoritmo genético de conejos
algoritmo_genetico_conejos()
