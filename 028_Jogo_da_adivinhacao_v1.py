# 028_Jogo_da_adivinhacao.py
# Adivinha número pensado pelo computador

from time import sleep
from random import randint

print()
com = randint(0,10)
num = int(input("Qual número o Computador pensou (0-10)? "))
print()
# sleep(3) #opcional
print(f"O número pensado foi: {com}")
if com == num:
    print("Parabéns!")
else:
    print("Errou!")
print()
