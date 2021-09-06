#071_Simulador_de_caixa_eletronico.py

print()
print("=" * 34)
print("{:^30}".format("BANCO LabCrEs"))
print("=" * 34)
valor = int(input("Valor a ser sacado: R$"))
print("-" * 34)

total = valor
ced = 100
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f"Total de {totced} cédulas de R${ced:.2f}")
        if ced == 100:
            ced =50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        totced = 0
        if total == 0:
            break

print("=" * 34)
print()