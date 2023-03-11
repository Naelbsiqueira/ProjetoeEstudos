from math import hypot
co=float(input("Digite o cateto oposto:"))
ca=float(input("Digite o cateto adjacente:"))
print("O Cateto oposto é {}\nO Cateto adjacente {}\nA hipotenusa {:.1f} ".format(co,ca,hypot(co,ca)))