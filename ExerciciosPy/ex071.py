print('='*30)
print('{:^30}'.format('BANCO NBS'))
print('='*30)
valor=int(input('Que valor você quer sacar?R$ '))
total = valor
ced = 50
totC=0
while True:
    if total >=ced:
        total-=ced
        totC+=1
    else:
        if totC > 0:
            print(f'Total de {totC} cédulas  de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced=10
        elif ced == 10:
            ced = 1
        totC=0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao Banco BNS')
print('='*30)
