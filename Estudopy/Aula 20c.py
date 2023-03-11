def dobra(lst):
    pos=0
    while pos < len(lst):
        lst[pos] *= 2
        pos+=1

valores=[7,2,5,6,4,8]
dobra(valores)
print(f'{valores}')