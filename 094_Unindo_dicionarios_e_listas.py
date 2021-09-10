#094_Unindo_dicionarios_e_listas.py
from datetime import date

pessoa = {} #dicionário de cada pessoa
lista = [] #lista que armazena os dicionários de cada pessoa
mulheres = [] #lista de mulheres cadastradas
idades = [] #lista de idades acima da média
anoatual = date.today().year
totidade = med_idade = 0

while True:
    print("")
    pessoa['nome'] = str(input("Nome: "))
    
    pessoa['sexo'] = str(input("Sexo [M/F]: ")).strip().upper()[0]
    while pessoa['sexo'] not in "MF":
        print("[ERRO] Digite apenas 'M' ou 'F'")
        pessoa['sexo'] = str(input("Sexo [M/F]: ")).strip().upper()[0]
    if pessoa['sexo'] == "F":
        mulheres.append(pessoa['nome'])
    
    pessoa['idade'] = anoatual - int(input("Ano de nascimento: "))
    totidade += pessoa['idade']
    
    esc = str(input("Desja continuar [S/N]? ")).strip().upper()[0]
    while esc not in "SN":
        print("[ERRO] Digite apenas 'S' ou 'N'")
        esc = str(input("Desja continuar [S/N]? ")).strip().upper()[0]
    
    lista.append(pessoa.copy()) #Adiciona as pessoas a lista
    
    if esc == "N":
        break

med_idade = (totidade / len(lista)) #Calcula a média das idades
for i in range(0, len(lista)):
    if lista[i]['idade'] > med_idade:
        idades.append(lista[i]['idade'])

print("")
print(lista)
print("")
print(f"{'NOME':<10}{'IDADE':<6}{'SEXO':<4}")
for i in range(0,len(lista)):
    print(f"{lista[i]['nome']:<10}{lista[i]['idade']:<6}{lista[i]['sexo']:<4}")
print("")
print(f"(a) Foram cadastradas {len(lista)} pessoas")
print(f"(b) A média das idades é: {med_idade:.1f} anos")
print(f"(c) Mulheres cadastradas:")
for i in range(0,len(mulheres)):
    print(f"   {mulheres[i]}")
print(f"(d) Lista das idade superiores a média é:")
for i in range(0, len(idades)):
    print(f"   {idades[i]}")
print("")
