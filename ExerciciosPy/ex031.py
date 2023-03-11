dis=float(input("Qual a distância da viagem em KM ?"))
if dis >200:
    print('Valor da viagem {:.1f}R$'.format(dis*0.45))
else:
    print ('Valor da viagem {:.1f}R$'.format(dis*0.5))

