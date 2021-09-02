# 026_Primeira_e_ultima_ocorrencia.py
# Programa que recebe uma frase e exibe quantas vezes ela aparece, onde ela aparece pela primeira e última vez

print()
frase = str(input("Escreva uma frase: ")).strip().lower()
print()
print(f"A letra 'A' aparece {frase.count('a')} vezes")
print(f"A letra 'A' aparece pela 1ª vez na posição {frase.find('a')+1}")
print(f"A letra 'A' aparece pela última vez na posição {frase.rfind('a')+1}")
print()
