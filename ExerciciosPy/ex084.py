temp=list()
prin=list()
mai=men=0
while True:
    temp.append(str(input('Nome:')))
    temp.append(float(input('Peso:')))
    if len(prin) == 0:
        mai=men=temp[1]
    else:
        if temp[1]>mai:
            mai=temp[1]
        if temp [1]<men:
            men=temp[1]
    prin.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar [S/N]:')).upper().strip()[0]
    if resp in 'Nn':
        break
print('=-'*30)
print(f'Ao todo, você cadastrou {len(prin)} pessoas.')
print(f'O maior peso foi {mai}Kg, Peso de ',end='')
for p in prin:
    if p[1] ==mai:
        print(f'[{p[0].upper()}]',end='')
print()
print(f'O menor peso foi {men}Kg, Peso de', end='')
for p in prin:
    if p[1] ==men:
        print(f'[{p[0].upper()}]',end='')
print()

