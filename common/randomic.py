from typing import List, Tuple
import random

def getRandomGraph(vertexes: int, edges: int, minimumWeight: float, maximumWeight: float) -> List[List[float]]:

    if edges > vertexes ** 2:
        raise Exception('Número de arestas maior do que o possível a ser feito com o número de vértices fornecido.')
    
    matrix: List[List[float]] = [[0 for j in range(vertexes)] for i in range(vertexes)]

    edgeNumber = 0
    while edgeNumber < edges:
        i = random.randint(0, vertexes - 1)
        j = random.randint(0, vertexes - 1)
        if i == j or matrix[i][j] != 0:
            continue
        weight = random.uniform(minimumWeight, maximumWeight)
        matrix[i][j] = weight
        matrix[j][i] = weight
        edgeNumber += 2
    
    return matrix