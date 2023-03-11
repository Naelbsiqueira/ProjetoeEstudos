cont = ('zero','um', 'dois', 'três', 'quatro', 'cinco' ,'seis', 'sete', 'oito', 'nove', 'dez',
'onze', 'doze', 'treze', 'cartorze', 'quinz', 'dezesseis', 'dezesete','dezoito', 'dezenove','vinte',)
while True:
    num = int(input("Digite um Número entre 0 e 20:"))
    if 0 <= num <= 20:
        break
    print("Tente novamente ! ", end=' ')
print(f'Você digitou o número {cont[num]}')