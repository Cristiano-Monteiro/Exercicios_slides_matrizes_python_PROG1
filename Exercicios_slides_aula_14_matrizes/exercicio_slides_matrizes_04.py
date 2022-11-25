"""
4) Faça um programa para o Jogo da Velha. Seu programa deve ler uma matriz 3x3 que representa um 
   tabuleiro de jogo da velha.
"""

def resultado_jogo(matriz, i = 0):
    if(i == 0):
        vitoria_na_linha(matriz)
    elif(i == 1):
        vitoria_na_coluna(matriz)
    elif(i == 2):
        vitoria_na_diagonal(matriz)
    else:
        print('HOUVE EMPATE')

def vitoria_na_linha(matriz, i=1):
    vitoria = False
    for r in matriz:
        if(r[0] == r[1] and r[0] == r[2]):
            vitoria = r[0]
    if(vitoria != False):
        print('VITÓRIA DO JOGADOR {}'.format(vitoria))
    else:
        resultado_jogo(matriz, i)

def matriz_transposta(matriz):
    m1 = [[],[],[]]
    for cont in range(3):
        for lin in range(3):
            for col in range(3):
                if(col == cont):
                    m1[cont].append(matriz[lin][col])
    return m1

def vitoria_na_coluna(matriz):
    matriz_t = matriz_transposta(matriz)
    vitoria_na_linha(matriz_t, 2)

def vitoria_na_diagonal(matriz):
    vitoria = False
    if(matriz[0][0] == matriz[1][1] == matriz[2][2]):
        vitoria = matriz[0][0]
    elif(matriz[0][2] == matriz[1][1] == matriz[2][0]):
        vitoria = matriz[0][2]

    if(vitoria != False):
        print('VITÓRIA DO JOGADOR {}'.format(vitoria))
    else:
        resultado_jogo(matriz, 3)

matriz_teste_linha = [
    ['X','X','O'],
    ['O','O','X'],
    ['X','X','X']
]

matriz_teste_coluna = [
    ['X','O','X'],
    ['O','O','X'],
    ['X','O','O']
]

matriz_teste_diagonal = [
    ['O','X','X'],
    ['O','X','X'],
    ['X','O','O']
]

matriz_teste_empate = [
    ['X','X','O'],
    ['O','O','X'],
    ['X','O','X']
]

print('matriz_teste_linha: ', end='')
resultado_jogo(matriz_teste_linha)
print('matriz_teste_coluna: ', end='')
resultado_jogo(matriz_teste_coluna)
print('matriz_teste_diagonal: ', end='')
resultado_jogo(matriz_teste_diagonal)
print('matriz_teste_empate: ', end='')
resultado_jogo(matriz_teste_empate)