#075_Analise_de_dados_em_uma_tupla.py


num = (int(input("Digite o 1º número: ")), int(input("Digite o 1º número: ")), int(input("Digite o 1º número: ")), int(input("Digite o 1º número: ")), int(input("Digite o 1º número: ")))

print(num)
print(f"O valor 9 apareceu {num.count(9)} vezes")
if 3 in num:
    print(f"O valor 3 apareceu na {num.index(3)+1}º posição")
else:
    print("O valor 3 não foi digitado")
print("Os valores: ", end="")
for n in num:
    if n % 2 == 0:
        print(f"{n} ", end="")
print("São pares")
