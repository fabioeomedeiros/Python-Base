# 006 Dobro_triplo_raiz_quadrada.py
# Recebe um número e exibe na tela seu dobro, triplo e raiz quadrada

import math

print()
num = float(input("Entre com um número: "))
print(f"O dobro de {num} é {num*2}")
print(f"O triplo de {num} é {num*3}")
print(f"A raiz quadrada de {num} é {num**(1/2):.2f}")
print(f"A raiz quadrada de {num} é {pow(num, (1/2)):.2f}")
print(f"A raiz quadrada de {num} é {math.sqrt(num):.2f}")
print()