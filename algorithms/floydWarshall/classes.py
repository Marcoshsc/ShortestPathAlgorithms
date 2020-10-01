from typing import List
from algorithms.floydWarshall.implementations import floydWarshallAlgorithm
from abs.genericAlgorithm import GenericAlgorithm, AlgorithmResult
from common.util import getPathFromMatrix, getCost
import time


class FloydWarshallAlgorithm(GenericAlgorithm):

    def execute(self, graph: List[List[float]], source: int, target: int) -> AlgorithmResult:
        initTime = time.time()
        dist, pred = floydWarshallAlgorithm(graph)
        executionTime = time.time() - initTime
        path = getPathFromMatrix(pred, source, target)
        cost = getCost(dist, path)
        return AlgorithmResult(path, cost, executionTime)