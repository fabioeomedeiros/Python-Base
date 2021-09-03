#057_Validacao_de_dados.py

sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
while (sexo not in "MF"):
    print("Informe seu sexo corretamente")
    sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]

print(sexo)