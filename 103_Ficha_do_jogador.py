#103_Ficha_do_jogador.py

def ficha(nome="<desconhecido>", gols=0):
    print("Cadastro de Jogador")
    nome = str(input("Nome: "))
    gols = str(input("Quantidade de gols: "))
    if nome == "":
        nome = "<desconhecido>"
    if gols == "":
        gols = "0"
    print(f"{nome} fez {gols} gol(s)")

print(ficha())