import forca
import adivinhacao


def exibir_jogos():
    print('****************')
    print('Escolha seu jogo')
    print('****************')
    continua_jogando = 'S'
    while continua_jogando.upper() == 'S':
        print('(1) Forca (2) Adivinhação')
        jogo = int(input('Escolha o jogo'))
        if jogo == 1:
            print('Jogando Forca')
            forca.inicializar_jogo()
        elif jogo == 2:
            print('Jogando Adivinhação')
            adivinhacao.inicializar_jogo()
        continua_jogando = input('Deseja continuar jogando? S/N ')


if __name__ == '__main__':
    exibir_jogos()
