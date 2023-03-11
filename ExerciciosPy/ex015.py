D=int(input(('Quantos dias alugados:')))
K=float(input('Quanto Km rodados:'))
C=(D * 60 ) + (K * 0.15)
print('Valor a pagar{:.2f}R$'.format(C))