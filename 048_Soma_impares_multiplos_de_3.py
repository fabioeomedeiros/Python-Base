#048_Soma_impares_multiplos_de_3.py

i = int(input("Início: "))
f = int(input("Fim: "))
s = int(input("Passo: "))

soma = 0
for c in range(i, f+1, s):
    if (c % 2 == 1 and c % 3 == 0):
        print(c)
        soma += c
print(soma)