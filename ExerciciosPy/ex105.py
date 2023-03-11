def notas(*n, sit=False):
    """
    ->Função para analisar notas e situação de vários alunos.
    :param n: Uma ou mais notas de aluno {aceita várias}.
    :param sit:valor opcional, indica se deve ou não adicionar a situação.
    :return:Dicionário com várias informações sobre a situação da turma.
    """
    r=dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor']= min(n)
    r ['media']=sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] ='RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

#Programa principal
resp=notas (10,9,8, sit=True)
print(resp)
