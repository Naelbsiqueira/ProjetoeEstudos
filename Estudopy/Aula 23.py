# TRATAMENTO DE ERRO E EXCEÇÕES.
# ERRO SINTÁTICO:
    #EX.: primt(x)
# ERRO SEMÁNTICO: não foi estabecido a variável para comando x.
    #EX.:print(x) NameError (exceção)
    #EX.: n=int(input('Número:'))
    #print(f'Você digitou o número {n}.')
    #Número:oito valueError (erro de Valor)
#try: #tente
#operação
#except: exceção
#falhou
try:
    p = int(input('Numerador:'))
    s = int(input('Denominador:'))
    r = p / s
except Exception as erro:
    print(f'Infelizmente tivemos um probelma! {erro.__class__}:(')
else:
    print(f'O resultado é {r:.1f}.')
finally:
    print(f'Volte sempre, muito obrigado.')