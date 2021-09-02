# 023_Separando_digitos_de_um_numero.py
# Recebe um número e reescreve separando milhar, centena, dezena e unidade

print()
num = int(input("Informe um número (0-9999): "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print()
print(f"M: {m*1000:>4}")
print(f"C: {c*100:>4}")
print(f"D: {d*10:>4}")
print(f"U: {u:>4}")
print("   ----")
print(f"{num:>7}")
print()
