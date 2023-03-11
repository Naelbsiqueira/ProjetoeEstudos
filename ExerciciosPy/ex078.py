valores=[]
mai= men= 0
for c in range (0,5):
    valores.append(int(input(f'Digite um valor para pasição {c}:')))
    if c==0:
        mai=men=valores[c]
    else:
        if valores[c]>mai:
            mai=valores[c]
        if valores[c]<men:
            men=valores[c]
        else:
            c<men
print('=-'*30)
print(f'Você digitou {valores}')
print(f'O maior valor digitado foi {mai} nas posições ' , end='')
for i, v in enumerate (valores):
    if v==mai:
        print(f'{i}...', end='')
print(f'\nO menor valor digitado foi {men} nas posições ' , end='')
for i, v in enumerate (valores):
    if v==men:
        print(f'{i}...', end='')


