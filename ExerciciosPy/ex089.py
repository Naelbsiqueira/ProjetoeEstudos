aluno=dict()
aluno['nome']=str(input('Nome:')).upper()
aluno['media']=float(input(f'Média de {aluno["nome"]}:'))
if aluno['media'] >= 7:
    aluno['Situação'] ='Aprovado '
elif 5 <= aluno['media'] < 7:
    aluno ['Situação'] = 'Recupeção'
else:
    aluno ['Situação'] =  'Reprovado'
print('=-'*30)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
#print(f'- O nome é {aluno["nome"]}.')
#print(f'- A média é igual {aluno["media"]}.')
#print(f'- A sitação é igual a {aluno["Situação"]}.')
print('=-'*30)
