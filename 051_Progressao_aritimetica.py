#051_Progressao_aritimetica.py

p = int(input("1º termo: "))
r = int(input("Razão: "))
qtd_t = int(input("Quantidade de termos: "))
u = p + (qtd_t - 1) * r

for i in range(p, u+r, r):
    print(i)