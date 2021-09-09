#079_Valores_unicos_em_uma_lista.py

lista = []

print("")
while True:
    n = int(input("Adicione valor: "))
    if n not in lista:
        lista.append(n)
        print(f"Valor {n} adicionado com sucesso")
    else:
        print(f"Valor {n} duplicado NÃO adicionado")

    esc = " "
    while esc not in "SN":
        esc = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]
        if esc == "N":
            break
    if esc == "N":
        break
print("")
print(lista)
lista.sort()
print(lista)
print("")
