sal=float(input('Qual o salario do funcionário? R$'))
if sal>1250:
    novo= sal+(sal*10/100)
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(sal,novo))
else:
    novo = sal + (sal * 15 / 100)
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(sal,novo))