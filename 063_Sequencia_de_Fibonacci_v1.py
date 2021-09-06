#063_Sequencia_de_Fibonacci.py

n = int(input("Número de termos? "))
t1 = 0
t2 = 1
print()
print(f"{t1} -> {t2}", end="")

j = 3
t3 = 0
while (j <= n):
    t3 = t2 + t1
    print(f" -> {t3}", end="")
    t1 = t2
    t2 = t3
    j += 1
print(" -> Fim")