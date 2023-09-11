import numpy as np

# # Usando exemplo do caderno na forma já padronizada: -min -3x1 -5x2 + 0x3 + 0x4 + 0x5
# # x1 + x2 >= 5
# # x1 + x2 >= 5
# # x1 + x2 >= 5
# # x1 + x2 >= 5

# A = np.array([  # -----------------OK
#     [3, 2, 1, 0, 0],
#     [1, 0, 0, 1, 0],
#     [0, 2, 0, 0, 1],
# ])

# b = np.array([
#     [18],
#     [4],
#     [12],
# ])

# variaveisX = np.array([-3, -5, 0, 0, 0])

# # A = np.array([ ------------------------OK
# #     [1, 2, 3, 1, 0],
# #     [3, 2, 2, 0, 1],
# # ])

# # b = np.array([
# #     [9],
# #     [15],
# # ])

# # variaveisX = np.array([-1, -9, 1, 0, 0])

# # A = np.array([  # ----------------------------OK
# #     [1, 2, 4, -1, 1, 0, 0],
# #     [2, 3, -1, 1, 0, 1, 0],
# #     [1, 0, 1, 1, 0, 0, 1]
# # ])

# # b = np.array([
# #     [6],
# #     [12],
# #     [4],
# # ])

# # variaveisX = np.array([-2, -1, 3, -5, 0, 0, 0])


# base = np.array([3, 4, 5])
# naoBase = np.array([1, 2])
# iteracao = 0


# ---------TESTES DE EXERCICIOS----------

# Exemplo 2: TESTE = Erro pelo xb / y ser negativo

# A = np.array([
#     [1, 1, 1, 0, 0],
#     [1, -1, 0, 1, 0],
#     [-1, 1, 0, 0, 1],
# ])

# b = np.array([
#     [6],
#     [4],
#     [4],
# ])

# variaveisX = np.array([-1, -2, 0, 0, 0])


# LISTA 2: Exercicio a)
"""
# A = np.array([  # ----------------------------OK
#     [1, 2, 4, -1, 1, 0, 0],
#     [2, 3, -1, 1, 0, 1, 0],
#     [1, 0, 1, 1, 0, 0, 1]
# ])

# b = np.array([
#     [6],
#     [12],
#     [4],
# ])

# variaveisX = np.array([-2, -1, 3, -5, 0, 0, 0])
"""

# Trabalho 2: Exercicio e)
A = np.array([
    [1, 2, 3, 1, 0],
    [3, 2, 2, 0, 1],
])

b = np.array([
    [9],
    [15],
])

variaveisX = np.array([-1, -9, -1, 0, 0])


base = np.array([4, 5])
naoBase = np.array([1, 2, 3])
iteracao = 0


