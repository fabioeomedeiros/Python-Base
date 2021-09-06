#067_Tabuada_v3.py

while True:
    n = int(input("Entre com um número: "))
    if n != 0:
        for i in range(0, 11):
            print(f"{i} x {n} = {i*n}")
    else:
        break

print("Fim do programa")