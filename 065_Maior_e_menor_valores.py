#065_Maior_e_menor_valores.py

j = soma = 0
resp = 'S'

while (resp == "S"):
    n = int(input("Entre com o número: "))
    soma += n
    j += 1
    resp = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]
print(f"{j}")
print(f"{soma")
print(f"{soma/j}")