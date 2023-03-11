# tratando cadeias de caracteres (testo, ou stringer)
frase = 'Curso em Video Python'
#print (frase)
    # ex.: Curso em Video Python.

    ### FATIAMENTO ###

#print(frase[9]) indica a nona letra da stringer;
    #ex.: [V].

#print (frase[9:13]);
    #ex.:[Vide].

#print (frase [9:21]);
    #ex.: [Video Python].

#print(frase[9::]) indica o início da stringer até o final dela;
    #ex.:  [Video `Python].

#print(frase[1:15:2]) indica a segunda letra até decima quinta, pulando de 2 em 2 letras;
    #ex.:[us mVdo P].

    ### ANALISE ###

#print(len(frase)) demonstra quantas letras há na stringer;
    #ex.: [21].

#print(frase.count('o')) #contar quantas vezes exite a letra ´o´ na frase (stringer);
    #ex.:[3].

#print(frase.count('o',0,13)#contar quantas vezes a letra 'o' aparece na frase do início até a ""13"" no caso 12.
    #ex.:[1].

#print('Curso' in frase) Demonstra valores verdadeiro ou falsos (True or False);
    #ex.: true

#print(frase.find('Curso')) Quanto a palavra se inicia;

#print(frase.split()) divide a frase

### TRANSFORMAÇÃO ###

#print(frase.replace('Python', 'Android')) altera o nome da variável, vale ressaltar que variárias são imutaveis.
    #ex.: Curso em Video Android.

#print(frase.upper()) altera todas a letras para maiúculas;
    #ex.: CURSO EM VIDEO PYTHON.

#print(frase.lower()) altera todas as letras para minúsculas;
    #ex.: curso em vídeo python.

#print(frase.capitalize()) altera toda frase para minúsculo, depois deixa a primeira
# letra da primeira palavra em maiúculo;
    #ex.: Curso em video em python.

#print(frase.title()) transforma toda primeira letra de cada palavra em maiúsculo;
    #ex.: Curso Em Vídeo Python.

#print(frase.strip()) remove espaço vazios no inicio e no final;
    #ex.:XXXCurso em Vídeo PythonXX

##print(frase.rstrip()) remove espaço vazios à direita;
    #ex.:Curso em Vídeo PythonXX

#print(frase.lstrip()) remove espaço vazios à esqueda;
    #ex.:XXXCurso em Vídeo Python

    ### DIVISÃo ###

#print(frase.split()) divião em espaço.
    #ex.:Curso|em|Video|Python
        #01234 01 01234 012345
        #0      1   2     3

    ###Junção ###

#print('-'.join(frase)) Junção/união da frase com '-'
    #ex.: C-u-r-s-o-e-m-V-i-d-e-o-P-y-t-h-o-n


