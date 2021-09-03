#041_Classificando_atletas.py

from datetime import date

ano = date.today().year
nasc = int(input("Ano de Nascimento: "))
idade =  ano - nasc

if (idade <= 0):
    print("Você ainda nem nasceu! Tente novamente")
elif (0 < idade <= 9):
    print(f"{idade} anos > calssificação: MIRIM")
elif (9 < idade <= 14):
    print(f"{idade} anos > calssificação: INFANTIL")
elif (14 < idade <= 19):
    print(f"{idade} anos > calssificação: JÚNIOR")
elif (19 < idade <= 25):
    print(f"{idade} anos > calssificação: SÊNIOR")
elif (25 < idade <= 120):
    print(f"{idade} anos > calssificação: MASTER")
else:
    print(f"{idade} > Você já deveria estar morto!")