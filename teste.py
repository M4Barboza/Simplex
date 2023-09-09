import numpy as np

# Usando exemplo do caderno na forma já padronizada: -min -3x1 -5x2 + 0x3 + 0x4 + 0x5

A = np.array([
    [3, 2, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [0, 2, 0, 0, 1],
])

b = np.array([
    [18],
    [4],
    [12],
])

variaveisX = np.array([-3, -5, 0, 0, 0])


base = np.array([3, 4, 5])
naoBase = np.array([1, 2])


def Simplex(A, b, variaveisX, base, naoBase):
    # monta a matriz base
    matrizBase = np.array(
        A[:, base - 1],
    )

    # monta a matriz não base
    matrizNaoBase = np.array(
        A[:, naoBase - 1],
    )

    cbT = np.array(variaveisX[base - 1])
    cnT = np.array(variaveisX[naoBase - 1])

    # print(cbT)
    # print(cnT)

    # PASSO 1:
    matrizBaseInvertida = np.linalg.inv(matrizBase)
    xB = np.dot(matrizBaseInvertida, b)
    # print(matrizBaseInvertida)

    # PASSO 2 i:
    lambaTrasposta = np.dot(cbT, matrizBaseInvertida)

    # PASSO 2 ii:
    # inicializa um array do tamanho da matrizNaoBase e insere 0 em todos os elementos para depois podermos iterar no loop
    # cnChapeu = lambdaTramposta * anj, j = 1,2;
    cnChapeu = np.zeros(matrizNaoBase.shape[1])

    # o [1] representa o indice do "vetor" criado na matrizNaoBase.shape
    for i in range(matrizNaoBase.shape[1]):
        for j in range(matrizNaoBase.shape[0]):
            cnChapeu[i] += lambaTrasposta[j] * matrizNaoBase[j][i]

    cnChapeuFinal = cnT - cnChapeu

    # Passo 2 III -> cnk é o menor valor e k é o indice desse valor (Lembrar que conta de 0 pra cima no vetor)
    cnk = cnChapeuFinal.min()
    k = np.argmin(cnChapeuFinal)

    # Passo 3 ->
    # colunaK é a matriz/coluna referente a coluna que SAI da BASE
    colunaK = np.array(matrizNaoBase[:, k]).T

    # y retorna true ou false se a colunaK for menor ou igual a zero
    # ARRUMAR ISSO PARA O IF
    y = np.all(colunaK <= 0)

    # O else
    if y != 0:
        print("Achou")
    else:
        # ARRUMAR AQUI DIVISAO ESTA DANDO ERRADO
        valoresDivisao = (xB / colunaK)
        eChapeu = np.argmin(valoresDivisao)

    colunaAux = matrizBase[:, eChapeu-1].copy()
    matrizBase[:, eChapeu-1] = matrizNaoBase[:, k]
    matrizNaoBase[:, k] = colunaAux

    valorAux = base[eChapeu-1].copy()
    base[eChapeu-1] = naoBase[k]
    naoBase[k] = valorAux

    Simplex(A, b, variaveisX, base, naoBase)


Simplex(A, b, variaveisX, base, naoBase)
