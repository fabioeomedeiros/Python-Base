#069_Analise_de_dados_do_grupo.py

qtdm = qtdh = qtdm20 = 0
esc = " "

while True:

    idade = int(input("Idade: "))
    
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo: ")).strip().upper()[0]
        
    if idade >= 18:
        qtdm += 1

    if sexo == "M":
        qtdh += 1

    if sexo == "F" and idade < 20:
        qtdm20 += 1
    
    esc = " "
    while esc not in "SN":
        esc = str(input("Desja cadastrar uma pessoa? [s/n]? ")).strip().upper()[0]
    
    if esc == "N":
        break

print(f"{qtdm} pessoas são maiores de idade")
print(f"{qtdh} homens foram cadastrados")
print(f"{qtdm20} mulheres tem menos de 20 anos")