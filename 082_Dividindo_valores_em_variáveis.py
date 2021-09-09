#082_Dividindo_valores_em_variáveis.py

lista = []
pares = []
impares = []

while True:
    n = int(input("Digite um numero: "))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    if n % 2 == 1:
        impares.append(n)
    
    resp = " "
    while resp not in "SN":
        resp = str(input("Deseja continuar [S/N]?")).strip().upper()[0]
        if resp == "N":
            break
    
    if resp == "N":
        break

print(f"Lista completa: {lista}")
print(f"Lista de pares: {pares}")
print(f"Lista de impares: {impares}")
