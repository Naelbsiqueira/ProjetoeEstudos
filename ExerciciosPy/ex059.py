from time import sleep
n1=int(input('Digite o primeiro valor:'))
n2=int(input('Digite o segundo valor:'))
opcao = 0
print('=-='*10)
while opcao != 5:
    s=print('[1] somar')
    m=print('[2] mutiplicar')
    maior=print('[3] maior')
    n=print('[4] novos números')
    sair=print('[5] sair do programa')
    opcao=int(input('>>>>> Qual é sua opção ?'))
    print('=-=' * 10)
    if opcao == 1:
        print('A soma é igual a {}'.format(n1+n2))
    elif opcao ==2:
        print('A soma é igual a {}'.format(n1*n2))
    elif opcao ==3:
        if n1>n2:
            print('O maior é {}'.format(n1))
        elif n2>n1:
            print('O maior é {}'.format(n2))
        else:
            print('Ambos são igual')
    elif opcao ==4:
        print('informe o números novamente:')
        n1 = int(input('Digite o primeiro valor:'))
        n2 = int(input('Digite o segundo valor:'))
    elif opcao == 5:
        print('Finalizando...')
        sleep(3)
    else:
        print('Opção invalida, tente novamente:')
    print('=-='*10)
print('Fim do programa! volte sempre.')
