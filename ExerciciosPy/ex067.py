while True:
    num = int(input('Digite um número para ver sua tabuada:'))
    if num < 0:
        break
    print('=' * 12)
    for c in range(1, 11):
        print('{} x {} = {}'.format(num, c, (c * num)))
    print('=' * 12)
print('Programa Tabuada Encerrado. Volte sempre !')





