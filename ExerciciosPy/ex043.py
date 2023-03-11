from time import sleep
peso= float(input('Qual o seu peso? (KG)'))
altura=float(input('Qual sua altura?(M)'))
imc=peso/(altura**2)
print('\033[1;31mCalculando...\033[m')
sleep(3)
print('Seu IMC está em {:.1f}'.format(imc))
if imc < 18.5:
    print('\033[1;41mAtenção !!!\033[m Abaixo do peso ideal, Coma mais!')
elif 18 <= imc < 25 :
    print('\033[1;42mPARABENS!!!\033[m Peso ideal.')
elif 25 <= imc <30:
    print('\033[1;43mATENÇÃO!!!\033[m Sobrepeso, Pratique atividade Física!')
elif 30 <= imc <40:
    print('\033[1;41mCUIDADO!!!\033[m Obesidade, Sua saúde corre perigo!')
else:
    print('\033[1;41mPERIGO!!!\033[m Obesidade morbida, você está em risco de vida, procure um médico!')