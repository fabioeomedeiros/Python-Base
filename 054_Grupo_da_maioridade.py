#054_Grupo_da_maioridade.py

from datetime import date

lista_nasc = []
lista_idade = []
ano = date.today().year
menor = 0
maior = 0

for i in range(1, 6):
    nasc = int(input(f"Ano de nascimento da {i}ª pessoa: "))
    idade = ano - nasc
    lista_nasc.append(nasc)
    lista_idade.append(idade)
    if (idade < 18):
        menor += 1
    else:
        maior += 1

for i in range(1, 6):
    print(f"{i}ª PESSOA | NASC: {lista_nasc[(i-1)]} | IDADE: {lista_idade[(i-1)]}")

print(f"{menor} pessoas são MENORES de idade")
print(f"{maior} pessoas são MAIORES de idade")