# 031_Custo_da_viagem.py

print()
dist = float(input("Distância da viagem (km): "))
# if em bloco
# if (dist < 200):
#     preco = dist * 0.50
# else: 
#     preco = dist * 0.45
print()
# if in line
preco = dist * 0.50 if dist < 200 else dist * 0.45
print(f"O custo total de sua viagem será: R${preco:.2f}")
print()
