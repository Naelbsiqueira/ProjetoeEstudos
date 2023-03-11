s=str(input("Informe seu sexo [M]/[F]:")).upper().strip()[0]
while s not in 'FfMm':
    s=str(input("ERRO!, Informe seu sexo [M]/[F]:")).upper().strip()[0]
if s=='F':
    print('O sexo escolhido foi {}.'.format(s))
elif s=='M':
    print('O sexo escolhido foi {}.'.format(s))
print('FIM')

