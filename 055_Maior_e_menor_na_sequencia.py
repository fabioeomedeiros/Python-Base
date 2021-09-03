#055_Maior_e_menor_na_sequencia.py

list_m = []

maior = 0
menor = 0

for i in range(1, 6):
    m = float(input(f"{i}ª Massa (kg): "))
    list_m.append(m)
    if (i == 1):
        maior = m
        menor = m
    else:
        if (m > maior):
            maior = m
        if (m < menor):
            menor = m

print(list_m)
print(maior)
print(menor)