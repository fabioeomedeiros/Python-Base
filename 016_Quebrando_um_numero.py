# 016_Quebrando_um_numero.py
# Quebra e exibe um número em sua parte inteira e fracionária

from math import trunc

print()
num = float(input("Entre com um número: "))
#importando o método trunc da biblioteca math
print(f"A parte inteira de {num} é :{int(num)}")
print(f"A parte fracionária de {num} é :{(num - trunc(num)):.4f}")
print()
#usando a função interna int
print(f"A parte inteira de {num} é :{int(num)}")
print(f"A parte fracionária de {num} é :{(num - int(num)):.4f}")
print()
