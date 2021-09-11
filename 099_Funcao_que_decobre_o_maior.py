#099_Funcao_que_decobre_o_maior.py

def maior(*n):
    m = 0
    for i in range(0,len(n)):
        if i == 0:
            m = n[i]
        else:
            if n[i] > m:
                m = n[i]
    print(m)

#Programa Principal
maior(2, 9, 4, 7, -1)
maior(0, 7, 4)
maior(-9, -4, -5)
maior(0)
maior()