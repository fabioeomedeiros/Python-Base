#086_Matriz_em_python.py

matriz = [[0, 0, 0], [0, 0, 0,], [0, 0, 0]]

print("")
for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = int(input(f"Digite um número: [{i}, {j}] "))

print("")
print(matriz)
print("")
for i in range(0,3):
    for j in range(0,3):
        print(f"[{matriz[i][j]:^5}]",end="")
    print("")
print("")
