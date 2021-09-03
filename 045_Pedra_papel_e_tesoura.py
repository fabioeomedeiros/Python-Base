#045_Pedra_papel_e_tesoura.py

from time import sleep
from random import randint

print("Pedra, Papel ou Tesoura?")
print('''[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

lista = ["PEDRA", "PAPEL", "TESOURA"]
c = randint(0, 2)
j = int(input("Sua escolha: "))

sleep(1)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
sleep(1)

print(f"Jogador: {lista[j]}")
print(f"Computador: {lista[c]}")

sleep(1)
if (c == 0):
    if (j == 0):
        print("Empate")
    elif (j == 1):
        print("Vitória")
    elif (j == 2):
        print("Derrota")
elif (c == 1):
    if (j == 1):
        print("Empate")
    elif (j == 2):
        print("Vitória")
    elif (j == 0):
        print("Derrota")
elif (c == 2):
    if (j == 2):
        print("Empate")
    elif (j == 0):
        print("Vitória")
    elif (j == 1):
        print("Derrota")
else:
    print("Jogada inválida")

