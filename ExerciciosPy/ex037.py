num=int(input("Digite um número inteiro:"))
print('\033[1;42mEscolha uma das bases para conversão:\033[m')
print('[1]converter para \033[1;44mBINÁRIO\033[m')
print('[2]converter para \033[1;44mOCTAL\033[m')
print('[3]converter para \033[1;44mHEXADECIMAL\033[m')
opção=int(input("Sua opção foi:"))
if opção==1:
    print("{} convertido para BINÁRIO é igual a {}".format(num,bin(num)[2:]))
elif opção ==2:
    print("{} convertido para OCTAL é igual a {}".format(num,oct(num)[2:]))
elif opção == 3:
    print("{} convertido para  HEXADECIMAL é igual a {}".format(num,hex(num)[2:]))
else:
    print('Opção invalidade, tente novamente')
