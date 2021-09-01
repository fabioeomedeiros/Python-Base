# 008_Conversor_de_medidas.py
# Recebe uma medida em metros do usuário de converte em várias unidades formatadas

print()
medida = float(input("Entre com uma medida (m): "))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print()
print(f"{medida} m = {km:>10.4f} km")
print(f"{medida} m = {hm:>10.4f} hm")
print(f"{medida} m = {dam:>10.4f} dam")
print(f"{medida} m = {dm:>10.4f} dm")
print(f"{medida} m = {cm:>10.4f} cm")
print(f"{medida} m = {mm:>10.4f} mm")
print()
