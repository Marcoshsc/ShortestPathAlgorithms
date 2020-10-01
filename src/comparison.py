from test import getExecutionTime
import json

data = []

with open('resources/dataToCompare.json', 'r') as dataFile:
    data = json.loads(dataFile.read())

print(f'Total de {len(data)} registros...')
results = {}

for d in data:
    vertexes = d['vertex']
    edges = d['edge']
    minimum = d['min']
    maximum = d['max']
    print(f'Rodando para {vertexes} vértices, {edges} arestas, {minimum} peso mínimo e {maximum} peso máximo...')
    times = getExecutionTime(d)
    key = (f'{vertexes}#{edges}#{minimum}#{maximum}')
    results[key] = {
        'Djikstra': times[0],
        'Bellman-Ford': times[1],
        'Bellman-Ford-Efficient': times[2],
        'Floyd-Warshall': times[3]
    }

with open('resources/results.json', 'w+') as resultsFile:
    json.dump(results, resultsFile)
