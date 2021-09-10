#084_Lista_composta_e_analise_de_dados.py

pessoas = []
temp = [] #Lista temporária
maior = menor = 0

cont = 0
while True:

    nome = str(input("Nome: "))
    massa = float(input("Massa (kg): "))
    temp.insert(0, nome)
    temp.insert(1, massa)
    if len(pessoas) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]  
    pessoas.append(temp[:])
    temp.clear()

    esc = " "
    while esc not in "SN":
        esc = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]
        if esc == "N":
            break
    if esc == "N":
        break

print("")
print(pessoas)
print(f"A lista tem: {len(pessoas)} pessoas")
print("A(s) pessoas(s) mais pesadas são: ", end="")
for p in pessoas:
    if p[1] == maior:
        print(f"{p[0]} ", end="")
print(f"com {maior}kg")
print("A(s) pessoas(s) mais leves são: ", end="")
for p in pessoas:
    if p[1] == menor:
        print(f"{p[0]} ", end="")
print(f"com {menor}kg")
print("")
print("")
