#100_Funcao_pra_sortear_e_somar.py

def sorteia(x,lista):
    from random import randint
    for i in range(0,x):
        lista.append(randint(0,10))


def somapar(lista):
    soma = 0
    for v in lista:
        print(v)
        if v % 2 == 0:
            soma += v
    print(soma)

num = []
x = int(input("Quantos números que sortear? "))
sorteia(x, num)
print(num)
somapar(num)