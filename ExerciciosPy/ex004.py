x=input('Digite algo:')
print('O tipo primitivo desse arquivo é:',type(x))
print('Só tem espaço ?',x.isspace())
print('É númerico ?',x.isnumeric())
print('é alfabético ?',x.isalpha())
print('É alfanúmerico ?', x.isalnum())
print('Está em maiusculas?', x.isupper())
print('Está em minúculas?',x.islower())
print ("Está capitalizada?", x.istitle())
