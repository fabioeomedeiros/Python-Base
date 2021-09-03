#039_Alistamento_militar.py

from datetime import date

ano = date.today().year
nasc = int(input("Ano de nascimento: "))
idade = ano - nasc
if (idade < 18):
    print(f"Você tem {idade} anos e deve se alistar em {nasc + 18}")
elif(idade == 18):
    print(f"Você tem {idade} anos e deve se alistar imediatamente!")
else:
    print(f"Você tem {idade} anos e deveria ter se alistado em {nasc + 18}")