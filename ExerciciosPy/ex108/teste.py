import moeda
print('~'*20)
p=float(input('Digite um preço: R$'))
print('~'*20,)
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}.')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}.')
print(f'Aumento de 10%, temos {moeda.moeda(moeda.aumentar(p,10))}.')
print(f'Com desconto de 25%, temos {moeda.moeda(moeda.diminuir(p,25))}.')
