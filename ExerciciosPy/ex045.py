from random import randint
from time import sleep
itens=('Pedra', 'Papel','Tesoura')
computador = randint(0,2)
print('Suas opções')
print('[0]PEDRA')
print('[1]PAPEL')
print('[2]TESOURA')
jogador=int(input('Qual sua escolha?'))
print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PO!!!')
print('-='*15)
print ("O jogador escolheu {}: ".format(itens[jogador]))
print ("O Computador escolheu {}: ".format(itens[computador]))
print('-='*15)
if computador == 0:
    if jogador ==0:
        print('EMPATE')
    elif jogador ==1:
        print('JOGADOR VENCEU')
    elif jogador ==2:
        print('COMPUTADOR VENCEU')
    else:
        print('Jogada invalida')
elif computador == 1:
    if jogador ==0:
        print('COMPUTADOR VENCEU')
    elif jogador ==1:
        print('EMPATE')
    elif jogador ==2:
        print('JOGADOR VENCEU')
    else:
        print('Jogada invalida')
elif computador == 2:
    if jogador ==0:
        print('JOGADOR VENCEU')
    elif jogador ==1:
        print('COMPUTADOR VENCEU')
    elif jogador ==2:
        print('EMPATE')
    else:
        print('Jogada invalida')


