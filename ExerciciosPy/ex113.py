def leiaInt(msg):
    while True:
        try:
            n=int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;031mERRO! Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[0:031mEntrada de dados interropida pelo usuário.\033[m')
            return 0
        else:
            return n
def leiafloat(msg):
    while True:
        try:
            n=float(input(msg))
        except (ValueError,IndexError, TypeError):
            print('\033[0;031mERRO! Digite um número inteiro válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[0:031mEntrada de dados interropida pelo usuário.\033[m')
            return 0
        else:
            return n

#Programa principal
n=leiaInt('Digite um número Inteiro:')
n2=leiafloat('Digite um número Real:')
print(f'Número Inteiro digitado foi {n} e o Real {n2} ')
