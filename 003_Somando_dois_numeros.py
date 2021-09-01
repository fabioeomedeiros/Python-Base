# 003_Somando_dois_numeros
# Recebe dois números tipo float do usuário, armazena em variáveis, executa a soma entre eles e exibe na tele formantando o número de casas decimais

print()
n1 = float(input("Entre com o 1º valor: "))
n2 = float(input("Entre com o 2º valor: "))
soma = n1 + n2
print()
print("A soma entre %f e %f é %.2f." %(n1, n2, soma))
print("A soma entre {} e {} é {:.3f}.".format(n1, n2, soma))
print(f"A soma entre {n1} e {n2} é {soma:.2f}.")
print()