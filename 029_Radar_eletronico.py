# 029_Radar_eletronico.py
# Resebe um valor de velocidade e calcula a multa se for apropriado
# velocidade máx = 80km/h e multa = R$7,00 por km/h ultrapassado

print()
vel = float(input("Velocidade registrada: "))
print()
if (vel > 80):
    multa = (vel-80)*7
    print(f"Você foi multado em R${multa:.2f}")
else:
    print("Dirija com cuidado!")
print()
