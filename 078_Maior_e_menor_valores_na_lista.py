#078_Maior_e_menor_valores_na_lista.py

print("")
lista = []
maior = menor = 0

for i in range(0, 5):
    lista.append(int(input(f"Número na posição {i}: ")))
    if i == 0:
        maior = menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]

print("")
print(f"Maior valor é: {maior}, nas posições: ", end="")
for i, v in enumerate(lista):
    if v == maior:
        print(f"{i}... ", end="")
print("")
print(f"Menor valor é: {menor}, nas posições: ", end="")
for i, v in enumerate(lista):
    if v == menor:
        print(f"{i}... ", end="")
print("")
print("")
# print(f"Maior: {maior} {max(lista)} {sorted(lista)[-1]}")
# print(f"Menor: {menor} {min(lista)} {sorted(lista)[0]}")