'''
Membros do grupo:

Leandro de Carvalho Medeiros
Rafael da Silva Albuquerque
Yan Felipe Ferreira da Silva
'''

from random import randint

modo = 0
jogar = True
jogador1 = jogador2 = int()
vitoriasJogador1 = int()
vitoriasJogador2 = int()

print('Escolha o modo de jogo:'
      '\n\033[32:40m[1] Humano vs Humano\033[m'
      '\n\033[36:40m[2] Humano vs Computador\033[m')

while modo < 1 or modo > 2:  # para evitar um erro
    modo = int(input('Modo de jogo: '))

if modo == 1:
    print('\n\033[32:40mHUMANO\033[37:40m VS \033[36:40mHUMANO\033[m\n')
    while jogar:
        print('[0] Parar [1] Pedra [2] Papel [3] Tesoura')
        jogador1 = int(input('O que vai jogar? '))
        jogador2 = int(input('O que vai jogar? '))


        if jogador1 == 0 or jogador2 == 0:
            jogar = False
        elif jogador1 == 1:
            if jogador2 == 1:
                print('\033[33mEmpate.\033[m')
            elif jogador2 == 2:
                print('\033[36mO jogador 2 ganhou.\033[m')
                vitoriasJogador2 += 1
            elif jogador2 == 3:
                print('\033[32mO jogador 1 ganhou.\033[m')
                vitoriasJogador1 += 1
        elif jogador1 == 2:
            if jogador2 == 1:
                print('\033[32mO jogador 1 ganhou.\033[m')
                vitoriasJogador1 += 1
            elif jogador2 == 2:
                print('\033[33mEmpate.\033[m')
            elif jogador2 == 3:
                print('\033[36mO jogador 2 ganhou.\033[m')
                vitoriasJogador2 += 1
        elif jogador1 == 3:
            if jogador2 == 1:
                print('\033[36mO jogador 2 ganhou.\033[m')
                vitoriasJogador2 += 1
            elif jogador2 == 2:
                print('\033[32mO jogador 1 ganhou.\033[m')
                vitoriasJogador1 += 1
            elif jogador2 == 3:
                print('\033[33mEmpate\033[m')

        print(f'\033[32mJogador 1: {vitoriasJogador1}\033[m x \033[36m{vitoriasJogador2} Jogador 2\033[m\n')
elif modo == 2:
    print('\n\033[32:40mHUMANO\033[37:40m VS \033[31:40mCOMPUTADOR\033[m\n')
    while jogar:
        print('[0] Parar [1] Pedra [2] Papel [3] Tesoura')
        while jogador1 < 1 or jogador1 > 3:
            jogador1 = int(input('O que vai jogar? '))
        jogador2 = randint(1, 3)

        if jogador1 == 0:
            jogar = False
        elif jogador1 == 1:
            if jogador2 == 1:
                print('\033[33mEmpate.\033[m')
            elif jogador2 == 2:
                print('\033[31mO computador ganhou.\033[m')
                vitoriasJogador2 += 1
            elif jogador2 == 3:
                print('\033[32mVoc?? ganhou.\033[m')
                vitoriasJogador1 += 1
        elif jogador1 == 2:
            if jogador2 == 1:
                print('\033[32mVoc?? ganhou.\033[m')
                vitoriasJogador1 += 1
            elif jogador2 == 2:
                print('\033[33mEmpate.\033[m')
            elif jogador2 == 3:
                print('\033[31mO computador ganhou.\033[m')
                vitoriasJogador2 += 1
        elif jogador1 == 3:
            if jogador2 == 1:
                print('\033[31mO computador ganhou.\033[m')
                vitoriasJogador2 += 1
            elif jogador2 == 2:
                print('\033[32mVoc?? ganhou.\033[m')
                vitoriasJogador1 += 1
            elif jogador2 == 3:
                print('\033[33mEmpate\033[m')

        print(f'\033[32mJogador 1: {vitoriasJogador1}\033[m x \033[31m{vitoriasJogador2} Computador\033[m\n')
