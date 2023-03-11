valores=list()
pares=list()
impares=list()
while True:
    valores.append(int(input('Digite um valor:')))
    resp=str(input('Quer continuar [S/N]:'))
    if resp in 'Nn':
        break
for i, v in enumerate(valores):
    if v % 2==0:
        pares.append(v)
    else:
        impares.append(v)
print('=-'*30)
print(f'A lista Completa são {sorted(valores)};')
print(f'A lista de Pares são {sorted(pares)};')
print(f'A lista de ímpares são {sorted(impares)}.')
print('=-'*30)
