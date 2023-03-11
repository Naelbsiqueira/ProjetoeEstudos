from random import randint
computador = randint(0,10)
cont=0
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.\nSera que você consegue adivinhar qual foi?')
num = int(input('Escolha um número:'))
while num != computador:
    if num > computador:
        cont += 1
        num=int(input('MENOS! digite um número:'))
    elif num < computador:
        cont += 1
        num = int(input('MAIS! digite um número:'))
if num == computador:
    cont+=1
    print('Você acertou com {} tentativas, PARABÉNS!'.format(cont))
