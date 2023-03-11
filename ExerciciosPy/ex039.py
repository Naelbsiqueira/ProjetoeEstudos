from datetime import date
atual=date.today().year
nasc=int(input('Ano de Nascimento:'))
idade = atual-nasc
print('Quem nasceu em {}, tem {} anos, em {}.'.format(nasc,idade,atual))
if idade == 18:
    print('Você tem que se alistar \033[1;46mIMEDIATAMENTE!\033[m')
elif idade >18:
    print('Você já deveria ter se alistado há {} anos'.format(idade-18))
elif idade < 18:
    print('\033[1;41mAguarde !\033[m seu alistamento será daqui há {} anos'.format(18-idade))