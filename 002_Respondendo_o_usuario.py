# 002_Respondendo_o_usuário.py
# Recebe dados do usuário, armazena em variáveis e escreve na tela com formatado de formas direfentes

print("")
nome = str(input("Nome: "))
idade = int(input("Idade (anos): "))
altura = float(input("Altura (metros): "))
print("")

print("1º forma:")
print(nome, "tem", idade, "anos de idade e", altura, "metros de altura.")
print("")

print("2º forma:")
print("%s tem %d anos de idade e %.2f metros de altura." % (nome, idade, altura))
print("")

print("3º forma:")
print("{} tem {} anos de idade e {:.2f} metros de altura.".format(nome, idade, altura))
print("")

print("4º forma:")
print(f"{nome} tem {idade} anos de idade e {altura:.2f} metros de altura.")
print("")
