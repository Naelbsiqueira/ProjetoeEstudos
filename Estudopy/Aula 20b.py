def contador (*num): #Criou uma tupla. DESEMPACOTAR !!!
    for v in num:
        print(f'{v} ', end=' ')
    print('Fim...')

contador(2,3,5)
contador(8,0)
contador(2,4,8,1,0)

def soma(*v): # Criou uma tupla. DESEMPACOTAR !!!
    s=0
    for i in v:
        s+=i
    print(f'Somando os valores {v} temos {s}')

soma(2,3,5)
soma(8,0)
soma(2,4,8,1,0)
