def moeda(preco=0, moeda='R$', format=False):
    return f"{moeda}{preco:.2f}".replace(".", ",")

def aumentar(preco=0, taxa=0, format=False):
    resp = preco + (preco * taxa/100)
    return resp if format == False else moeda(resp)

def diminuir(preco=0, taxa=0, format=False):
    resp = preco - (preco * taxa/100)
    return resp if format == False else moeda(resp)

def dobro(preco=0, format=False):
    resp = preco * 2
    return  resp if format == False else moeda(resp)

def metade(preco=0, format=False):
    resp = preco / 2
    return  resp if format == False else moeda(resp)

def resumo(preco=0, taxaa=10, taxar=10):
    print("=" * 35)
    print("RESUMO DO VALOR".center(30))
    print("=" * 35)
    print(f"Valor analisado: \t{moeda(preco)}")
    print(f"Dobro do preço: \t{dobro(preco, True)}")
    print(f"Metade do preço: \t{metade(preco, True)}")
    print(f"Aumento de {taxaa}%: \t{aumentar(preco, taxaa, True)}")
    print(f"Redução de {taxar}%: \t{diminuir(preco, taxar, True)}")
    print("=" * 35)