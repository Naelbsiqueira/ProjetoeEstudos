def factorial(n, show=False):
    """
    --> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show:(Opcional) Motrar ou não a conta.
    :return:O valor do fatorial de um número n.
    """


    print('~'*25)
    f=1
    for c in range(n,1,-1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

#Programa principal:
#print(factorial(5,show=True))
help(factorial)