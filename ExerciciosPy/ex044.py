print('{} Lojas Bernardo {}'.format('='*10,'=' *10))
compras= float(input('Preço das compras: R$'))
print('\033[1;42mFORMAS DE PAGAMENTO\033[m')
print('[1] à vista dinheiro/cheque.')
print('[2] à vista cartão.')
print('[3] 2x no cartão.')
print('[4] 3x no cartão.')
opção = int(input('Qual sua opção? '))
if opção == 1:
    print('Suas compras de {:.2f}R$ com pagamento a vista ficarão {:.2f}R$.'.format(compras,(compras - (compras * 10 / 100))))
elif opção == 2:
    print('Suas compras de {:.2f}R$, à vista no cartão ficarão {:.2f}R$.'.format(compras, (compras - (compras * 5 / 100))))
elif opção ==3:
    print('Suas compras de {:.2f}R$, parcelado em 2x, ficarão {:.2f}R$ SEM JUROS, por parcela.'.format(compras, (compras/2)))
elif opção == 4:
    total=compras+(compras*20/100)
    totparc= int(input('Quantas parcelas?'))
    parcela=total/totparc
    print('''Sua compra de {:.2f}R$, parcelado em {}x, ficarão {:.2f}R$ COM JUROS 
    por parcela, com o total da compra em {:.2f}R$ no final.'''.format(compras,totparc,parcela, total))
else:
    print('\033[1;43mERRO! tente novamente\033[m')
