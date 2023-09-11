# # def ValoresDeXB()


# def Simplex(A, b, variaveisX, base, naoBase, iteracao=0):

#     iteracao += 1

#     while True:
#         print(f"------- Iteração {iteracao} ----------\n")

#         # monta a matriz base
#         matrizBase = np.array(
#             A[:, base - 1],
#         )

#         # monta a matriz não base
#         matrizNaoBase = np.array(
#             A[:, naoBase - 1],
#         )

#         print(f"Matriz Base (B):\n {matrizBase} \n")
#         print(f"Matriz Não Base (N):\n {matrizNaoBase} \n")

#         # cbT = np.array(variaveisX[base - 1])
#         # cnT = np.array(variaveisX[naoBase - 1])

#         cbT = np.array([variaveisX[i] for i in base-1])
#         cnT = np.array([variaveisX[i] for i in naoBase-1])

#         print(f"Variaveis x da Base: cbt = {cbT}")
#         print(f"Variaveis x da Não Base: cnt = {cnT} \n")

#         # print(cbT)
#         # print(cnT)

#         # PASSO 1:
#         print("PASSO 1: Calcular a Solução Básica")
#         matrizBaseInvertida = np.linalg.inv(matrizBase)
#         xB = np.dot(matrizBaseInvertida, b)
#         print(f"Inversa da Base (B-¹):\n {matrizBaseInvertida}\n")
#         print(f"xb = B-¹ * b:\n {xB}\n")
#         # print(matrizBaseInvertida)

#         # PASSO 2 i:
#         print("PASSO 2: Calcular os Custos Relativos")
#         lambaTransposta = np.dot(cbT, matrizBaseInvertida)
#         print(f"i)  = cbt * B-¹:\n {lambaTransposta}\n")

#         # PASSO 2 ii:
#         # inicializa um array do tamanho da matrizNaoBase e insere 0 em todos os elementos para depois podermos iterar no loop
#         # cnChapeu = lambdaTramposta * anj, j = 1,2;
#         print("ii)CnjChapeu = Cnj -  * anj, j = 1,2,...")
#         cnChapeu = np.zeros(matrizNaoBase.shape[1])

#         # o [1] representa o indice do "vetor" criado na matrizNaoBase.shape
#         for i in range(matrizNaoBase.shape[1]):
#             for j in range(matrizNaoBase.shape[0]):
#                 cnChapeu[i] += lambaTransposta[j] * matrizNaoBase[j][i]

#         cnChapeuFinal = cnT - cnChapeu
#         print(f"O custo relativo do X da Não Base são: {cnChapeuFinal}\n")

#         # Passo 2 III -> cnk é o menor valor e k é o indice desse valor (Lembrar que conta de 0 pra cima no vetor)
#         cnk = cnChapeuFinal.min()
#         k = np.argmin(cnChapeuFinal)
#         print(
#             f"iii) O menor valor (CNK) é {cnk} portanto, a coluna {k+1} entra na Base!\n")

#         # Passo 3 ->
#         # colunaK é a matriz/coluna referente a coluna que SAI da BASE
#         if cnk >= 0:
#             print("Passo 3: CNK é maior que 0. Solução Encontrada!!\n")
#             for i in range(len(base)):
#                 print("x", base[i] + 1, " = ", xB[i])
#             for i in range(len(naoBase)):
#                 print("x", naoBase[i] + 1, " = ", 0)
#             break

#         print("PASSO 3: CNK não é maior que 0, portanto continuamos o algoritmo\n")

#         colunaK = np.array(matrizNaoBase[:, k]).T

#         y = np.dot(matrizBaseInvertida, colunaK)
#         print(f"Passo 4: y = B-¹ * ank = {y}\n")
#         # ARRUMAR ISSO PARA O IF
#         menorZero = np.all(y <= 0)
#         # menorZero retorna true ou false se a colunaK for menor ou igual a zero

#         # O else
#         if menorZero:
#             return print("y é menor que 0 - Solução Infinita")
#         else:
#             # ARRUMAR AQUI DIVISAO ESTA DANDO ERRADO

#             valoresDivisao = []
#             for i in range(len(y)):
#                 # append adiciona o resultado na final da divisão
#                 valoresDivisao.append(xB[i]/y[i])
#             eChapeu = np.argmin(valoresDivisao)
#         print(
#             f"Passo 5: o indíce do menor valor valor de xB / y é {eChapeu}\n, portanto a coluna {eChapeu} sai da Base!")

#         colunaAux = matrizBase[:, eChapeu].copy()
#         matrizBase[:, eChapeu] = matrizNaoBase[:, k]
#         matrizNaoBase[:, k] = colunaAux

#         valorAux = base[eChapeu].copy()
#         base[eChapeu] = naoBase[k]
#         naoBase[k] = valorAux


# s = Simplex(A, b, variaveisX, base, naoBase, iteracao)
# print(s)
