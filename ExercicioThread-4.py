import platform
import subprocess
import multiprocessing

def os():
    system: str = ''
    system = platform.system()

    return system

def le_processo(id, operacao):
    vetor_processo: list = []
    linha: str = ''
    saida: str = ''
    
    vetor_processo = operacao.split(' ')
    linha = ''
    saida = subprocess.Popen(vetor_processo, stdout=subprocess.PIPE)
    linha = saida.stdout.readline().decode('utf-8', errors = 'ignore')
    print(vetor_processo)
    while (linha != ''):
        if (os() == 'Windows'):
            if ('Mdia' in linha):
                #print(linha)
                pingMedia = linha.split(', ')
                #print(pingMedia)
                for i in range(1):
                    if (id == 0):
                        print('Tempo médio do Terra: ', pingMedia[2])
                    elif (id == 1):
                        print('Tempo médio do UOL: ', pingMedia[2])
                    elif (id == 2):
                        print('Tempo médio do Google: ', pingMedia[2])
        elif (os() == 'Linux'):
            if ('avg' in linha):
                #print(linha)
                pingMedia = linha.split('/')
                #print(pingMedia)
                for i in range(1):
                    if (id == 0):
                        print('Tempo médio do Terra: ', pingMedia[4], 'ms')
                    elif (id == 1):
                        print('Tempo médio do UOL: ', pingMedia[4], 'ms')
                    elif (id == 2):
                        print('Tempo médio do Google: ', pingMedia[4], 'ms')
        else:
            print("Sistema Operacional inválida")
        linha = saida.stdout.readline().decode('utf-8', errors='ignore')
def main():
    i: int = 0
    processoTerra: str = ''
    processoUOL: str = ''
    processoGoogle: str = ''

    id: str = [0]*3
    for i in range (3):
        id[i] = i

    if (os() == "Windows"):
        print("Estou no Windows")

        processoTerra = 'ping -4 -n 10 www.terra.com.br'
        processoUOL = 'ping -4 -n 10 www.uol.com.br'
        processoGoogle = 'ping -4 -n 10 www.google.com.br'

        operacao: str = [processoTerra,processoUOL,processoGoogle]

        params: str = [('', '')]*3
        for j in range (3):
            params[j] = (id[j], operacao[j])
        
        with multiprocessing.Pool(processes=3) as pool:
            pool.starmap(le_processo, params)
    elif (os() == "Linux"):
        print("Estou no Linux")

        processoTerra = 'ping -4 -c 10 www.terra.com.br'
        processoUOL = 'ping -4 -c 10 www.uol.com.br'
        processoGoogle = 'ping -4 -c 10 www.google.com.br'
        
        operacao: str = [processoTerra,processoUOL,processoGoogle]

        params: str = [('', '')]*3
        for j in range (3):
            params[j] = (id[j], operacao[j])

        with multiprocessing.Pool(processes=3) as pool:
            pool.starmap(le_processo, params)

if __name__ == '__main__':
    main()