#052_Numeros_primos.py

num = int(input("Entre com o Número: "))
tot = 0

for i in range (1, num+1):
    if (num % i == 0):
        print(f"({i})")
        tot += 1
    else:
        print(i)

if (tot == 2 or num == 1):
    print(f"{num} é Primo")
else:
    print(f"{num} NÃO é Primo e foi dividido {tot} vezes")
    