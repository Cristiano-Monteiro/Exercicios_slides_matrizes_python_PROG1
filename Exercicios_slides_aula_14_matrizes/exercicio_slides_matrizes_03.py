"""
3) Um treino para a Corrida do Círio foi definido no parque Porto Futuro em Belém. A ideia era 
   permitir 10 voltas para cada um de 6 corredores. Faça um programa que leia os nomes e os tempos 
   (em segundos) de cada volta de cada corredor e guarde as informações em uma matriz. Ao final, o 
   programa deve informar:
    - De quem foi a melhor volta da prova, e em que volta.
    - Classificação final em ordem crescente.
    - Qual foi a volta com a média mais rápida.
"""

def preencher_matriz():
    for lin in range(6):
        matriz = []
        atleta = str(input('Nome do atleta: '))
        nome_corredores.append(atleta)
        for col in range(10):
            print('Tempo na {}ª Volta: '.format(col+1))
            tempo = float(input(''))
            matriz.append(tempo)
        tempo_corredores.append(matriz)

def melhor_volta_da_prova(tempos, nomes):
    melhor_volta_tempo = 50
    melhor_volta_atleta = ''
    melhor_volta_pos = 0
    for i, atleta in enumerate(tempos):
        for j, tempo in enumerate(atleta):
            if(tempo <= melhor_volta_tempo):
                melhor_volta_tempo = tempo
                melhor_volta_atleta = nomes[i]
                melhor_volta_pos = j
    print('Melhor volta da prova(atleta, tempo, volta): ', end='')
    print(melhor_volta_atleta, melhor_volta_tempo, melhor_volta_pos+1)

def calculo_media(matriz):
    lista_media = []
    for item in matriz:
        media = sum(item) / len(item)
        lista_media.append(media)
    return lista_media

def classificacao_final(medias, nomes):
    classificacao = []
    for cont in range(len(medias)):
        temp = {'Atleta': nomes[cont], 'Média': medias[cont]}
        classificacao.append(temp)

    def chave_media(m):
        return m['Média']

    classificacao.sort(key=chave_media)
    print()
    print('Classificação final em ordem crescente:')
    for i, posicao in enumerate(classificacao):
        print('{}) {} {:.1f}'.format(i+1, posicao['Atleta'], posicao['Média']))

def calculo_matriz_transposta(matriz):
    matriz_transp = []
    for cont in range(10):
        m = []
        for mat in matriz:
            m.append(mat[cont])
        matriz_transp.append(m)
    return matriz_transp

def volta_media_mais_rapida(media_volta):
    posicao_volta = 0
    media_mais_rapida = 0
    for volta, media in enumerate(media_volta):     
        if(media >= media_mais_rapida):
            media_mais_rapida = media
            posicao_volta = volta+1
    print()
    print('Volta com a média mais rápida(posição, média): ', end='')
    print('{} {:.1f}'.format(posicao_volta, media_mais_rapida))

# Matrizes preenchidas com dados totalmente fictícios:

tempo_corredores = [
    [2,2,2,2,2,2,2,2,2,2],
    [5,2,3,4,5,6,7,8,9,10],
    [3,3,3,3,3,3,3,3,3,3],
    [2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5],
    [4,4,4,4,4,4,4,4,4,4],
    [1.2,1.11,1.22,1.9,2,6,2.4,1.8,1.55,1.15]
]

nome_corredores = [
    'atleta1',
    'atleta2',
    'atleta3',
    'atleta4',
    'atleta5',
    'atleta6'
]

# Descomentar para preencher as matrizes com novos valores:
""" 
tempo_corredores = []
nome_corredores = []

preencher_matriz()
"""

melhor_volta_da_prova(tempo_corredores, nome_corredores)
media_tempos = calculo_media(tempo_corredores)
classificacao_final(media_tempos, nome_corredores)
transposta = calculo_matriz_transposta(tempo_corredores)
media_volta = calculo_media(transposta)
volta_media_mais_rapida(media_volta)