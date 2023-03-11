estado=dict()
brasil=list()
for c in range(0,3):
    estado ['uf']=str(input("Unidade Federativa:")).upper()
    estado ['sigla']=str(input('Sigla do Estado:')).upper()
    brasil.append(estado.copy()) # Método útilizado para copiar dicionários e adicionar em listas !!
for e in brasil:
    for k, v in e.items():
        print(f'{k} = {v}.')