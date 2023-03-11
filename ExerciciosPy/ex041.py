from datetime import date
atual=date.today().year
ano=int(input("Ano de Nascimento:"))
idade=atual-ano
print('Idade atual é {} anos'.format(idade))
if idade<=9:
    print('Cassificação MIRIM.')
elif idade <=14:
    print('Classificação INFANTIL.')
elif idade <=19:
    print('Classificação JUNIOR.')
elif idade <=25:
    print('Classificação SÉNIOR.')
else:
    print('Classificação MASTER.')