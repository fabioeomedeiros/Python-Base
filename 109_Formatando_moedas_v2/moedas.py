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