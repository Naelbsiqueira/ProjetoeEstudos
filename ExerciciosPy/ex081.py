valores = []
cont=0
while True:
    valores.append(int(input('Digite um valor :')))
    resp = str(input('Quer continuar [S/N] ?')).upper().strip()[0]
    cont+=1
    if resp in 'Nn':
        break
print(f'foram digitados {len(valores)}')
valores.sort(reverse=True)
print(f'O valores em ordem decrecente é {valores} ')
if 5 in valores:
    print('O valor 5 faz parte da lista')
else:
    print('Valor não encontrado')