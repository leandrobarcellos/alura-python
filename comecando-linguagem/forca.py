from random import randint, randrange
from re import sub
from shlex import join


def obter_palavras_arquivo():
    palavras = []
    with open('palavras.txt') as arq_palavras:
        for linha in arq_palavras.readlines():
            palavras.append(linha.strip())
    return palavras


def montar_array_palavras():
    return [
        'banana',
        'açougue',
        'matusalem',
        'biblia',
        'ortopedico',
        'cadeira',
        'mesario',
        'orcamentario',
        'planta',
        'tecnologia',
        'piscina',
        'casarao',
        'janela',
        'elefante',
        'telhado',
        'computador',
        'diamante',
    ]


def encontrar_indices(caracter, palavra):
    indices = []
    indice = 0
    for letra in palavra:
        if caracter == letra:
            indices.append(indice)
        indice += 1
    return indices


def inicializar_letras_apontadas(palavra):
    return ["_" for _ in palavra]


def inicializar_letras_apontadas_tradicional(palavra):
    letras = []
    i = 0
    tamanho = len(palavra)
    while i < tamanho:
        letras.append('_')
        i += 1
    return letras


def even_numbers_with_list_comprehension():
    inteiros = [1, 3, 4, 5, 7, 8, 9]
    pares = [n for n in inteiros if n % 2 == 0]
    print('Pares: {}'.format(pares))


def exibir_banner():
    print('***************************')
    print('Bem vindo ao jogo da Forca!')
    print('***************************')


def obter_palavra_secreta():
    palavras = obter_palavras_arquivo()
    indice_palavra_secreta = randrange(0, len(palavras))
    return palavras[indice_palavra_secreta-1].strip().lower()


def apontar_letra(apontadas, corretamente_apontadas):
    chute = ''
    while chute == '' or chute in apontadas:
        chute = input('Qual letra? ').strip().lower()
        if chute in apontadas:
            print('A letra {} já foi apontada'.format(chute))
    return chute


def exibir_arquivo(nome):
    with open(nome) as arquivo:
        for linha in arquivo.readlines():
            print(linha[0:len(linha) - 2])


def exibir_ganhou():
    exibir_arquivo('ganhou.txt')


def exibir_perdeu():
    exibir_arquivo('perdeu.txt')


def inicializar_jogo():
    exibir_banner()
    palavra_secreta = obter_palavra_secreta()
    corretamente_apontadas = inicializar_letras_apontadas(palavra_secreta)
    enforcou = False
    acertou = False
    max_chutes = 6
    apontamentos_errados = 0
    apontadas = []
    while not enforcou and not acertou:
        chute = apontar_letra(apontadas, corretamente_apontadas)
        apontadas.append(chute)
        indices = encontrar_indices(chute, palavra_secreta)
        for i in indices:
            corretamente_apontadas[i] = chute
        if len(indices) == 0:
            apontamentos_errados += 1
            print('Você tem {} tentativas restantes!'.format(max_chutes))
        enforcou = max_chutes == apontamentos_errados
        acertou = '_' not in corretamente_apontadas
        desenha_forca(apontamentos_errados, corretamente_apontadas)
    if enforcou:
        print('Você perdeu!')
        exibir_perdeu()
    elif acertou:
        print('A palavra é: {}'.format(palavra_secreta))
        print('Você ganhou!')
        exibir_ganhou()
    print('O jogo acabou.')


def desenha_forca(erros, apontamentos):
    print("  _______     ")
    print(" |/      |    ")
    if(erros == 0):
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print(join(apontamentos))


if __name__ == '__main__':
    inicializar_jogo()
