#061_Progessao_aritimetica.py

a1 = int(input("Qual o 1º termo? ")) # 1º termo da P.A.
r = int(input("Qual é a razão? ")) # razão da P.A.
n = int(input("Qual é a quantidade de termos?: ")) # Quantidade de termos desejados
an =  a1 + (n - 1)*r # n-éssimo termo da P.A.

print()
print("P.A. = ", end="")
for i in range(a1, an+r, r):
    print(f"{i} -> ", end="")
    
print("Fim")
print()

j = a1
print("P.A. = ", end="")
while (j < an+r):
    print(f"{j} -> ", end="")
    j += r 
    
print("Fim")
print()