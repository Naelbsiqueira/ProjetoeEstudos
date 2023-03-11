from math import radians,sin,cos,tan
ângulo=float(input("Digite um angulo:"))
sen = sin(radians(ângulo))
cos = cos(radians(ângulo))
tan = tan(radians(ângulo))
print("O ângulo de {:.0f} tem como seno {:.2f}.".format(ângulo,sen))
print ("O ângulo de {:.0f} tem como cosseno {:.2f}.".format(ângulo,cos))
print("O ângulo de {:.0f} tem como tangente {:.2f}.".format(ângulo,tan))