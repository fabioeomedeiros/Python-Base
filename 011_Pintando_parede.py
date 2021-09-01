# 011_Pintando_parede.py
# Recebe altura e largura de uma parede, calcula quantos litros de tinta são necessários e exibe quantas latas de tinta serão compradas
# 1 litro de tinta pinta 2m²
# 1 lata tem 3,6 litros de tinta

from math import ceil

print()
A = float(input("Altura (m): "))
L = float(input("Largura (m): "))
area = A * L
qtd_latas = area / 2
print(f"Área: {area:.1f} m2")
print(f"Quantidade de latas: {ceil(qtd_latas)} uni")
