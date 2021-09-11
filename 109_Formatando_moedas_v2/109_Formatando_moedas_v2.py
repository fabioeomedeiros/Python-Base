#108_Formatando_moedas.py

import moedas

p = float(input("Digite o preço R$"))
print(f"A metade de {moedas.moeda(p)} é {moedas.metade(p, True)}")
print(f"Dobro de {moedas.moeda(p)} é {moedas.dobro(p, True)}")
print(f"O aumento de {moedas.moeda(p)} é {moedas.aumentar(p,20, True)}")
print(f"A redução de {moedas.moeda(p)} é {moedas.diminuir(p,10, True)}")