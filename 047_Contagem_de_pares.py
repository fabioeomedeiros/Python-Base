#047_Contagem_de_pares.py

#contagem normal
inicio = int(input("Início da contagem: "))
fim = int(input("Fim da contagem: "))
passo = int(input("Passo da contagem: "))

# for i in range(inicio, fim+1, passo):
#     print(i)
# print("Acabou!")

#Contagem de pares
for i in range(inicio, fim+1, passo):
    print(".")
    if (i % 2 == 0):
        print(i)
