#036_Aprovando_emprestimo.py

print()
v_casa = float(input("Valor do imóvel: R$"))
sal = float(input("Salário do comprador: R$"))
anos = int(input("Total de anos: "))
print(f"Total de parcelas: {anos * 12}")
print(f"Valor das parcelas R${(v_casa / (anos * 12)):.2f}")
print()
if ((v_casa / (anos * 12)) > (sal * 0.3)):
    print("Empréstimo negado")
else:
    print("Emprestimo aprovado")
print()