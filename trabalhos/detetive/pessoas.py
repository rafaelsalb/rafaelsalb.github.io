import sys
from time import sleep

class Pessoa:

    def __init__(self, nome_i, conversas_i) -> None:
        self.nome = nome_i
        self.n_interacao = 0
        self.interacoes = conversas_i
        self.conversas = [self.interacoes[0], self.interacoes[1], self.interacoes[2], self.interacoes[3]]
        self.evidencias = []

    def falar(self, mensagem):
        for i in mensagem:
            sys.stdout.write(i)
            sys.stdout.flush()
            sleep(0.05)
        print('')
        sleep(0.5)

    def interagir(self):
        self.n_interacao = 0
        fala = self.nome + ': ' + self.conversas[self.n_interacao]
        self.falar(fala)
        self.n_interacao += 1
        falar = True
        while falar:   
            print('[1] Perguntar o que sabe. [2] Despedir-se.')
            interacao = int(input('>'))
            while interacao < 0 or interacao > 2:
                interacao = int(input('>'))
            if interacao == 2:
                self.falar(self.nome + ': ' + self.conversas[3])
                falar = False
            else:
                fala = self.nome + ': ' + self.conversas[self.n_interacao]
                if fala not in self.evidencias:
                    self.evidencias.append(fala)
                self.falar(fala)
                self.n_interacao += 1
                if self.n_interacao > 2:
                    self.n_interacao = 1
    
    def pistas_dadas(self):
        return self.evidencias
