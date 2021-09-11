#098_Funcao_de_contador.py

def contador(i,f, s):
    for j in range(1, 11, 1):
        print(f"{j} ", end="")
    print("")
    for j in range(10, -1, -2):
        print(f"{j} ", end="")
    print("")
    for j in range(i, f, s):
        print(f"{j} ", end="")
    print("")

i = int(input("Início: "))
f = int(input("Fim: "))
s = int(input("Passo: "))
contador(i, f, s)