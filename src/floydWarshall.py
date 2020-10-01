from typing import List, Tuple
import time
from util import getPathFromMatrix, getCost
from abs.genericAlgorithm import GenericAlgorithm, AlgorithmResult

class FloydWarshallAlgorithm(GenericAlgorithm):

    def execute(self, graph: List[List[float]], source: int, target: int) -> AlgorithmResult:
        initTime = time.time()
        dist, pred = floydWarshallAlgorithm(graph)
        executionTime = time.time() - initTime
        path = getPathFromMatrix(pred, source, target)
        cost = getCost(dist, path)
        return AlgorithmResult(path, cost, executionTime)


def floydWarshallAlgorithm(graph: List[List[float]]) -> Tuple[List[List[float]], List[List[int]]]:
    dist: List[List[float]] = [[float('inf') for w in graph] for n in graph]
    pred: List[List[int]] = [[None for w in graph] for n in graph]
    indexes = range(len(graph))
    for i in indexes:
        for j in indexes:
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]
                pred[i][j] = i
            else:
                dist[i][j] = float('inf')
                pred[i][j] = None
    
    for k in indexes:
        for i in indexes:
            for j in indexes:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]
    
    return (dist, pred)
            