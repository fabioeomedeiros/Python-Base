#053_Detector_de_palindromo.py

frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split(" ")
junto = "".join(palavras)
# com fatiamento
inverso = junto[::-1]

# Sem fatiamento
# inverso = ""
# for i in range(len(junto)-1, -1, -1):
#    inverso = inverso + junto[i]

print(junto)
print(inverso)

if (junto == inverso):
    print("É palíndromo")
else:
    print("Não é palíndromo")