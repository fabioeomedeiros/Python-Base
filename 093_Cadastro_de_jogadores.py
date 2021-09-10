#093_Cadastro_de_jogadores.py

jogador = {}
gols = []
totgols = 0

print("")
jogador['Nome'] = str(input("Nome: "))
jogador['Partidas Jogadas'] = int(input("Quantidades de partidas: "))
for i in range(0,jogador['Partidas Jogadas']):
    g = int(input(f"    Quantidades de gols na {i+1}º partida: "))
    gols.append(g)
    totgols += g
jogador['Gols'] = gols[:]
jogador['Total de Gols'] = totgols # ou sum(gols)
print("")
print(jogador)
print("")
for k, v in jogador.items():
    print(f"{k}: {v}")
print("")
print(f"O jogador {jogador['Nome']} jogou {len(jogador['Gols'])} partidas")
for i, v in enumerate(jogador['Gols']):
    print(f"    -> na {i+1}º partida fez {v} gols")
print(f"    No total de {totgols} gols")
