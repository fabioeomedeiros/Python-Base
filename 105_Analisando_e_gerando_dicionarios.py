#105_Analisando_e_gerando_dicionarios.py

def notas(*n, sit=False):
    """
    -> Função para analisar as notas e a situação de uma turma.
    :n: Notas das turmas (aceita vários valores)
    :sit: (opcional) Exibe situação da turma baseada na média das notas
    :return: Dicionário com informações completas da turma
    """
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] < 4:
            r['sit'] = "Ruim"
        elif r['media'] < 7:
            r['sit'] = "Regular"
        else:
            r['sit'] = "Boa"
   
    return r


#PROGRAMA PRINCIPAL
# lista_de_notas = [5.5, 2.5, 9, 8,5]
resp = notas(5.5, 2.5, 5.1, sit=True)
print(resp)