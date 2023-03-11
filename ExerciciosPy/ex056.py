soma=0
maioridade=0
nomevelho=0
totm20=0
for p in range(1,5):
    print('----- {}°PESSOA -----'.format(p))
    nome=str(input('Nome:')).strip()
    idade=int(input('Idade:'))
    sexo=str(input('Sexo[M/F]:')).strip()
    soma+=idade
    if p ==1 and sexo in 'Mm':
        maioridade=idade
        nomevelho=nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade=idade
        nomevelho=nome
    if sexo in 'Ff' and idade < 20:
        totm20+=1
print('A média de idade do grupo é de {} anos.'.format(soma/p))
print('O homem mais velho tem {} sendo de {}.'.format(maioridade,nomevelho))
print('Ao todo são {} com menos de 20 anos.'.format(totm20))
