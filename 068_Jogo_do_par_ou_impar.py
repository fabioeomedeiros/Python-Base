#068_Jogo_do_par_ou_impar.py

from random import randint

v = 0
while True:
    esc = " "
    c = randint(0,5)
    while esc not in "pi":
        esc = str(input("PAR ou ÍMPAR [p/i]? ")).strip().lower()[0]

    j = int(input("Jogue um número (0-5): "))
    print(f"JOGADOR: {j}")
    print(f"COMPUTADOR: {c}")
    print(f"Total: {j + c}")
    print("PAR" if ((j + c) % 2 == 0) else "ÍMPAR")
    if esc == "p":
        if ((j + c) % 2 == 0):
            print("Venceu")
            v += 1
        if((j + c) % 2 == 1):
            print("Perdeu")
            break
    if esc == "i":
        if((j + c) % 2 == 0):
            print("Perdeu")
            break
        if((j + c) % 2 == 1):
            print("Venceu")
            v += 1
print(f"Você venceu {v} vezes consecutivas")
