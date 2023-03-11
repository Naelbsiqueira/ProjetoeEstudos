n1=int(input('Digite um valor:'))
n2=int(input('Digite outro valor:'))
s=n1+n2
m=n1*n2
x=n1**n2
d=n1/n2
di=n1//n2
r=n1%n2
print ('A soma é: {}\n O produto: {}\n Exponeciação é : {}\n A divisaõ é : {:.8f}\n '.format(s,m,x,d),end=' ')
print ('A divisão inteira é :{}\n Resto da divisão é:{}'.format(di,r))