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

for i in range(matrizNaoBase.shape[1]):
    for j in range(matrizNaoBase.shape[0]):
        cnChapeu[i] += lambaTrasposta[j] * matrizNaoBase[j][i]

print(cnChapeu)

cnChapeuFinal = cnT - cnChapeu

cnk = cnChapeuFinal.min()

k = np.argmin(cnChapeuFinal)

colunateste = matrizNaoBase[:, k]

colunaK = np.all(colunateste >= 0)
print(colunaK)
print("teste")
