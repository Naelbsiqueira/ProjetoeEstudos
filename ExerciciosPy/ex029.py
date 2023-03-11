vel=float(input('Velocidade:'))
if vel > 80:
    print("Atenção ! Voce foi multado, execedeu o limite permitido.")
    mul = (vel - 80) * 7
    print('valor a pagar {}R$'.format(mul))
else:
    print(f"Parabéns, você está na velocidade da via, há {vel}k/h")
