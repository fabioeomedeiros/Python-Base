#107_Exercitando_modulos_em_python.py

import moedas

p = float(input("Digite o preço R$"))
print(f"A metade de {p} é {moedas.metade(p):.2f}")
print(f"Dobro de {p} é {moedas.dobro(p):.2f}")
print(f"O aumento de {p} é {moedas.aumentar(p,20):.2f}")
print(f"A redução de {p} é {moedas.diminuir(p,10):.2f}")