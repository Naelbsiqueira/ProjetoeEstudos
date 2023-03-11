from time import sleep
c = ('\033[m',        # 0 - Sem Cores;
   '\033[0;30;41m', # 1 - Vemelho;
   '\033[0;30;42m', # 2 - Verde;
   '\033[0;30;43m', # 3 - Amarela;
   '\033[0;30;44m', # 4 - Azul
   '\033[0;30;45m', # 5 - Roxo;
   '\033[7;30m'     # 6 - Branco
   );

def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'',4)
    print(c[5], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def título(msg, cor=0):
    tam=len(msg)+4
    print(c[cor], end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(c[0], end='')
    sleep(1)

#Programa Principal.
comando=''
while True:
    título('Sistema de Ajuda PyHelp',2)
    comando=str(input("Função ou Biblioteca>"))
    if comando.upper() =='FIM':
        break
    else:
        ajuda(comando)
título('Até Logo',1)
