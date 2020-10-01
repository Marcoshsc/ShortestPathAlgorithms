from typing import List, Tuple


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