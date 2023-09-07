import numpy as np

# Usando exemplo do caderno na forma já padronizada: -min -3x1 -5x2 + 0x3 + 0x4 + 0x5

A = np.array([
    [3, 2, 2, 1, 0, 0],
    [1, 0, 2, 0, 1, 0],
    [0, 2, 1, 0, 0, 1],
])

b = np.array([
    [18],
    [4],
    [12],
])

variaveisX = np.array([-3, -5, -1, 0, 0, 0])


base = np.array([4, 5, 6])
naoBase = np.array([1, 2, 3])

# monta a matriz base
matrizBase = np.array(
    A[:, base - 1],
)

# monta a matriz não base
matrizNaoBase = np.array(
    A[:, naoBase - 1],
)

print(matrizBase)
print()
print(matrizNaoBase)

cbT = np.array(variaveisX[base - 1])
cnT = np.array(variaveisX[naoBase - 1])

# print(cbT)
# print(cnT)


# PASSO 1:
matrizBaseInvertida = np.linalg.inv(matrizBase)
xB = np.dot(matrizBaseInvertida, b)
# print(matrizBaseInvertida)
print(xB)

# PASSO 2 i:
lambaTrasposta = np.dot(cbT, matrizBaseInvertida)
print(cnT)


# PASSO 2 ii:
# for i in range(cnT):
#     cn = np.array([])

# cnChapeu = np.array([
# ])

# cnk = cnChapeu.min()
k = 2
an2 = np.array([2, 0, 2]).T

y = np.dot(matrizBaseInvertida, an2)
print(y)
