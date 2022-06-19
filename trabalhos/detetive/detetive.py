'''
Autores:
Leandro de Carvalho Medeiros
Luca Takemura Piccoli
Rafael da Silva Albuquerque
Yan Felipe Ferreira da Silva
'''

from lugares import *
from pessoas import *
from player import *
from time import sleep
from os import system
from random import choice, randint
import pygame

try:
    system('cls')
except:
    print('')
print('-=-' * 10)
print(f'{"O SUMIÇO DO SANDUÍCHE":^30s}')
print('-=-' * 10)
#sleep(3)
input('Pressione Enter para começar...')

nomes_padrao = ['Rafael', 'Vicente', 'Leandro', 'Luca', 'Yan']

nomes = [input('Nome do jogador: [vazio para padrão] '), input('Nome de um colega: '), input('Nome de outro colega: '), input('Nome de mais um colega: '), input('Nome do último colega: ')]
for nome in range(len(nomes)):
    if nomes[nome] == '' or nomes[nome] == ' ':
        nomes[nome] = nomes_padrao[nome]

Leandro = Pessoa(nomes[2], ['Que foi mano?', f'O {nomes[4]} é quieto, pessoas quietas sempre são suspeitas. Então acho que foi ele.', '', 'Até depois...'])
Luca = Pessoa(nomes[3], ['eae.', f'Bom, o {nomes[2]} esqueceu o lanche dele hoje.', f'Além disso, já percebeu que o {nomes[4]} sempre tá com fome?', 'Falou.'])
Colega1 = Pessoa(nomes[1], ['E aí cara, beleza? :).', f'Sanduíche? Bom, eu vi o {nomes[3]} comendo um sanduíche durante o intervalo...',
 f'O {nomes[4]} passou o intervalo inteiro no banheiro', 'Falou mano, espero que ache o culpado desse crime hediondo!'])
Yan = Pessoa(nomes[4], ['Vamo atrás desse ladrão de sanduíche', f'Percebeu que o {nomes[2]} sempre traz lanche, mas hoje não trouxe? Suspeito...',
 'Mano, eu passei o intervalo todo no banheiro, não pode ter sido eu.', 'Até mais.'])

pessoas = {
    "Colega1" : Colega1,
    "Leandro" : Leandro,
    "Luca" : Luca,
    "Yan" : Yan
}

Banheiro = Lugar('Banheiro', ['Corredor'], [], [], 'banheiro.mp3')
Corredor = Lugar('Corredor', ['Banheiro', 'Sala', 'Escadaria'], [Colega1], [], 'main.mp3')
Escadaria = Lugar('Escadaria', ['Frente do bloco 9', 'Corredor'], [Luca], [], 'main.mp3')
Sala = Lugar('Sala', ['Corredor'], [Leandro], ['Você encontrou um guardanapo no lixo da sala. O guardanapo é preenchido com imagens do Shrek.', 'Há migalhas de pão na mesa do Yan.'], 'main.mp3')
Bloco9 = Lugar('Frente do bloco 9', ['Escadaria'], [Yan], [], 'bloco9.mp3')

lugares = {
    "Banheiro" : Banheiro,
    "Frente do bloco 9" : Bloco9,
    "Corredor" : Corredor,
    "Escadaria" : Escadaria,
    "Sala" : Sala
}

jogar = True
local_inicial = lugares.get("Sala")
player = Player(nomes[0], local_inicial.nome)
player.caminho.append(local_inicial)
player.caminho.append(local_inicial)

def acoes(lugar):

    print('O que quer fazer agora?')
    print('[1] Ir para outro lugar: ', end='')
    for i in range(len(lugar.acessos)):
        print(lugar.acessos[i], end='')
        if len(lugar.acessos) > 1 and i != len(lugar.acessos) - 1:
            print(', ', end='')

    print('')
    if len(lugar.pessoas) != 0:
        print('[2] Falar com alguém: ', end='')
        for i in lugar.pessoas:
            print(i.nome, end=' ')
        print('')
    print('[3] Examinar o local.')

    if len(player.evidencias) != 0:
        print('[4] Recapitular pistas.')
    
    print('[5] Acusar alguém.')

    print('O que quer fazer?')
    acao = int(input('>'))
    if acao == 1:
        if len(lugar.acessos) == 1:
            entrada = 0
            player.mover(lugar.acessos[0], lugar)
        else:
            possibilidades = len(lugar.acessos)
            for i in range(possibilidades):
                print(f'[{i}] {lugar.acessos[i]}', end=' ')
            print('')
            entrada = int(input('>'))
            while 0 > entrada or entrada >= possibilidades:
                print('Opção inválida! Tente novamente.')
                entrada = int(input('>'))
            player.mover(lugar.acessos[entrada], lugar)
        print(f'Indo até {lugar.acessos[entrada]}...')
    elif acao == 2:
        if len(lugar.pessoas) == 0:
            player.pensar('Não tem ninguém aqui... Queria meu sanduíche :(')
        elif len(lugar.pessoas) == 1:
            lugar.pessoas[0].interagir()
        else:
            possibilidades = len(lugar.pessoas)
            for i in range(possibilidades):
                print(f'[{i}] {lugar.pessoas[i]}', end=' ')
            print('')
            entrada = int(input('>'))
            pessoa = lugar.pessoas[entrada]
            while 0 > entrada or entrada >= possibilidades:
                print('Opção inválida! Tente novamente.')
                entrada = int(input('>'))
            pessoa.interagir()
            pistas = pessoa.pistas_dadas()
            for i in range(len(pistas)):
                if pistas[i] not in player.evidencias:
                    player.evidencias.append(pistas[i])
    elif acao == 3:
        if len(lugar.pistas) != 0:
            evidencia = lugar.pistas[0]
            player.pensar(evidencia)
            player.evidencias.append(lugar.pistas.pop(0))
        else:
            player.pensar('Não há nenhuma pista por aqui. Que fome...')
    elif acao == 4:
        player.recapitular()
    elif acao == 5:
        print('É recomendável que você recapitule as pistas antes de chegar a uma decisão.')
        print('Tem certeza? Uma acusação falsa pode lhe custar tudo. [s/n]')
        entrada = input('>').strip().lower()
        while entrada not in 'sn':
            entrada = input('>').strip().lower()
        if entrada == 's':
            print('Vai acusar quem?')
            possibilidades = len(pessoas)
            nomes = []
            for nome in pessoas:
                print(f'{pessoas.get(nome).nome}', end=' ')
                nomes.append(pessoas.get(nome).nome)
                print('')
            acusado = input('Digite o nome de quem quer acusar... >').strip()
            while acusado not in nomes:
                acusado = input('>').strip()
            player.pensar('S u s p e n s e . . .')
            player.pensar('..........')
            sleep(2)
            acusar(acusado)

    sleep(1.5)


