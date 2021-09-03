#037_Conversor_de_bases.py

print()
num = int(input("Entre com um número: "))
print()
print('''Escolha uma das bases para conversão:
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadeceimal''')
opcao = int(input("--->: "))
if (opcao == 1):
    print(f"DEC{num} = BIN{bin(num)[2:]}")
elif (opcao == 2):
    print(f"DEC{num} = OCT{oct(num)[2:]}")
elif (opcao == 3):
    print(f"DEC{num} = HEX{hex(num)[2:]}")
else:
    print("Opção INVÁLIDA. Tente novamente")
print()