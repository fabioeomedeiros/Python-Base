#059_Menu_de_opcoes.py

n1 = float(input("1º Número: "))
n2 = float(input("2º Número: "))
op = 0
while (op != 5):
    print("[ 1 ] Somar")
    print("[ 2 ] Multiplicar")
    print("[ 3 ] Maior")
    print("[ 4 ] Novos números")
    print("[ 5 ] Finalizar")
    op = int(input("----> "))

    if (op == 1):
        print(n1 + n2)
    elif (op == 2):
        print(n1 * n2)
    elif (op == 3):
        if (n1 > n2):
            print(f"{n1} é o maior")
        if (n2 > n1):
            print(f"{n2} é o maior")
        else:
            print("Os valores são iguais")
    elif (op == 4):
        n1 = float(input("1º Número: "))
        n2 = float(input("2º Número: "))
    elif (op == 5):
        print("Finalizando")
    else:
        print("Opção inválida")