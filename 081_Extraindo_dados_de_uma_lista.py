#081_Extraindo_dados_de_uma_lista.py

lista = []

while True:
    lista.append(int(input("Digite um número: ")))
    esc = " "
    while esc not in "SN":
        esc = str(input("Desja continuar [S/N]? ")).strip().upper()[0]
        if esc == "N":
            break
    if esc == "N":
        break

print(lista)
lista.sort(reverse=True)
print(f"A lista tem {len(lista)} valores")
print(lista)
if 5 in lista:
    print(f"O valor 5 está na lista na posisão {lista.index(5)}")
else:
    print("O valor 5 não está na lista")