def notas(*n,sit=False):
    """
    ->função para analisar a situação de um aluno
    :param n: uma ou mais notas de um aluno (aceita varias)
    :param sit: valor opicional , se deve ou não adicionar a situação do aluno
    :return: dicionario com varias informaçães sobre a turma
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if  r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOAVEL'
        else:
            r['situação'] = 'RUIM'
    return r


#programa principal
resp = notas(6.5,9,8.5,10,sit=True)
print(resp)
help(notas)
