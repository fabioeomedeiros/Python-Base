#088_Palpites_para_mega_sena.py

from random import randint

jogo = []

print("")
num = int(input("Quantos jogos você quer gerar? "))
print("")
for i in range(0,num):
    while len(jogo) < 6:
        n = randint(1,60)
        if n not in jogo:
            jogo.append(n)
    print(sorted(jogo))
    jogo.clear()
print("")