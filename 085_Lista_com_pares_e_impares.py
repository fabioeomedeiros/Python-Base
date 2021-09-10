#085_Lista_com_pares_e_impares.py

lista = [[], []]

while True:
    
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        lista[0].append(n)
    if n % 2 == 1:
        lista[1].append(n)
    esc = " "
    while esc not in "SN":
        esc = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]
    if esc == "N":
        break

print(lista)
print(sorted(lista[0]))
print(sorted(lista[1]))
