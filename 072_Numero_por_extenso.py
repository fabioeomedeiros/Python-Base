#072_Numero_por_extenso.py

num = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez")

while True:
    n =  int(input("Digite um número (1 - 10): "))
    while n not in range(0,11):
        print("Tente novamente!")
        n =  int(input("Digite um número entre 0 e 10: "))
    print(f"Voce digitou o número: {num[n]}")
    esc = str(input("Desja continuar [S/N]? ")).strip().upper()[0]
    if esc == "N":
        break


#OUTRO EXEMPLO DE VALIDAÇÃO
# while True:
#     print("Tente novamente!")
#     n =  int(input("Digite um número entre 0 e 10: "))
#     if (0 <= n <= 10):
#         break

