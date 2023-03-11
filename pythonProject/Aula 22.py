#import uteis # Modularização, serve para importar modulos que so próprio usuário cria.
from uteis import numeros
num=int(input('Digite um valor:'))
fat=numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {numeros.dobro(num)}.')
print(f'O tripo de {num} é {numeros.tripo(num)}.')

#nome do modulo, nome da função(rotina)
#       |              |
#       |              |
#       v              v
#from uteis import fatorial
#from random import randint
#from datetime import datetime
#from math import sqrt