from typing import List

def getPath(pred: List[int], source: int, target: int) -> List[int]:
    path: List[int] = [target]
    cost: float = 0
    aux = target
    while aux != source:
        aux = pred[aux]
        path.insert(0, aux)
    return path