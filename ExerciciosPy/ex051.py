primeiro=int(input("Primeiro Termo:"))
razão=int(input("Razão:"))
décimo = primeiro+(11-1)*razão
for c in range (primeiro,décimo,razão):
    print('{}'.format(c), end= ' → ' )
print('Acabou')