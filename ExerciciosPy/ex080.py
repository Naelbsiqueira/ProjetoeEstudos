lista= list()
for c in range (0,5):
    n = int(input(f"Digite um valor {c}:"))
    if c == 0 or n > lista[len(lista)-1]:
        lista.append(n)
        print('adicionado ao final da lista...')
    else:
        pos=0
        while pos<len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'adicionado na posição {pos} da lista ')
                break
            pos+=1
print('=-'*0)
print(f'Os valores digitados foram {lista}')
print('adicionado ao final da fila...')
