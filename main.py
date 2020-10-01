import argparse
from run.runner import runAlgorithms

parser = argparse.ArgumentParser()

parser.add_argument('-p', '--predef',  action='store_true', help='Utilizar configurações pré-definidas na pasta resources')
parser.add_argument('-s', '--save', action='store_true', help='Salvar o grafo gerado')
parser.add_argument('-ng', '--nogenerate', action='store_true', help='Utilizar grafo provido pelo usuário')

args = parser.parse_args()

runAlgorithms(not args.nogenerate, args.predef, args.save)
