#058_Jogo_da_adivinhacao_v2.py

from random import randint

comp = randint(1,10)

print("Sou seu computador")
print("Acabei de pensar em um número")
print("Voce consegue adivinhar?")

jog = int(input("Qual é o seu palpite? "))
cont = 0
acertou = False
while (not acertou):
    cont += 1
    if (jog == comp):
        print(f"Você acertou com {cont} tentativas")
        acertou = True
    elif (jog < comp):
        jog = int(input("Errou, tente pra mais: "))
    elif (jog > comp):
        jog = int(input("Errou, tente pra menos: "))