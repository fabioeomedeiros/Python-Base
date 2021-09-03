#050_Soma_dos_pares.py

soma = 0
for c in range(1, 6):
    num = int(input(f"{c}º Número: "))
    if (num % 2 == 0):
        soma += num
print (f"Soma = {soma}")