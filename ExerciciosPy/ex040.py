n1=float(input('Primeira Nota:'))
n2=float(input('Segunda Nota:'))
media=(n1+n2)/2
print('Primeira nota {:.1f} + Segunda nota {:.1f} a média foi {:.1f}'.format(n1,n2,media))
if media>=7:
    print('\033[1;42mPARABÉNS !!!\033[m Você foi Aprovado! Nós vemos no próximo semestre.')
elif media>=5 and 7:
    print('\033[1;43mATENÇÃO !!!\033[m Estute mais, você está de recuperação.')
else:
    print('\033[1;41mREPROVADO!!!\033[m, Tente novamente no próximo semestre.')