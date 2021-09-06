#066_Varios_numeros_com_flag.py

j = soma = 0
while True:
    num = int(input("Entre com um número: "))
    if num == 999:
        break
    j += 1
    soma += num
print(f"A soma dos {j} valores é {soma} e a média é {(soma/j):.2f}")