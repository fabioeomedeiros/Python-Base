# 017_Calculando_hipotenusa.py
# Recebe o valor do cateto oposto e do cateto adjacente e calcula a calculando a hipotenusa

import math

print()
co = float(input("Cateto oposto: "))
ca = float(input("Cateto adjacente: "))
print()
#usando operadores internos
h = (co**2 + ca**2)**(1/2)
print(f"Hipotenusa: {h}")
#usando a biblioteca math
print()
print(f"Hipotenusa: {math.hypot(co, ca)}")
print()
