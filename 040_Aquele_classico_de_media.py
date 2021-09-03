#040_Aquele_classico_de_media.py

n1 = float(input("1º nota: "))
n2 = float(input("2ª nota: "))
n3 = float(input("3ª nota: "))
m1 = (n1 + n2 + n3) / 3
if (0 < m1 < 4):
    print(f"A média é {m1:.2f} e o aluno está REPROVADO")
elif (4 <= m1 < 7):
    print(f"A média é {m1:.2f} e o aluno deverá fazer a PROVA FINAL")
    nf = float(input("Nota Final: "))
    m2 = (m1 + nf) / 2
    if (m2 < 5):
        print(f"A média final foi {m2:.2f} e o aluno está REPROVADO")
    else: 
        print (f"A média final foi {m2:.2f} e o aluno está APROVADO")
else:
    print(f"A média é {m1:.2f} é o aluno está APROVADO")
