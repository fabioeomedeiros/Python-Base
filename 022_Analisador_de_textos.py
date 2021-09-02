# 022_Analisador_de_textos.py
# Recebe o nome do usuário e o analiza por completo

print()
nome = str(input("Digite seu nome completo: ")).strip()
nome_list = nome.split(" ")
print()
print(f"Olá {nome_list[0]} {nome_list[-1]},")
print(nome.upper())
print(nome.lower())
print(f"Seu nome tem {len(nome)-nome.count(' ')} letras")
print()
