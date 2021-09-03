#049_Tabuada_v2.py

num = int(input("Entre com um número: "))

for i in range(0, 11):
    print(f"{i:>2} x {num:>2} = {(num * i):>3}")