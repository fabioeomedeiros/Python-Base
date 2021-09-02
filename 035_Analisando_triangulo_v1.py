# 035_Ano_bissexto.py

print()
print("Quais os lados do triângulo?")
l1 = float(input("1º seguimento: "))
l2 = float(input("2º seguimento: "))
l3 = float(input("3º seguimento: "))
print()
if (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l1 + l2):
    print("Formam triangulo")
else:
    print("Não formam triângulo")
print()

# Possibilidade in-line 
# print("Formam triângulo" if ((l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l1 + l2)) else "Não formam triângulo")
