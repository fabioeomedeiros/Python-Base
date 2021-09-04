#060_Calculo_fatorial.py
#Calcula função fatorial através de biblioteca
#loop FOR e loop WHILE

from math import factorial

num = int(input("Entre com o número: "))
print()

ff = 1
print(f"{num}! = ", end="")
for i in range(num, 0 ,-1):
    print(f"{i}", end="")
    print(" x " if i > 1 else " = ", end="")
    ff *= i
print(ff)

fw = 1
j = num
print(f"{j}! = ", end="")
while j >= 1:
    print(f"{j}", end="")
    print(" x " if j > 1 else " = ", end="")
    fw *= j
    j -= 1
print(fw)

print(f"{num}! = {factorial(num)}")
