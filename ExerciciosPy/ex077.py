palavra=('APRENDER', 'PROGRAMAR',
   'LINGUAGEM', 'PYTHON',
   'CURSO', 'GRATIS',
   'ESTUDAR', 'PRATICAR','TRABALHAR',
   'MERCADO', 'PROGRAMAR', 'FUTURO')
for p in palavra:
    print (f'\nNa palavra {p} temos', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')