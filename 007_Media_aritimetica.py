# 007_Media_aritimetica.py
# Recebe duas notas de alunos e calcula sua média. Exibe na tela a média e a situação do aluno, entre aprovado e reprovado

print()
n1 = float(input("1ª Nota: "))
n2 = float(input("2ª Nota: "))
media = (n1 + n2)/2
print()
print(f"A média foi {media:.2f}")
if (media >= 6.0):
	print("O aluno está APROVADO")
else:
	print("O aluno está REPROVADO")