# 032_Ano_bissexto.py
# Determina se o ano é ou não bissexto

from datetime import date

print()
ano = int(input("Digite o ano a ser analisado: "))
print()
if (ano == 0):
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0):
    print(f"O ano {ano} é bissexto")
else:
    print(f"O ano {ano} NÃO é bissexto")
print()
