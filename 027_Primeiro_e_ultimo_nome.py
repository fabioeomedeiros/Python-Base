# 027_Primeiro_e_ultimo_nome.py
# Recebe um nome completo e escreve o primeiro e ultimo

print()
nome = str(input("Escreva seu nome completo: ")).strip()
lista_nome = nome.split()
print()
print(f"Olá {lista_nome[0]} {lista_nome[-1]}, tudo bem?")
print()
