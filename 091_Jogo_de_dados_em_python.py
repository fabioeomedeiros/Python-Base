#091_Jogo_de_dados_em_python.py

from time import sleep
from random import randint
from operator import itemgetter

print("")
jogo = {'j1':randint(1,6), 
        'j2':randint(1,6),
        'j3':randint(1,6),
        'j4':randint(1,6),
        'j5':randint(1,6),
        'j6':randint(1,6),
        'j7':randint(1,6)}

print("Valores Sorteados")
# print(jogo)
sleep(1)
for k, v in jogo.items():
    print(f"{k} = {v}")
    sleep(.5)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print("")
# print(ranking)
print("Ranking")
sleep(1)
for i, v in enumerate(ranking):
    print(f"{i+1}º - {v[0]} = {v[1]}")
    sleep(.5)
print("")
