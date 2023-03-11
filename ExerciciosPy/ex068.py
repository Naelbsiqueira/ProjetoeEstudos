from random import randint
print('='*25)
print('VAMOS JOGAR PAR OU IMPAR')
print('='*25)
v=0
while True:
    jogador=int(input("Digite um valor:"))
    comp = randint(0, 10)
    total=jogador+comp
    tipo=' '
    while tipo not in 'PI':
        tipo = str(input('PAR ou IMPAR? [P/I}')).upper().split()[0]
    print(f"Você Jogou {jogador} e o Computador Jogou {comp}. Total {total}, ", end=' ')
    print('Deu PAR' if total%2==0 else'Deu IMPAR')
    if tipo=='P':
        if total%2==0:
            print(("Você GANHOU"))
            v+=1
        else:
            print('Voce PERDEU')
            break
    elif tipo =='I':
        if total%2==1:
            print("Você Ganhou")
            v+=1
        else:
            print('Você PERDEU')
    print('Vamos jogar novamente ...')
print(f'GAME OVER! Você venceu {v} vezes')