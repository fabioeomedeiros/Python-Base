#108_Formatando_moedas.py

import moedas

p = float(input("Digite o preço R$"))
print(f"A metade de {moedas.moeda(p)} é {moedas.moeda(moedas.metade(p))}")
print(f"Dobro de {moedas.moeda(p)} é {moedas.moeda(moedas.dobro(p))}")
print(f"O aumento de {moedas.moeda(p)} é {moedas.moeda(moedas.aumentar(p,20))}")
print(f"A redução de {moedas.moeda(p)} é {moedas.moeda(moedas.diminuir(p,10))}")