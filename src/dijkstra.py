from typing import List, Tuple
from queue import PriorityQueue

def djikstraAlgorithm(graph: List[List[float]], origin: int) -> Tuple[List[float], List[int]]:

    dist: List[float] = [float('inf') for v in graph]
    pred: List[int] = [None for v in graph]

    dist[origin] = 0
    Q: PriorityQueue = PriorityQueue()
    Q.put((0, origin))

    elements = 1
    while elements != 0:
        
        element: Tuple[int, float] = Q.get()
        elements -= 1
        distance: float = element[0]
        current: int = element[1]
        if distance > dist[current]:
            continue

        adjacents: List[Tuple[int, float]] = [(c, n) for c, n in enumerate(graph[current]) if n != 0]
        for vertex, weight in adjacents:
            if dist[vertex] > dist[current] + weight:
                dist[vertex] = dist[current] + weight
                pred[vertex] = current
                Q.put((weight, vertex))
                elements += 1
    
    return (dist, pred)