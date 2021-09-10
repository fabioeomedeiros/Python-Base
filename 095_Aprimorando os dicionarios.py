#095_Aprimorando os dicionarios.py

time = []
jogador = {}
gols = []

while True:
    
    print("")
    gols.clear()
    jogador['Nome'] = str(input("Nome: "))
    jogador['Partidas Jogadas'] = int(input("Quantidades de partidas: "))
    for i in range(0,jogador['Partidas Jogadas']): 
        gols.append(int(input(f"    Quantidades de gols na {i+1}º partida: ")))
    jogador['Gols'] = gols[:]
    jogador['Total de Gols'] = sum(gols)

    time.append(jogador.copy())

    esc = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]
    while esc not in "SN":
        print("[ERRO] Responda apenas 'S' ou 'N'")
        esc = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]
    if esc == "N":
        break

for i, v in enumerate(time):
    print(f"{i+1} - {v}")
print("")