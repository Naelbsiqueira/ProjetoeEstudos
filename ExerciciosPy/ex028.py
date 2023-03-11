from random import randint
from time import sleep
computador = randint(0,5)
num = int(input('Escolha um numero entre 0 e 5:'))
print('PROCESSANDO...')
sleep(3)
print('O numero sorteado foi {}'.format(computador))
if num == computador:
    print('Você ganhou, PARABÉNS!')
else:
    print('Que pena você perdeu,tente novamente!')