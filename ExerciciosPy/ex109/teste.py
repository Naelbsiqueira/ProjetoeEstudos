import moeda
print('~'*20)
p=float(input('Digite um preço: R$'))
print('~'*20,)
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p,True)}.')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p,True)}.')
print(f'Aumento de 10%, temos {moeda.aumentar(p,10,True)}.')
print(f'Com desconto de 25%, temos {moeda.diminuir(p,25,True)}.')
