#104_Validando_entrada_de_dados.py

def leiaInt(msg):
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            return int(n)
            ok = True
        else:
            print("[ERRO] Digite um número inteiro válido")
        if ok:
            break


#PROGRAMA PRINCIPAL
n = leiaInt("Digite um número: ")
print(f"Voce digitou o número {n}")