def deducao():
    print('A = Luca foi visto comendo um sanduíche de atum durante o intervalo.\nB = Leandro sempre leva lanche.\nC = Yan sempre está com fome.')
    print('D = O guardanapo do Shrek foi encontrado no lixo da sala de aula.\nE = Há migalhas na mesa do Yan.\nF = Leandro esqueceu seu lanche naquele dia.')
    print('G = Leandro roubou o sanduíche.\nH = Yan roubou o sanduíche.\nI = Luca roubou o sanduíche.\nJ = Yan passou o intervalo no banheiro.')
    print('K = O sanduíche foi comido na sala de aula.\nL = O sanduíche foi comido no corredor.\nN = Leandro estava na sala durante o intervalo.')
    print('O = Luca estava na sala durante o intervalo.\nP = O seu sanduíche era de presunto.')

    print('1. A ^ P -> ~I\t\thip\n2. J -> ~H\t\thip\n3. (D ^ E) -> K\t\thip\n4. K -> ~L\t\thip')
    print('5. (K ^ ~L) -> ~H\thip \n6. B ^ F ^ N ^ E -> G\thip\n7. ~H -> I v G\t\thip')
    print('8. K v L\t\thip\n---------------------------\n9. D ^ E -> ~L\t\td. c. 3, 4\n10. (K ^ ~L) -> I v G\td. c. 5, 7\n11. ~I ^ ~H -> G\tconcl.')


def acusar(acusado):
    global jogar
    if acusado == pessoas.get('Leandro').nome:
        print(f'Parabéns, Sherlock! Você acertou na acusação e venceu o jogo. Se não fosse por essas crianças enxeridas, {acusado} teria saído impune!')
    else:
        print(f'{acusado} era inocente e você errou na acusação. Agora vai ficar sozinho e com fome! >:(')
    print('Gostaria de ver a dedução da resposta correta? [s/n]')
    ded = input('>').strip().lower()
    while ded not in 'sn':
        ded = input('>').strip().lower()
    if ded == 's':
        deducao()
    jogar = False

musica_funcionando = True

def lidar_musica(musica, trocar):
    global musica_funcionando

    if musica_funcionando:
        if trocar:
            pygame.mixer.music.stop()
        pygame.mixer.music.load(musica)
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.music.play()
        pygame.mixer.music.queue(musica)
        return musica


musica = ' '
while musica not in 'sn':
    print('Gostaria de ter música durante o jogo? [s/n]')
    musica = input('>').strip().lower()

if musica == 's':
    try:
        pygame.mixer.init()
        musica_atual = lidar_musica('main.mp3', True)
    except:
        print('Ocorreu um erro carregando a biblioteca Pygame.')


player.pensar('\nREGRAS\nVocê começará o jogo na Sala de aula.\nPara jogar, digite o que o jogo pedir para interagir com o menu.')
player.pensar('Você deverá procurar pistas pelos ambientes e falando com as pessoas.\nA partir disso, deverá chegar a uma conclusão. Se errar, perde.\nQuando tiver coletado evidências, você poderá listá-las através do comando "Recapitular evidências" que aparecerá no menu.')
sleep(5)
print('\n')


print('\n\nCONTEXTO INICIAL:')
player.pensar(f'Durante uma aula de lógica matemática, {player.nome} sai da sala brevemente para encher sua garrafa de água...')
player.pensar(f'Quando chega o horário do intervalo, {player.nome} procura o sanduíche de presunto embrulhado em um guardanapo do Shrek que havia guardado em sua mochila antes de sair de casa, porém não o encontra...')
player.pensar(f'{player.nome} fica igualmente enfurecido e determinado a encontrar o autor deste crime de furto ao fim da aula...')
player.pensar(f'\nVocê jogará como {player.nome}, resolva esse caso como um detetive o faria! Boa sorte.')


while jogar:
    local_atual = lugares.get(player.local)

    if local_atual.musica != player.caminho[-1].musica:
        lidar_musica(local_atual.musica, False)

    # código pra mudar o leandro e o luca de lugar aleatoriamente, mas está quebrado por enquanto
    # mudar = randint(0, 3)
    # if mudar == 3:
    #     for lugar in lugares:
    #         if Leandro in lugares.get(lugar):
    #             locacao_atual = lugar
    #     locacao_atual.pessoas.remove(Leandro)
    #     destino = choice(lugares)
    #     lug = destino.get(destino.nome)
    #     lug.pessoas.append(Leandro)

    print('\n', end='')
    print('-=-' * 30)
    print('Você está em:', local_atual.nome)
    acoes(local_atual)
