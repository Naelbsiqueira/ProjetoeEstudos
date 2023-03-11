time=list()
dados=dict()
partidas=list()
while True:
    dados.clear()
    dados['nome'] = str(input('Nome do jogador:')).upper()
    tot= int(input(f'Quantas partidas {dados["nome"]} jogou:'))
    partidas.clear()
    for c in range(0,tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}°?')))
    dados['gols'] = partidas[:]
    dados['total'] = sum(partidas)
    time.append(dados.copy())
    while True:
        resp=str(input('Quer continuar ?[S/N}')).upper().strip()[0]
        if resp in 'NS':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('=-'*30)
print('Cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for i, v in enumerate(time):
    print(f'{i:>1} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    busca= int(input('Mostrar dado de qual jogador?(999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Jogador inexistente {busca}!')
    else:
        print(f'-- Levantamento do Jogador {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('=-'*40)
print('<Finalizado> Volte Sempre!')
print(time)


