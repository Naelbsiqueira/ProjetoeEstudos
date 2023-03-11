from ex115.lib.arquivo import *
from time import sleep

arq='cursoemvideo.txt'

if not arqexiste(arq):
    criararquivo(arq)

cabecalho('MENU PRINCIPAL')

while True:
    resposta = menu(['Ver Pessoas Cadastradas','Cadastrar Nova Pessoa ','Sair do Sistema '])
    if resposta == 1:
        #opção de lista o conteúdo de um arguivo.
        lerarquivo(arq)
    elif resposta ==2:
        #opção cadastrar nova pessoas
        cabecalho('NOVO CADASTRO')
        nome=str(input('Nome:'))
        idade=leiaint("Idade:")
        cadastrar(arq, nome, idade)
    elif resposta==3:
        print('Saindo do sistema, Volte sempre !')
        break
    else:
        print('\033[0;031mERRO! Opção invalida.\033[m')
        sleep(2)
