#070_Estatistica_em_produtos.py

i = total = totmil = mprec = 0
mprod = " "

print()
while True:

    produto = str(input("Produto: "))
    preco = float(input("Preço: R$"))

    total += preco

    if preco >= 1000:
        totmil += 1

    if i == 1 or preco < mprec:
        mprec = preco
        mprod = produto

    i += 1

    esc = " "
    while esc not in "SN":
        esc = str(input("Deseja continuar [s/n]? ")).strip().upper()[0]
    if esc == "N":
        break

print()
print(f"Total das compras R${total}")
print(f"{totmil} produto(s) custa(am) mais de R$1000,00")
print(f"O produto mais barato é {mprod} e custa R${mprec:.2f}")
print()