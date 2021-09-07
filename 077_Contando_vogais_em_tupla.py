#077_Contando_vogais_em_tupla.py

palavras = ("O", "experimento", "é", "o", "juíz", "da", "verdade", "científica")

for p in palavras:
    print(f"\nNa palavra '{p}' temos: ", end="")
    for l in p:
        if l.lower() in "aeiouáéíóúâêîôûãẽĩõũ":
            print(f"'{l.upper()}' ", end="")
print("")
print("")