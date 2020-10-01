from typing import List
from abs.genericAlgorithm import GenericAlgorithm, AlgorithmResult
from algorithms.bellmanFord.implementations import bellmanFordAlgorithm, bellmanFordAlgorithmEficient
from common.util import getPath
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