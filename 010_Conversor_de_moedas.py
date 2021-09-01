# 010_Conversor_de_moedas.py
# Recebe um valor em R$ e converte em US$

print()
real = float(input("Entre com o valor em Reais: R$"))
dolar = real/5.17 #cotação no dia 2021-09-01
print(f"Com R${real:.2f} você pode comprar US${dolar:.2f}")
print()
