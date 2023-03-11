from datetime import datetime
dados=dict()
dados['nome']=str(input('Nome:')).upper()
dados['ano']= int(input('Ano de Nascimento:'))
dados['carteira']=int(input('Carteira de Trabalho (0 não tem):'))
dados['idade'] = datetime.now().year - dados['ano']
if dados['carteira'] != 0:
    dados['contrato']=int(input('Ano de Contratação:'))
    dados['salário']=float(input('Salario: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contrato']+35)-datetime.now().year)
print('=-'*30)
for k,v in dados.items():
    print(f'- {k} tem o valor {v}')
print('=-'*30)
