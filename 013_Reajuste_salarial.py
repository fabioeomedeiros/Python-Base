# 013_Reajuste_salarial.py
# Calcula o ajuste salarial de um funcionário e mostra o novo salário com x% de aumento

print()
reajuste = (1+(float(input("Entre com o reajuste (%): "))/100))
salario = float(input("Qual o salário? "))
novo_salario = salario*reajuste
print(f"O novo salário é R${novo_salario:.2f}")
print()
