#101_Funcoes_para_votacao.py

def voto():
    """
        -> Retorna situação de voto do usuário
        Entrada: Ano de nascimento
        return: situação
    """
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - int(input("Ano de nascimento: "))
    if idade < 16:
        return f"{idade} anos: Voto NEGADO"
    elif idade < 18 or idade > 65:
        return f"{idade} anos: Voto OPCIONAL"
    else:
        return f"{idade} anos: Voto OBRIGATÓRIO"

print(voto())
