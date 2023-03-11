# As listas [] são mutáveis.

lanche= ['Amburguer', 'Suco', 'Pizza','Pudim' ]
lanche[2]= 'Filé' #troca elemento em uma lista
print(lanche)
#Para adicionar elementos em uma listas o comando utilizado é
#lanche.append('elemento')

# Para inserir elemento em uma lista em qualquer parte da lista o comando utilizado é
#lanche.insert(0,'Elemento')

#Para apagar elemento de uma lista basta ultilizar o comando
#del lanche[3]
#lanche.pop(3)
#lanche.remove('Elemento escrito')
#lanche.pop() remove o último elemento.

# caso o elemento não estive na lista, utiliza-se o comando if.
#if 'refrigerante'in lanche:
    #lanche.remove('refrigerante')

#valores=list(range(4,11))
#print(valores)

# valores na ordem reversa:
#valores.sort(reverse=True)
#len(valores)
#print(valores)
#print(len(valores))

#valores=[]
#for cont in range(0,5):
    #valores.append(int(input('Digite um Valor:')))
#for c,v in enumerate(valores):
    #print(f'Na posição {c} temos o valor {v}!')
#print('Chegamos ao final.')

#a=[1,2,8,5] # Nesse exemplo as duas lista se modifica. Existe uma ligação da elemento.
#b=a
#b[3]=9
#print(f'Lista A:{a}')
#print(f'Lista B:{b}')

a=[1,2,8,5]
b=a [:] # Nesse exemplo à um cópia da lista com o comando '[:]'.
b[3]=9
print(f'Lista A:{a}')
print(f'Lista B:{b}')