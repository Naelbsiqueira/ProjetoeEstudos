print('=='*10)
print('SUPERMERCADO BARATÃO')
print('=='*10)
totC= totM = cont= menor= 0
barato=''
while True:
    prod=str(input("Nome do Produto:"))
    preco=float(input('R$:'))
    totC+=preco
    cont+=1
    opc=' '
    if preco >= 1000:
        totM+=1
    if cont ==1 or preco < menor:
        menor=preco
        barato = prod
    while opc not in 'SN':
        opc=str(input('Quer continuar:')).upper().strip()[0]
    if opc=='N':
        break
print ('{:=^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi {totC:.2f}R$')
print(f'Temos {totM:.0f} produtos que custa mais de R$1000.00')
print(f'O produto mais barato foi {barato} e custou {menor:.2f}R$')