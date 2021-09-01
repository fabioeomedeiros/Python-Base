# 019_Sorteando_um_item.py
# Sorteia um item em uma lista

import random

print()
n1 = str(input("1º aluno: "))
n2 = str(input("2º aluno: "))
n3 = str(input("3º aluno: "))
n4 = str(input("4º aluno: "))
n5 = str(input("5º aluno: "))
print()
lista = [n1, n2, n3, n4, n5]
escolhido = random.choice(lista)
print(f"O aluno escolhido foi {escolhido}")
print()
