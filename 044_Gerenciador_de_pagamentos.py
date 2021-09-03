#044_Gerenciador_de_pagamentos.py

preco = float(input("Preço do produto: R$"))

print('''Escolha a condição de pagamento:
[ 1 ] Á vista (espécie/débito)
[ 2 ] À vista (crédito)
[ 3 ] 2x no cartão
[ 4 ] 3x no cartão''')
op = int(input("----> "))

if (op == 1):
    print(f"10% de desconto -> Novo preço: R${(preco * 0.9):.2f}")
elif (op == 2):
    print(f"5% de desconto -> Novo preço: R${(preco * 0.95):.2f}")
elif (op == 3):
    print(f"2 parcelas de R${(preco / 2):.2f}")
elif (op == 4):
    print(f"3 parcelas de R${(preco*1.2 / 3):.2f}")
else:
    print("OPÇÃO INVÁLIDA SEU BURRO!")