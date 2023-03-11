ano=int(input('Que ano quer analisar ?'))
if ano%4==0 and ano%100!=0 or ano%400==0:
    print('É um ano BISSEXTO!')
else:
    print('Não é um ano BISSEXTO!')