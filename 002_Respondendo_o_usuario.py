# 002_Respondendo_o_usuário.py
# Recebe dados do usuário, armazena em variáveis e escreve na tela com formatado de formas direfentes

nome = str(input("Nome: "))
idade = int(input("Idade (anos): "))
altura = float(input("Altura (metros): "))

print(nome, "tem", idade, "anos de idade e", altura, "metros de altura.")
print("%s tem %d anos de idade e %f metros de altura." % (nome, idade, altura))
print("{} tem {} anos de idade e {} metros de altura.".format(nome, idade, altura))
print(f"{nome} tem {idade} anos de idade e {altura} metros de altura.")
