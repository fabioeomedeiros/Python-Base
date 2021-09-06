#062_Super_progressao_aritimetica_v3.py

a1 = int(input("1º termo: "))
r = int(input("Razão: "))
n = int(input("Quantidade de termos: "))
# an = a1 + (n-1) * r
print()
j = 1
t = a1
mais = n
while (mais != 0):
    while (j <= n):
        print(f"{t} -> ", end="")
        t += r
        j += 1
    print("Pausa")
    mais = int(input("Quantos termos a mais? "))
    n += mais
print("FIM")
print(f"Foram mostrados {n} termos")
print()