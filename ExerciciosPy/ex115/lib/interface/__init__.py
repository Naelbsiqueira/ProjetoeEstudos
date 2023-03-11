def leiaint(msg):
    while True:
            try:
                n = int(input(msg))
            except (ValueError, TypeError):
                print('\033[0;031mERRO! Digite um número inteiro válido.\033[m')
                continue
            except (KeyboardInterrupt):
                print('\n\033[0:031mEntrada de dados interropida pelo usuário.\033[m')
                return 0
            else:
                return n

def linha(tam=42):
    return '='*tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lst):
    c=1
    for i in lst:
        print(f'{c} - {i}')
        c+=1
    print(linha())
    opc=leiaint('Sua opção:')
    return opc
