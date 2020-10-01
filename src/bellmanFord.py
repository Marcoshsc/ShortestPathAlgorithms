from typing import List, Tuple
from abs.genericAlgorithm import GenericAlgorithm, AlgorithmResult
from util import getPath, getCost
import time

class BellmanFordAlgorithm(GenericAlgorithm):

    def execute(self, graph: List[List[float]], source: int, target: int) -> AlgorithmResult:
        initTime = time.time()
        dist, pred = bellmanFordAlgorithm(graph, source)
        executionTime = time.time() - initTime
        path = getPath(pred, source, target)
        cost = dist[target]
        return AlgorithmResult(path, cost, executionTime)


class BellmanFordAlgorithmEfficient(GenericAlgorithm):

    def execute(self, graph: List[List[float]], source: int, target: int) -> AlgorithmResult:
        initTime = time.time()
        dist, pred = bellmanFordAlgorithmEficient(graph, source)
        executionTime = time.time() - initTime
        path = getPath(pred, source, target)
        cost = dist[target]
        return AlgorithmResult(path, cost, executionTime)


def bellmanFordAlgorithm(graph: List[List[float]], origin: int) -> Tuple[List[float], List[int]]:

    dist: List[float] = [float('inf') for v in graph]
    pred: List[int] = [None for v in graph]
    dist[origin] = 0

    edges: List[Tuple[int, int]] = []
    indexes = range(len(graph))
    for i in indexes:
        for j in indexes:
            if graph[i][j] != 0:
                edges.append((i, j))
    
    for _ in indexes:
        for edge in edges:
            u, v = edge
            if dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]
                pred[v] = u
    
    return (dist, pred)

def bellmanFordAlgorithmEficient(graph: List[List[float]], origin: int) -> Tuple[List[float], List[int]]:

    dist: List[float] = [float('inf') for v in graph]
    pred: List[int] = [None for v in graph]
    dist[origin] = 0

    edges: List[Tuple[int, int]] = []
    indexes = range(len(graph))
    for i in indexes:
        for j in indexes:
            if graph[i][j] != 0:
                edges.append((i, j))
    
    for _ in indexes:
        trocou = False
        for edge in edges:
            u, v = edge
            if dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]
                pred[v] = u
                trocou = True
        if not trocou:
            break
    
    return (dist, pred)