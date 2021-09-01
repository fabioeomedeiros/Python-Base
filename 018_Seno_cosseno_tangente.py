# 018_Seno_cosseno_tangente.py
# Calcula e exibe seno, cosseno e tangente de angulo recebido pelo usuário

import math

print()
ang = math.radians(float(input("Entre com um angulo: ")))
print(f"sin({ang:.2f}) = {math.sin(ang):.2f}")
print(f"cos({ang:.2f}) = {math.cos(ang):.2f}")
print(f"tan({ang:.2f}) = {math.tan(ang):.2f}")
print()
