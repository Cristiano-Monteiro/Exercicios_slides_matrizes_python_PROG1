"""
2) Escreva um programa que leia todas as posições de uma matriz 10x10. O programa deve então exibir
   o número de posições não nulas na matriz.
"""

def posicoes_nao_nulas(matriz):
    posicoes_nao_nulas = 0
    for lin in matriz:
        for col in lin:
            if(col != 0):
                posicoes_nao_nulas+=1
    return posicoes_nao_nulas

# Função para o usuário escolher os valores de cada posição na matriz:
def preencher_matriz():
    matriz_usuario = []
    for lin in range(10):
        matriz_secundaria = []
        for col in range(10):
            print('[{}][{}]: '.format(lin, col), end='')
            valor = int(input())
            matriz_secundaria.append(valor)
        matriz_usuario.append(matriz_secundaria)
    resultado = posicoes_nao_nulas(matriz_usuario)
    print('Quantidade de posições não nulas na matriz: ', resultado)

# Descomentar "preencher_matriz()" para ver o seu funcionamento:
"""
preencher_matriz()
"""

# Testes para ver o funcionamento da função "posicoes_nao_nulas" com matrizes exemplos:

matriz_10x10 = [
    [0,1,1,1,0,0,1,1,0,1],
    [1,0,0,0,1,1,0,0,1,0],
    [1,0,0,1,1,1,0,1,0,1],
    [1,0,1,0,0,1,1,1,0,0],
    [0,2,0,2,0,0,0,0,1,1],
    [0,1,1,1,0,0,1,0,1,1],
    [0,0,1,1,0,1,0,1,0,1],
    [1,1,0,0,0,0,1,1,0,0],
    [0,1,0,0,1,0,1,0,0,0],
    [1,0,0,1,0,0,0,1,1,1]
]

matriz1_3x3 = [
    [0,1,0],
    [1,0,0],
    [0,1,0]
]

matriz2_3x3 = [
    [0,1,0],
    [0,0,0],
    [0,0,1]
]

resultado = posicoes_nao_nulas(matriz1_3x3)
print('Matriz-1 3x3: ', resultado)

resultado = posicoes_nao_nulas(matriz2_3x3)
print('Matriz-2 3x3: ', resultado)

resultado = posicoes_nao_nulas(matriz_10x10)
print('Matriz 10x10: ', resultado)