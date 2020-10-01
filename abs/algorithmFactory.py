from abs.genericAlgorithm import GenericAlgorithm
from algorithms.dijkstra.classes import DijkstraAlgorithm
from algorithms.bellmanFord.classes import BellmanFordAlgorithm, BellmanFordAlgorithmEfficient
from algorithms.floydWarshall.classes import FloydWarshallAlgorithm

class AlgorithmFactory:

    def getAlgorithm(self, name: str) -> GenericAlgorithm:
        upperName = name.upper()
        if upperName == 'DIJKSTRA':
            return DijkstraAlgorithm()
        elif upperName == 'BELLMAN-FORD':
            return BellmanFordAlgorithm()
        elif upperName == 'BELLMAN-FORD-EFFICIENT':
            return BellmanFordAlgorithmEfficient()
        elif upperName == 'FLOYD-WARSHALL':
            return FloydWarshallAlgorithm()
        else:
            raise Exception('Invalid algorithm.')