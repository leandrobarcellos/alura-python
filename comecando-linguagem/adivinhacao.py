"""
Para comentar múltiplas linhas devem ser utilizadas três aspas simples ou duplas.
Dessa forma é possível fazer funcionar.
"""
import re  # disponibiliza o uso das funções regex
from random import randint  # disponibiliza o uso da função randint

regexOnlyNumbers = '^[0-9]+$'


def mostrar_pontuacao(pontuacao):
    print('Você conquistou {} pontos'.format(pontuacao))


def calcular_penalidade(nro_secreto, chute, pontuacao_atual):
    if re.match(regexOnlyNumbers, f'{chute}'):
        sub = abs(nro_secreto - chute)
    else:
        sub = 100
    return pontuacao_atual - sub


def orientacao_jogo():
    print('Digite um número de 0 a 100')


def verificar_chute(numero_secreto, tentativas):
    chute_str = input('Digite seu número: ')
    chute = ''
    if re.match(regexOnlyNumbers, chute_str):
        chute = int(chute_str)
        if numero_secreto == chute:
            print('Acertou miserávi! Depois de {} tentativas.'.format(tentativas))
        elif chute > numero_secreto:
            print('O número é menor que ', chute)
        elif chute < numero_secreto:
            print('O número é maior que ', chute)
    else:
        print('Texto digitado inválido. Digite um número de 0 a 100')
    return chute


def jogo_desafio(numero_secreto):
    pontuacao = 1000
    nivel = int(input('Informe o nível de dificuldade: 1 - Fácil / 2 - Médio / 3 - Difícil'))
    tentativas = 21
    if nivel == 3:
        tentativas = 7
    elif nivel == 2:
        tentativas = 14
    orientacao_jogo()
    for rodada in range(1, tentativas + 1):
        print('Tentativas restantes: {}'.format(tentativas + 1 - rodada))
        chute = verificar_chute(numero_secreto, rodada)
        if chute == numero_secreto:
            break
        pontuacao = calcular_penalidade(numero_secreto, chute, pontuacao)
    mostrar_pontuacao(pontuacao)
    print('O jogo acabou.')


def jogo_livre(numero_secreto):
    pontuacao = 1000
    acertou = False
    tentativas = 0
    orientacao_jogo()
    while not acertou:
        tentativas = tentativas + 1
        chute = verificar_chute(numero_secreto, tentativas)
        acertou = chute == numero_secreto
        pontuacao = calcular_penalidade(numero_secreto, chute, pontuacao)
    mostrar_pontuacao(pontuacao)


def inicializar_jogo():
    print('*********************************')
    print('Bem vindo ao jogo de Adivinhação!')
    print('*********************************')

    adivinhar_novamente = 'S'

    while adivinhar_novamente == 'S':
        modo_jogo = input('Escolha o modo de jogo: 1 - Desafio / 2 - Livre ')
        numero_secreto = randint(1, 100)
        if 1 == int(modo_jogo):
            jogo_desafio(numero_secreto)
        else:
            jogo_livre(numero_secreto)
        adivinhar_novamente = input('Tentar novamente? S/N ').upper()
    print('O jogo acabou.')


if __name__ == '__main__':
    inicializar_jogo()
