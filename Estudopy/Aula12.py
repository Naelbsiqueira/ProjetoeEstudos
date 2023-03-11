#Condições aninhadas.
#As condições aninhadas utilizam estrutura das condições:
#if simples: Sempre será necessário para iniciar a estrutura condicionante.

#elif (senão se): Quantos forem necessário.
#elif (senão se): Quantos forem necessário.

#else (então). Estrutura opicional na forma de programar.

nome = str(input('Qual é o seu nome ?'))
if nome == 'Bernardo':
    print('Que belo nome!')
elif nome== 'Pedro' or nome == 'Maria' or nome=='Jose':
    print('Seu nome é muito popular')
else:
    print('Seu nome é tão normal.')
print('Tenha um Bom Dia, {}!'.format(nome ))