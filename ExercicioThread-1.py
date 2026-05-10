import multiprocessing
import time

def main():
    i: int = 0
    param: int = [0]*5


    for i in range(5):
        param[i] = i # Id do thread

    with multiprocessing.Pool(processes=5) as pool:
        pool.map(operacao, param)

def operacao(param):
    j: int = 0

    for j in range (5):
        print("Thread #", param)
        time.sleep(0.5)

if __name__ == '__main__':
    main()