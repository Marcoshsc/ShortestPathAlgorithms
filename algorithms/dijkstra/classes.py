from typing import List
from algorithms.dijkstra.implementations import djikstraAlgorithm
from common.util import getPath
from abs.genericAlgorithm import AlgorithmResult, GenericAlgorithm
import time

class DijkstraAlgorithm(GenericAlgorithm):

    def execute(self, graph: List[List[float]], source: int, target: int) -> AlgorithmResult:
        initTime = time.time()
        dist, pred = djikstraAlgorithm(graph, source)
        executionTime = time.time() - initTime
        path = getPath(pred, source, target)
        cost = dist[target]
        return AlgorithmResult(path, cost, executionTime)
        