def Simplex(A, b, variaveisX, base, naoBase, iteracao):

    while True:
        iteracao += 1
        print(f"------- Iteracao: {iteracao} ----------\n")

        if (iteracao >= 2):
            print("Atualizacao:")

        # monta a matriz base
        matrizBase = np.array(
            A[:, base - 1],
        )

        # monta a matriz não base
        matrizNaoBase = np.array(
            A[:, naoBase - 1],
        )

        print(f"Matriz Base (B):\n {matrizBase} \n")
        print(f"Matriz Nao Base (N):\n {matrizNaoBase} \n")

        cbT = np.array([variaveisX[i] for i in base-1])
        cnT = np.array([variaveisX[i] for i in naoBase-1])

        print(f"Variaveis x da Base: cbt = {cbT}")
        print(f"Variaveis x da Nao Base: cnt = {cnT} \n")

        # PASSO 1:--------------------------------------------------------
        print("PASSO 1: Calcular a Solucao Basica")
        matrizBaseInvertida = np.linalg.inv(matrizBase)
        xB = np.dot(matrizBaseInvertida, b)
        print(f"Inversa da Base (B-¹):\n {matrizBaseInvertida}\n")
        print(f"xb = B-¹ * b:\n {xB}\n")

        # PASSO 2 i:------------------------------------------------------
        print("PASSO 2: Calcular os Custos Relativos")
        lambdaTransposta = np.dot(cbT, matrizBaseInvertida)
        print(f"i) lambdaT = cbt * B-¹:\n {lambdaTransposta}\n")

        # PASSO 2 ii:-----------------------------------------------------
        # inicializa um array do tamanho da matrizNaoBase e insere 0 em todos os elementos para depois podermos iterar no loop
        # cnChapeu = lambdaTramposta * anj, j = 1,2;
        print("ii)CnjChapeu = Cnj - lambdaT * anj, j = 1,2,...")
        cnChapeu = np.zeros(matrizNaoBase.shape[1])

        # o [1] representa o indice do "vetor" criado na matrizNaoBase.shape
        for i in range(matrizNaoBase.shape[1]):
            for j in range(matrizNaoBase.shape[0]):
                cnChapeu[i] += lambdaTransposta[j] * matrizNaoBase[j][i]

        cnChapeuFinal = cnT - cnChapeu
        print(f"O custo relativo do X da Nao Base sao: {cnChapeuFinal}\n")

        # PASSO 2 iii:----------------------------------------------------
        # cnk é o menor valor e k é o indice desse valor (Lembrar que conta de 0 pra cima no vetor)
        cnk = cnChapeuFinal.min()
        k = np.argmin(cnChapeuFinal)
        print(f"iii) O menor valor (CNK) = {cnk}")
        # k+1 pois o vetor inicia do 0 e os valores de CNK são 1,2...
        print(f"K={k+1} Portanto, a coluna N{k+1} entra na Base!\n")

        # PASSO 3:--------------------------------------------------------
        # colunaK é a matriz/coluna referente a coluna que entra na BASE
        print("PASSO 3: Teste de Otimalidade")
        print(f"CNK >= 0 ?  ---> {cnk} >= 0 ?\n")
        if cnk >= 0:
            print("CNK eh maior ou igual que 0. Solução Encontrada!!\n")
            resultado = 0
            for i in range(len(base)):
                print("x", base[i], " = ", xB[i])
                if i < len(variaveisX):
                    resultado += xB[i] * variaveisX[i]
            for i in range(len(naoBase)):
                print("x", naoBase[i], " = ", 0)
            # for j in range(len(base)):
            #     if j < len(variaveisX):
            #         resultado += xB[j] * variaveisX[j]
            z = variaveisX[-1] + np.dot(variaveisX[base-1], xB)

            return z
        print("CNK não eh maior ou igual que 0, portanto continuamos o algoritmo!\n")
        colunaK = np.array(matrizNaoBase[:, k]).T

        # PASSO 4:--------------------------------------------------------
        print("PASSO 4: Calculo da Direcao Simplex")
        y = np.dot(matrizBaseInvertida, colunaK)
        print(f"y = B-¹ * ank:\n y = {y}\n")
        # OBS: Mesmo que colunak seja uma matriz coluna, a impressão é em linha!

        # PASSO 5:--------------------------------------------------------
        print("Passo 5: Determinacao do passo e variavel a sair da Base")
        print(f"y <= 0 ? ---> {y} <= 0 ?")
        # menorZero retorna true ou false se todos os valores de y for menor ou igual a zero
        menorZero = np.all(y <= 0)
        if menorZero:
            return print("Sim, y eh menor ou igual a 0 - Solução Infinita!")
        else:
            print("Não, continua!\n")
            valoresDivisao = []
            for i in range(len(y)):  # append adiciona o resultado na final da divisão
                resultadoDivisao = xB[i]/y[i]
                if np.isinf(resultadoDivisao) or resultadoDivisao < 0:
                    valoresDivisao.append(None)
                else:
                    valoresDivisao.append(resultadoDivisao)

            menorValor = float('inf')
            ind = None

            for i, elemento in enumerate(valoresDivisao):
                if elemento is not None:
                    valorElemento = elemento[0]
                    if valorElemento < menorValor:
                        menorValor = valorElemento
                        ind = i
            # ind = np.argmin(valoresDivisao)
            print(f"Echapeu = MIN {valoresDivisao}\n")

        print(f"O indíce do minimo de Echapeu: i = {ind+1}")
        print(f"Portanto a coluna B{ind+1} sai da Base!\n")

        colunaAux = matrizBase[:, ind].copy()
        matrizBase[:, ind] = matrizNaoBase[:, k]
        matrizNaoBase[:, k] = colunaAux

        valorAux = base[ind].copy()
        base[ind] = naoBase[k]
        naoBase[k] = valorAux


solucao = Simplex(A, b, variaveisX, base, naoBase, iteracao)
print(f"\nA solucao para o problema apresentado e: {solucao}")
