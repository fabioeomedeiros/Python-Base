# 064_Tratando_varios_valores_v1.py

num = j = soma = 0
num = int(input("Entre com um número: "))
while (num != 9999):
    soma += num
    j += 1
    num = int(input("Entre com um número: "))
print("Fim")
print(f"Você digitou {j} e a soma foi {soma}")