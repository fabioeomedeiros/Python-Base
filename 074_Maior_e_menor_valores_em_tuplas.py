#074_Maior_e_menor_valores_em_tuplas.py

from random import randint

num = (randint(0,5), randint(0,5), randint(0,5), randint(0,5), randint(0,5),)
print(num)
print(f"Maior: {max(num)}")
print(f"Menor: {min(num)}")