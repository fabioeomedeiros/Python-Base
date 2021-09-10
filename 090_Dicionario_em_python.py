#090_Dicionario_em_python.py

aluno = {}
print("")
aluno['nome'] = str(input("Nome: "))
aluno['n1'] = float(input(f"N1 de {aluno['nome']}: "))
aluno['n2'] = float(input(f"N2 de {aluno['nome']}: "))
aluno['media'] = ((aluno['n1'] + aluno['n2']) / 2)
if aluno['media'] < 4:
    aluno['sit'] = "Reprovado"
elif aluno['media'] < 7:
    aluno['sit'] = "Prova Final!"
else:
    aluno['sit'] = "Aprovado"
print("")
print(aluno)
print("")
for k, v in aluno.items():
    print(f"{k} = {v}")
print("")