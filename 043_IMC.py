#043_IMC.py

altura = float(input("Altura (cm): "))/100
massa = float(input("Massa (kg): "))
imc = massa / altura**2

if (0 < imc <= 18.5):
    print(f"IMC: {imc:.1f} -> Abaixo do peso")
elif (19 < imc <= 25):
    print(f"IMC: {imc:.1f} -> Peso ideal")
elif (25 < imc <= 30):
    print(f"IMC: {imc:.1f} -> Sobre peso")
elif (30 < imc <= 40):
    print(f"IMC: {imc:.1f} -> Obesidade")
else:
    print(f"IMC: {imc:.1f} -> Obesidade móbida")
