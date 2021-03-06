# Renan Antonio Hammerschmidt Krefta
# Rafael da Silva Albuquerque

import time
import random


# Gera a matriz resposta a partir da dificuldade selecionada e a mostra uma vez
def matriz_resposta(tamanho):

    resposta = []
    vet = []

    for m in range(0, tamanho):
        resposta.append([])

        for n in range(0, tamanho):
            resposta[m].append(0)

    for m in range(0, tamanho):
        for n in range(0, tamanho):

            if resposta[m][n] == 0:
                num = chr(random.randint(65, 88))
                resposta[m][n] = num
                j = 0

                while j == 0:
                    linha_resp = random.randint(0, tamanho - 1)
                    coluna_resp = random.randint(0, tamanho - 1)

                    if resposta[linha_resp][coluna_resp] == 0:
                        resposta[linha_resp][coluna_resp] = num
                        j = 1

    for m in range(0, tamanho):
        vet.append(str(m))

    return resposta


#Gera a matriz hash a partir da dificuldade selecionada
def matriz_hash(tamanho):

    hash_mat = []

    for m in range(0, tamanho):
        hash_mat.append([])

        for n in range(0, tamanho):
            hash_mat[m].append('#')

    return hash_mat


#Printa a matriz selecionada.
def matriz_print(m_print):
    tamanho = len(m_print)
    vet = []

    for m in range(0, tamanho):
        vet.append(str(m))

    print("#", vet)

    for m in range(0, tamanho):
        print(m, m_print[m])


def matriz_dica(resposta, hash):

    matriz_print(resposta)
    time.sleep(3)
    print('\n' * 50)
    matriz_print(hash)
    print(f'Você tem {dica} dica(s) restante(s).')


print('•' * 30)
print(f'{"JOGO DA MEMÓRIA":^30s}')
print('•' * 30)
modo = int(input("Escolha a dificuldade: Fácil (1) Médio (2) Dificil (3)."))

if modo == 1:
    tam = 4
elif modo == 2:
    tam = 8
elif modo == 3:
    tam = 10

jogo = 0
dica = 2
m_resp = matriz_resposta(tam)
m_hash = matriz_hash(tam)
matriz_print(m_resp)
time.sleep(3/4 * tam)
print('\n' * 50)
matriz_print(m_hash)
print("Para desistir, digite 10.\nPara uma dica, digite 11.\nVocê pode pedir uma dica 2 vezes.")

while jogo == 0:

    valido = 0

    while valido == 0 and jogo == 0:
        linha = int(input("Insira a linha: "))
        coluna = 0

        if linha < 10:
            coluna = int(input("Insira a coluna: "))

            if m_hash[linha][coluna] != '#':
                print("Célula inválida!")

            else:
                valido += 1

        if linha == 10 or coluna == 10:
            jogo = 1
            print("Jogador escolheu SAIR.")

        elif (linha == 11 or coluna == 11) and dica > 0:
            dica -= 1
            matriz_dica(m_resp, m_hash)

        while valido == 1 and jogo == 0:
            linha2 = int(input("Insira a linha 2: "))
            coluna2 = 0

            if linha2 < 10:
                coluna2 = int(input("Insira a coluna 2: "))

                if m_hash[linha2][coluna2] != '#':
                    print("Célula inválida!")

                else:
                    valido = 0

            if linha2 == 10 or coluna2 == 10:
                jogo = 1
                print("Jogador desistiu.")

            elif (linha2 == 11 or coluna2 == 11) and dica > 0:
                dica -= 1
                matriz_dica(m_resp, m_hash)

            elif m_resp[linha][coluna] == m_resp[linha2][coluna2]:

                if linha != linha2 or coluna != coluna2:

                    if m_hash[linha][coluna] and m_hash[linha2][coluna2] == '#':
                        m_hash[linha][coluna], m_hash[linha2][coluna2] = m_resp[linha][coluna]
                    
                    else:
                        print("Célula inválida!")
                    
                else:
                    print("Célula inválida!")

            matriz_print(m_hash)

        if m_hash == m_resp:
            jogo = 2

if jogo == 1:
    print("Jogo terminado por desistência.")

else:
    print("Jogo terminado.\nParabéns! Todas as respostas encontradas.")
