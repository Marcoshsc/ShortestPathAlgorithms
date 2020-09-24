from typing import List

def getPath(pred: List[int], source: int, target: int) -> List[int]:
    path: List[int] = [target]
    cost: float = 0
    aux = target
    while aux != source:
        aux = pred[aux]
        path.insert(0, aux)
    return pathdef getPathFromMatrix(pred: List[List[int]], source: int, target: int):
    path: List[int] = [target]
    aux = target
    while aux != source:
        aux = pred[source][aux]
        path.insert(0, aux)
    return path

def getCost(dist: List[List[float]], path: List[int]):
    cost = 0
    for n in range(len(path) - 1):
        cost += dist[path[n]][path[n + 1]]
    return cost