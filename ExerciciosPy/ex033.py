a=int(input('Primeiro número:'))
b=int(input('Segundo número:'))
c=int(input(('Terceiro número:')))
#Verificando quem é menor:
menor=a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c
#verificando quem é o maior:
maior=a
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior=c
    print('O menor valor digitado foi {}.'.format(menor))
    print('O maior valor digitado foi {}.'.format(maior))
