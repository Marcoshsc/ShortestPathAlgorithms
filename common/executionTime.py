from typing import Tuple
from algorithms.dijkstra.implementations import djikstraAlgorithm
from algorithms.bellmanFord.implementations import bellmanFordAlgorithm, bellmanFordAlgorithmEficient
from algorithms.floydWarshall.implementations import floydWarshallAlgorithm
from common.randomic import getRandomGraph
import time

def getExecutionTime(data: dict) -> Tuple[float, float, float, float]:

    randomGraph: List[List[float]] = getRandomGraph(data['vertex'], data['edge'], data['min'], data['max'])

    timePrev = time.time()
    djikstraAlgorithm(randomGraph, 0)
    dijkstraTime = time.time() - timePrev

    timePrev = time.time()
    bellmanFordAlgorithm(randomGraph, 0)
    bellmanFordTime = time.time() - timePrev

    timePrev = time.time()
    bellmanFordAlgorithmEficient(randomGraph, 0)
    bellmanFordEficientTime = time.time() - timePrev

    timePrev = time.time()
    floydWarshallAlgorithm(randomGraph)
    floydWarshallTime = time.time() - timePrev

    return (dijkstraTime, bellmanFordTime, bellmanFordEficientTime, floydWarshallTime)