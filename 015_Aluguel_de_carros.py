# 015_Aluguel_de_carros.py
# Calcula o valor total do aluguel de carros
# R$60,00/dia alugado + R$0,15/km rodado

print()
dias = float(input("Quantos dias? "))
km = float(input("Quantos quilometros? "))
print()
preco_tot = dias*60 + km*0.15
print(f"O preço total é R${preco_tot:.2f}")
print()
