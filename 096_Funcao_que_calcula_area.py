#096_Funcao_que_calcula_area.py

def area(l, c):
    print("-" * 30)
    print(f"{'Controle de terreno':^30}")
    print("-" * 30)
    A = l * c
    print(f"{l}m x {c}m = {A}m2")
    print("-" * 30)

x = int(input("Largura: "))
y = int(input("Comprimento: "))
area(x, y)
