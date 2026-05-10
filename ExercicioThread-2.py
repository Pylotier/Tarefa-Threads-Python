import random
import multiprocessing
import time

def main():
    id: int = 0

    param: int = [0]*3

    for id in range (3):
        param[id] = id

    with multiprocessing.Pool(processes=3) as pool:
        pool.map(operacao, param)

def operacao(param):
    j: int = 0
    soma: int = 0

    valor: int = [0]*5

    n1: int = 0
    # n2: int = 0
    # n3: int = 0
    # n4: int = 0
    # n5: int = 0
    # n2 = random.randint(1, 100)
    # n3 = random.randint(1, 100)
    # n4 = random.randint(1, 100)
    # n5 = random.randint(1, 100)

    for j in range (5):
        n1 = random.randint(1, 100)
        valor[j] = n1
        time.sleep(0.2)
        soma += valor[j]
        print("Resultado do Thread", param, ':', soma)
    


if __name__ == '__main__':
    main()