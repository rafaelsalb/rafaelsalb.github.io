from random import randint

'''
definindo os números que serão usados para fazer as contas
são usadas oito variáveis porque os números só devem mudar a cada execução,
e não a cada iteração
'''

acertos = 0
n1 = randint(0, 1000)
n2 = randint(0, 1000)
n3 = randint(0, 1000)
n4 = randint(0, 1000)
n5 = randint(0, 1000)
n6 = randint(0, 1000)
n7 = randint(0, 1000)
n8 = randint(0, 1000)
resposta = float()

while acertos < 4:
    
    print(f'Qual o resultado de {n1} + {n2}?')
    resposta = float(input('>'))  # a variável resposta é redefinida pq ela só serve pra checar o acerto

    print(f'Qual o resultado de {n3} - {n4}?')
    resposta = float(input('>'))

    print(f'Qual o resultado de {n5} * {n6}?')
    resposta = float(input('>'))

    print(f'Qual o resultado de {n7} / {n8}?')
    resposta = float(input('>'))
