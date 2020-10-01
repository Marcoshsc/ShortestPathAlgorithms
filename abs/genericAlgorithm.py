from typing import List

class AlgorithmResult:

    def __init__(self, path: List[int], cost: float, executionTime: float):
        self.path = path
        self.cost = cost
        self.executionTime = executionTime


class GenericAlgorithm:

    def execute(self, graph: List[List[float]], source: int, target: int) -> AlgorithmResult:
        pass
    