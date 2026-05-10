import multiprocessing
import random

def main():
    i: int = 0
    num_threads: int = 0
    num_threads = 5
    param: int = [0]*5

    for i in range (5):
        param[i] = i
    
    with multiprocessing.Pool(processes=num_threads) as pool:
        pool.map(operacao, param)

def operacao(param):
    distanciaPercorrida: int = 0
    distanciaTotal: int = 45

    while (distanciaPercorrida <= distanciaTotal):
        distanciaPercorrida += random.randint(0, 5)
        print('Sapo', param, 'percorreu', distanciaPercorrida, 'cm')

    if (distanciaPercorrida >= distanciaTotal):
        print('Sapo', param, 'Terminou a corrida')
        
if __name__ == '__main__':
    main()