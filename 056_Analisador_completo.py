#056_Analisador_completo.py

l_nome = []
l_idade = []
l_sexo = []

cont = 0
t_idade = 0
idhmv = 0 #idade do homem mais velho
ndhmv = "" #nome do homem mais velho
qtdmmv = 0 #quantidade de mulheres com menos de 20 anos

for i in range(1, 4):
    print("="*50)
    print(f"{i}ª PESSOA:")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
    l_nome.append(nome)
    l_idade.append(idade)
    l_sexo.append(sexo)
    t_idade += idade
    cont += 1
    if (i == 1 and sexo == "M"):
        idhmv = idade
        ndhmv = nome
    if(idade > idhmv and sexo == "M"):
        idhmv = idade
        ndhmv = nome
    if (idade < 20 and sexo == "F"):
        qtdmmv += 1

print("="*50)
print(l_nome)
print(l_idade)
print(l_sexo)
print("="*50)
print(f"A média das idades é {(t_idade / cont):.2f}")
print(f"O homem mais velho tem {idhmv} e se chama {ndhmv}")
print(f"{qtdmmv} mulheres tem menos de 20 anos")
print("="*50)