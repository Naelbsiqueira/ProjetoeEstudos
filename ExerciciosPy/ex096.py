def area(larg,comp):
    a=larg*comp
    print(f'A area de um terreno {larg} X {comp} é de {a}m²')

#PROGRAMA PRINCIPAL
print('CONTROLE DE TERRENOS ')
print('-='*10)
l = float(input('LARGURA (m):'))
c = float(input('COMPRIMENTO (m):'))
area(l,c)
