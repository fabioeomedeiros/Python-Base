# 034_Aumentos_multiplos.py

print()
salario = float(input("Salário atual: R$"))
print()
# if (salario <= 1250):
#     salario *= 1.15 # -> salario = salario * 1.15
# else:
#     salario *= 1.10 # -> salario = salario * 1.10

salario = salario * 1.15 if salario<= 1250 else salario * 1.10

print(f"Seu novo salário será: {salario:.2f}")
print()
