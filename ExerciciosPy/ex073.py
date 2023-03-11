times=('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
       'Atlético', 'Botafogo', 'Atlético-Pr', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife',
       'EC Vitória,', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-Go')
print('=-'*15)
for t in times:
       print(t)
print('=-'*15)
print(f'Os 4 primeiros são: {times[0:5]}')
print('=-'*15)
print(f'Os 4 últimos são: {times[-4:]}')
print('=-'*15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=-'*15)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}° posição')