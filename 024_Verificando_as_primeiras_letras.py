# 024_Verificando_as_primeiras_letras.py
# Verifica se o nome da cidade tem santo no nome

print()
cidade = str(input("Digite sua cidade: ")).strip().lower()
if "santo" in cidade:
    print("Sua cidade tem Santo no nome")
else:
    print("Sua cidade não tem Santo no nome")
print()
