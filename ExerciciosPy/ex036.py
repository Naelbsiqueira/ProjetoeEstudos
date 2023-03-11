ca=float(input("Qual o valor da casa?"))
sal=float(input("O salario atual?"))
an=int(input("Quanto anos de pagamento?"))
pre=ca/(an*12)
min=sal*30/100
print('Para pagar uma casa de R${:.2f} em {} anos,a prestação será de R${:.2f}'.format(ca,an,pre))
if pre<= min:
    print('=-=-='*15)
    print('Parabéns! O seu empréstimo foi \033[32mAPROVADO!\033[m\nO valor das parcelas é de R${:.2f}, '
          'e serão pagas em {:.0f} meses.'.format(pre, an))
    print('\033[1;41mObrigado por usar o nosso sistema!\033[m\nVolte sempre!\033[m')
elif pre> min:
    print('=-=-=' * 20)
    print('Infelizmente o seu empréstimo foi \033[31mNEGADO.\033[m\nO valor da sua prestação (R${:.2f}), '
          'excede 30% do seu salário. R$({:.2f})'.format(pre, min))
    print('\033[1;41mObrigado por usar o nosso sistema!\033[m\nVolte sempre!')

