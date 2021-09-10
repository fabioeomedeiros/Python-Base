#092_Cadastro_de_trabalhador.py

from datetime import date

ano = date.today().year
pessoa = {}

print("")
pessoa['nome'] = str(input("Nome: "))
pessoa['idade'] = (ano - int(input("Ano de nascimento: ")))
pessoa['ctpj'] = int(input("Carteira de trabalho: "))
if pessoa['ctpj'] != 0:
    pessoa['anoc'] = int(input("Ano de contratação: "))
    pessoa['salario'] = float(input("Salário R$"))

print("")
for k, v in pessoa.items():
    if k == 'idade':
        print(f"{k}: {v} anos")
    if k == 'salario':
        print(f"{k}: R${v:.2f}")
    print(f"{k}: {v}")

print("")