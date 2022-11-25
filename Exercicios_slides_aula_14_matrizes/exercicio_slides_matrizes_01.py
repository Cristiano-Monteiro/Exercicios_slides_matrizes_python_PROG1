"""
1) Subtração de 2 matrizes com dimensões n x n e Cálculo da transposta de uma matriz de 
   dimensão n x n.
"""

def calculo_subtracao_matrizes(matriz1, matriz2):
    if(len(matriz1) == len(matriz2)):
        resultado_subtracao = []
        for lin in range(len(matriz1)):
            matriz = []
            for col in range(len(matriz1)):
                subtracao = matriz1[lin][col] - matriz2[lin][col]
                matriz.append(subtracao)
            resultado_subtracao.append(matriz)
        return resultado_subtracao
    else:
        return 'ERRO! Não é possível subtrair matrizes de ordens diferentes!'

def calculo_matriz_transposta(matriz, dimensao):
    matriz_transposta_final = []
    for cont in range(dimensao):
        m_t = []
        for lin in range(dimensao):
            for col in range(dimensao):
                if(col == cont):
                    m_t.append(matriz[lin][col])
        matriz_transposta_final.append(m_t)
    return matriz_transposta_final

def preencher_matriz():
    dimensao = int(input('Dimensão da matriz n x n: '))
    matriz_principal = []
    for lin in range(dimensao):
        matriz = []
        for col in range(dimensao):
            print('[{}][{}]: '.format(lin, col), end='')
            valor = int(input())
            matriz.append(valor)
        matriz_principal.append(matriz)
    return matriz_principal

def mostrar_matriz(matriz):
    print()
    if(type(matriz) == list):
        for lin in range(len(matriz)):
            print('[ ', end='')
            for col in range(len(matriz)):
                print(matriz[lin][col], end=' ')
            print(']')
    else:
        print(matriz)

matriz1 = preencher_matriz()
matriz2 = preencher_matriz()

matriz_transposta = calculo_matriz_transposta(matriz1, len(matriz1))
subtracao_matrizes = calculo_subtracao_matrizes(matriz1, matriz2)

mostrar_matriz(matriz1)
mostrar_matriz(matriz2)
mostrar_matriz(matriz_transposta)
mostrar_matriz(subtracao_matrizes)