resp ='S'
cont = soma = media = maior= menor = 0
while resp in 'Ss':
    num =int(input('Digite um número:'))
    soma+=num
    cont+=1
    if cont ==1:
        maior = menor = num
    else:
        if num > maior:
            maior=num
        if num < menor:
            menor=num
    resp=str(input('Quer continuar ? [S/N]')).upper().strip()[0]
media= soma/cont
print('Você digitou {} valores, a soma foi {}, a media é de {}.'.format(cont,soma, media))
print('O maior valor foi {} e o menor foi. {}'.format(maior, menor))
