valor=list()
resp = ' '
while True:
    n=int(input('Digite um valor :'))
    if n not in valor:
        valor.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! não vou adicionar...')
    resp = str(input('Que continuar [S/N] :')).upper().strip()[0]
    if resp in 'Nm':
        break
print('=-'*30)
print(f'O valor adicionados foram {sorted(valor)}')
print('=-'*30)