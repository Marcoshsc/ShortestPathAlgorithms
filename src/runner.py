import json
from typing import List
from randomic import getRandomGraph
from abs.algorithmFactory import AlgorithmFactory

def getAndSaveGraph(saveGraph: bool, vertexes: int, edges: int, minWeight: float, maxWeight: float) -> List[List[float]]:
    graph = getRandomGraph(vertexes, edges, minWeight, maxWeight)
    if saveGraph:
        print('Salvando grafo...')
        with open('resources/generatedGraph.json', 'w+') as graphF:
            json.dump(graph, graphF)
    return graph


def runAlgorithms(generateGraph: bool, predef: bool, saveGraph: bool) -> None:

    print('Executando Shortest-Path CLI 1.0')
    data: dict
    if predef:
        with open('resources/predef.json', 'r') as dataF:
            data = json.loads(dataF.read())

    graph: List[List[float]]
    if generateGraph:
        if predef:
            print('Gerando grafo aleatório com configurações pré-definidas...')
            graph = getAndSaveGraph(saveGraph, data['vertexes'], data['edges'], data['minWeight'], data['maxWeight'])
        else:
            print('Você escolheu entrar com os dados do grafo a ser gerado via terminal. Entre com os dados a seguir:')
            vertexes = int(input('Digite a quantidade de vértics do grafo: '))
            edges = int(input('Digite a quantidade de arestas do grafo: '))
            minWeight = float(input('Digite o peso mínimo de uma aresta no grafo: '))
            maxWeight = float(input('Digite o peso máximo de uma aresta no grafo: '))
            answer = str(input('Deseja salvar o grafo gerado? S/N: '))
            willSave = answer.upper() == 'S'
            print('Gerando o grafo com a configuração inserida...')
            graph = getAndSaveGraph(willSave, vertexes, edges, minWeight, maxWeight)

    else:
        with open('resources/predefGraph.json', 'r') as graphFile:
            graph = json.loads(graphFile.read())
    
    source: int
    target: int
    algorithmName = str
    if predef:
        print('Você escolheu usar as configurações predefinidas em predef.json!')
        source = data['source']
        target = data['target']
        algorithmName = data['algorithm']
    else:
        print('Você escolheu ler os dados. Insira os dados a seguir...')
        source = int(input('Digite o vértice de origem: '))
        target = int(input('Digite o vértice de destino: '))
        print('\nVocê pode escolher entre quatro algoritmos: Dijkstra, Bellman-Ford, Bellman-Ford-Efficient, Floyd-Warshall.')
        algorithmName = str(input('Digite o nome do algoritmo a ser executado: '))
        
    print(f'Executando algoritmo {algorithmName.upper()}...')
    factory = AlgorithmFactory()
    algorithm = factory.getAlgorithm(algorithmName)

    result = algorithm.execute(graph, source, target)
    print(f'Menor caminho entre os vértices {source} e {target}: {result.path}')
    print(f'Custo: {result.cost}')
    print(f'Tempo de execução: {result.executionTime}')