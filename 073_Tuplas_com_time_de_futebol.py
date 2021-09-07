#073_Tuplas_com_time_de_futebol.py

times = ("Atlético-MG", "Palmeiras", "Fortaleza", "Bragantino", "Flamengo", "Corintians", "Atlético-GO", "Athletico-PR", "Ceará", "Cuiaba", "Internacional", "Fluminense", "Santos", "Juventude", "São Paulo", "Bahia", "América-MG", "Sport Recife", "Grêmio", "Chapecoense", "Vasco")

print("")
print("Os Times são:")
# print(f"{times}")
for t in range(0, len(times)):
    print(f"{(t+1):>2}º - {times[t]}")

print("")
print("Os 3 primeiros colocados são:")
# print(f"{times[:3]}")
for t in range(0, 3):
    print(f"{t+1}º - {times[t]}")

print("")
print("Os últimos 5 colocados são:")
# print(times[-1:-6:-1])
for t in range(-1, -6, -1):
    print(f"{len(times) + t +1}º - {times[t]}")

print("")
print("Os times em ordem alfabética são:")
# print(sorted(times))
for t in range(0,len(times)):
    print(f"{(t+1):>2} - {sorted(times)[t]}")

print("")
time = str(input("Qual time deseja pesquisar? "))

while time not in times:
    print("Tente novamente")
    time = str(input("Qual time deseja pesquisar? "))

print(f"O {time} está na {times.index(time)+1}º posição.")
print("")