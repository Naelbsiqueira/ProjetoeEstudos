# Variáveis compostas #
# Dicionários *{}* São utilizado para referênciar os indices de forma literais (letras).
#Tuplas (); Imutáveis
#Lista []; Mutaveis
#Dicionários {}. Literais.

#dados=dict --> Umas das formas de utilizar Dicionários.
dados={'nome':'Pedro', 'sexo':'M','idade':25}
#dados['sexo']='F'
#print(dados['idade'])
#print(dados['nome'])
#print(dados['sexo'])
#del dados['idade'] Deletar indice !
#print(f'O { dados["nome"]} tem {dados["idade"]} anos') #É importante colocar em aspas duplas nesse caso.

#print(dados.keys()) # Nesse caso o valores mostrados são os índices.
#print(dados.values()) # Nesse caso os o valores mostrados são os dados em si ou dados específicos.
#print(dados.items()) Já nesse caso o valores mostrados são os valores os dois,
#tanto índices como os dados conti nos itens, que ~soa valores mais específicos.
#dados['nome']='Nael' # Nesse caso houve a troca dentro dos valores internos. ### Mutável ###.
dados['peso']= 73.3
for i, v in dados.items():
    print(f'{i} = {v}')



