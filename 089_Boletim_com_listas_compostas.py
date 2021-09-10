#089_Boletim_com_listas_compostas.py

ficha = []

print("")
while True:

    nome = str(input("Nome: "))
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    media = (n1 + n2) / 2
    if media < 4:
        sit = "Reprovado"
    elif media < 7:
        sit = "Recuperação"
    else:
        sit = "Aprovado"
    ficha.append([nome, [n1, n2], media, sit])

    esc = " "
    while esc not in "SN":
        esc = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]

    if esc == "N":
        break

# print("")
# for i in range(0, len(ficha)):
#     print(ficha[i])
# print("")

print("")
ficha.sort()
print("="*35)
print(f"{'No.':<4}{'Nome:':<10}{'Média:':<10}{'Situação:':<11}")
print("-"*35)
for i in range(0, len(ficha)):
    print(f"{(i+1):<4}{ficha[i][0]:<10}{ficha[i][2]:<10.2f}{ficha[i][3]:<11}")
print("="*35)
print("")