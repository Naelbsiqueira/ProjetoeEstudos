from time import sleep
def contador(i,f, p):
    if p <0:
        p*=-1
    if p ==0:
        p=1
    print('~'*30)
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    print('~'*30)
    sleep(2.5)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            cont+=p
            sleep(0.2)
        print('FIM!')
    else:
        cont=i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.2)
            cont-=p
        print('FIM!')
#Programa Principal
contador(1,10,1)
contador(10,0,2)
print(f'Agora é sua vez de personalizar a contagem')
ini=int(input('Início:'))
fim=int(input('Fim:'))
pas=int(input('Passo:'))
contador(ini,fim,pas)