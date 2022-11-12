def dibujar(L):
    dibujo = list()
    for i in range(L):
        str1 = []
        if i != L//2:
            str1 = ['0']*L
            str1[i] = '#'
            str1[-1*i-1] = '#'
            str1[L//2] = '+'
            dibujo.append(str1)
        else:
            str1 = ['+']*L
            str1[L//2] = '#'
            dibujo.append(str1)

    return dibujo
        


n = int(input())

for i in range(n):
    L = int(input())
    dibujo_real = dibujar(L)
    dibujo_usuario = list()
    for i in range(L):
        dibujo_usuario.append(list(input()))

    if dibujo_usuario == dibujo_real:
        print('Bandera britanica')
    else:
        print('Ni idea')