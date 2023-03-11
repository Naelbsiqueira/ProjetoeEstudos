galera=list()
pessoa=dict()
cont=soma = media=0
while True:
    pessoa.clear()
    cont+=1
    pessoa['nome'] = str(input("Nome:"))
    pessoa['idade'] = int(input("Idade:"))
    soma+= pessoa["idade"]
    while True:
        pessoa['sexo'] = str(input("Sexo:[M/F]")).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! por favor, digite apenas M ou F.')
        pessoa['sexo'] = str(input("Sexo:[M/F]")).upper()[0]
    galera.append(pessoa.copy())
    opc = str(input('Quer continuar? [S/N]')).upper()[0]
    while opc not in 'NnSs':
        opc=str(input('Erro, Responda apenas [S/N]?')).upper()[0]
    if opc in 'Nn':
        break
print('=-'*30)
print(f'A) Ao todo temos {cont} pessoas cadastradas. ')
media=soma/cont
print(f'B) A média de idade é {media:.0f} anos.')
print(f'C) As mulheres cadastradas foram' , end=' ')
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ' , end='')
print()
print(f'D) lista de pessoas acima da média', end='')
for p in galera:
    if p["idade"] >= media:
        print('  ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print("<<ENCERRADO>>")
print('=-'*30)

