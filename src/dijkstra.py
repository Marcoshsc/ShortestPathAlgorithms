from typing import List
from queue import PriorityQueue

def djikstraAlgorithm(graph: List[List[float]], origin: int):

    dist: List[float] = [float('inf') for v in graph]
    pred: List[int] = [None for v in graph]

    dist[origin] = 0
    Q: PriorityQueue = PriorityQueue(len(graph))
    Q.put((0, origin))

    while Q.qsize() > 0:
        
        distance, current = Q.get()
        if distance > dist[current]:
            continue

        adjacents = [(c, n) for c, n in enumerate(graph[current]) if n != 0]
        for vertex, weight in adjacents:
            if dist[vertex] > dist[current] + weight:
                dist[vertex] = dist[current] + weight
                pred[vertex] = current
                Q.put((weight, vertex))
    
    return dist, pred