#087_Matriz_v2.py

matriz = [[0, 0, 0], [0, 0, 0,], [0, 0, 0]]
sp = st = m = 0

print("")
for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = int(input(f"Digite um número: [{i}, {j}] "))

print("")
print(matriz)
print("")
for i in range(0,3):
    st += matriz[i][2]
    for j in range(0,3):
        print(f"[{matriz[i][j]:^5}]",end="")
        if matriz[i][j] % 2 == 0:
            sp += matriz[i][j]
        
    print("")
print("")

# a) feito separadamente
# sp = 0
# for i in range(0,3):
#     for j in range(0,3):
#         if matriz[i][j] % 2 == 0:
#             sp += matriz[i][j]

# b) feito separadamente 
# st = 0
# for i in range(0,3):
#     st += matriz[i][2]

for j in range(0,3):
    if matriz[1][j] > m:
        m = matriz[1][j]


print(f"a) A soma dos valores pares é {sp}.")
print(f"b) A soma dos valores da 3ª coluna é {st}.")
print(f"c) O maior número da 2ª linha é {m}.")
print("")