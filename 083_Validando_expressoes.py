#083_Validando_expressoes.py

expr = str(input("Digite a expressão: "))

pilha = []

for s in expr:
    if s == "(":
        pilha.append("(")
    elif s == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break

if len(pilha) == 0:
    print("Sua expressão está válida!")
else:
    print("Sua expressão está errada!")
