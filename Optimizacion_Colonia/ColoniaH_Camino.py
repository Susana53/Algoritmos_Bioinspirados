#optimizacion por colonia de hormigas

import numpy as np

class ColoniaHormigas:
    def __init__(self, n_ciudades, distancias, feromonas, alfa=1.0, beta=2.0, rho=0.5, q=100):
        self.n_ciudades = n_ciudades
        self.distancias = distancias
        self.feromonas = feromonas
        self.alfa = alfa
        self.beta = beta
        self.rho = rho
        self.q = q

    def encontrar_camino_optimo(self, n_iteraciones):
        mejor_camino = None
        mejor_distancia = float('inf')

        for _ in range(n_iteraciones):
            camino_hormiga = self.construir_camino_hormiga()
            distancia = self.calcular_distancia(camino_hormiga)

            if distancia < mejor_distancia:
                mejor_camino = camino_hormiga
                mejor_distancia = distancia

            self.actualizar_feromonas(camino_hormiga, distancia)
            self.evaporar_feromonas()

        return mejor_camino, mejor_distancia

    def construir_camino_hormiga(self):
        ciudad_actual = np.random.randint(self.n_ciudades)
        camino_hormiga = [ciudad_actual]

        while len(camino_hormiga) < self.n_ciudades:
            siguiente_ciudad = self.elegir_siguiente_ciudad(ciudad_actual, camino_hormiga)
            camino_hormiga.append(siguiente_ciudad)
            ciudad_actual = siguiente_ciudad

        return camino_hormiga

    def elegir_siguiente_ciudad(self, ciudad_actual, camino_hormiga):
        probabilidades = self.calcular_probabilidades(ciudad_actual, camino_hormiga)
        return np.random.choice(self.n_ciudades, 1, p=probabilidades)[0]

    def calcular_probabilidades(self, ciudad_actual, camino_hormiga):
        feromonas = np.copy(self.feromonas[ciudad_actual, :])
        feromonas[camino_hormiga] = 0
        exponente = self.alfa * np.log(1.0 / (self.distancias[ciudad_actual, :] + 1e-10)) + \
                    self.beta * np.log(feromonas + 1e-10)
        probabilidades = np.exp(exponente)
        probabilidades /= np.sum(probabilidades)
        return probabilidades

    def calcular_distancia(self, camino):
        distancia = 0
        for i in range(self.n_ciudades - 1):
            distancia += self.distancias[camino[i], camino[i + 1]]
        return distancia

    def actualizar_feromonas(self, camino_hormiga, distancia):
        feromona_depositada = self.q / distancia
        for i in range(self.n_ciudades - 1):
            self.feromonas[camino_hormiga[i], camino_hormiga[i + 1]] += feromona_depositada
            self.feromonas[camino_hormiga[i + 1], camino_hormiga[i]] += feromona_depositada

    def evaporar_feromonas(self):
        self.feromonas *= (1.0 - self.rho)

# Ejemplo de uso
if __name__ == "__main__":
    # Definir número de ciudades
    n_ciudades = 5

    # Inicializar distancias y feromonas
    distancias = np.array([[0, 2, 3, 1, 4],
                           [2, 0, 5, 2, 1],
                           [3, 5, 0, 6, 7],
                           [1, 2, 6, 0, 3],
                           [4, 1, 7, 3, 0]])

    feromonas = np.ones((n_ciudades, n_ciudades))

    # Configurar parámetros de la colonia de hormigas
    alfa = 1.0
    beta = 2.0
    rho = 0.5
    q = 100

    # Crear instancia de la colonia de hormigas
    colonia = ColoniaHormigas(n_ciudades, distancias, feromonas, alfa, beta, rho, q)

    # Encontrar el camino óptimo y la distancia mínima
    mejor_camino, mejor_distancia = colonia.encontrar_camino_optimo(n_iteraciones=100)

    # Mostrar resultados
    print("Mejor camino encontrado:", mejor_camino)
    print("Distancia mínima:", mejor_distancia)
