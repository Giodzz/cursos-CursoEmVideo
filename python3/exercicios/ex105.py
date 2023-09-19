def notas(*varias_notas, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param varias_notas: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    dados = dict()
    dados['total'] = len(varias_notas)
    dados['maior'] = max(varias_notas)
    dados['menor'] = min(varias_notas)
    dados['media'] = sum(varias_notas) / dados['total']

    if sit:
        if dados['media'] < 5:
            dados['situação'] = 'RUIM'
        elif dados['media'] < 7:
            dados['situação'] = 'RAZOÁVEL'
        else:
            dados['situação'] = 'BOA'
    return dados


# Programa Principal
resp = notas(5.5, 9.5, 10, 6.5)
print(resp)
