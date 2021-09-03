#042_Analisando_triangulos_v2.py

print("Entre com os lados do triângulo")
l1 = float(input("1º lado: "))
l2 = float(input("2º lado: "))
l3 = float(input("3º lado: "))

if ((l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l1 + l2)):
    print("Forma triangulo: ", end="")
    if (l1 == l2 == l3):
        print("EQUILÁTERO")
    elif ((l1 == l2) or (l2 == l3) or (l1 == l3)):
        print("ISÓCELES")
    else:
        print("ESCALENO")
else:
    print("Não forma triângulo")