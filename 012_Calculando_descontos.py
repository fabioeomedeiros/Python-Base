# 012_Calculando_descontos.py
# Calcula o desconto de um produto

print()
ajuste = (1-(float(input("Qual o desconto (%)? "))/100))
preco = float(input("Qual o preço do produto R$"))
print()
print(f"O peço com desconto é {preco*ajuste:.2f}")
