#076_Lista_de_precos_com_tupla.py

listagem = ("Lápis", 1.75,
            "Borracha", 2.00,
            "Caderno", 15.90,
            "Estojo", 25.00,
            "Transferidor", 4.20,
            "Compasso", 9.99,
            "Mochila", 120.30,
            "Caneta", 1.50,
            "Livro", 34.90)

print("="*30)
print(f"{'LISTA DE COMPRAS':^30}")
print("="*30)
for i in range(0, len(listagem)):
    if i % 2 == 0:
        print(f"{listagem[i]:.<21}", end="")
    else:
        print(f"R${listagem[i]:>7.2f}")
print("="*30)