dados=dict()
partidas=list()
dados['nome'] = str(input('Nome do jogador:')).upper()
tot= int(input(f'Quantas partidas {dados["nome"]} jogou:'))
for c in range(0,tot):
    partidas.append(int(input(f'Quantos gols na partida {c+1}°?')))
dados['gols']=partidas[:]
dados['total']=sum(partidas)
print('=-'*30)
print(dados)
print('=-'*30)
for k, i in dados.items():
    print(f'O campo {k} tem o valor {i}.')
print('=-'*30)
print(f'O jogador {dados["nome"]}  jogou {tot} partidas')
for i, v in enumerate(dados['gols']):
    print(f'    => Na {i+1}° partida fez {v} gols')
print(f'Foi um total de {dados["total"]} partidas')

