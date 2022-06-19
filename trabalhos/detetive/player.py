import sys
from time import sleep

class Player:

    def __init__(self, nome, local):
        self.nome = nome
        self.local = local
        self.evidencias = []
        self.caminho = []

    def mover(self, local, localO):
        self.local = local
        self.caminho.append(localO)

    def pensar(self, mensagem):
        for i in mensagem:
            sys.stdout.write(i)
            sys.stdout.flush()
            sleep(0.02)
        print('')
        sleep(0.5)

    def recapitular(self):
        for i in range(len(self.evidencias)):
            self.pensar(i, self.evidencias[i])
