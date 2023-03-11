import moeda
print('~'*20)
p=float(input('Digite um preço: R$'))
print('~'*20,)
print(f'A metade de R$ {p} é {moeda.metade(p)}R$.')
print(f'O dobro de R${p} é {moeda.dobro(p)}R$.')
print(f'Aumento de 10%, temos {moeda.aumentar(p,10)}R$.')
print(f'Com desconto de 25%, temos {moeda.diminuir(p,25)}R$.')
