#106_Sistema_interativo_de_ajuda.py
def ajuda(com):
    help(com)

def titulo(msg):
    tam = len(msg) + 2
    print("=" * tam)
    print(f" {msg}")
    print("=" * tam)

#PROGRAMA PRINCIPAL
comando = ""
while True:
    titulo("SISTEMA DE AJUDA PyHELP", 1)
    comando = str(input("Função ou Biblioteca > "))
    if comando.strip().upper() == "FIM":
        break
    else:
        ajuda(comando)
