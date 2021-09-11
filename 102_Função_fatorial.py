#102_Função_fatorial.py

def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: Número a ser calculado.
    :param show: (opcional) Mosta a conta passo a passo.
    :return: Retorna o valor do fatorial de n.
    """
    f = 1
    for i in range(n, 0, -1):
        f *= i
    if show:
        print(f"{n}! = ", end="")
        for i in range(n, 0, -1):
            print(f"{i}", end="")
            if i > 1:
                print(" x ", end="")
            else:
                print(" = ", end="")
        f *= i
    return f

print(fatorial(5, show=True))
# help(fatorial)