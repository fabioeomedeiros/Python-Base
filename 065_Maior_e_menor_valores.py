#065_Maior_e_menor_valores.py

j = soma = maior = menor = 0
resp = 'S'

while (resp == "S"):
    n = int(input("Entre com o número: "))
    soma += n
    j += 1
    if j == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input("Deseja continuar [s/n]? ")).strip().upper()[0]

print(f"Quantidade de números: {j}")
print(f"Soma entre eles: {soma}")
print(f"Média: {soma/j}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")
