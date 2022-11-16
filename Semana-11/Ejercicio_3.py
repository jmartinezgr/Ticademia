import random

for i in range(int(input())):
    maquina = int(input().split()[1])
    suma = random.randint(1,6) + random.randint(1,6)
    if suma == maquina:
        print('Empate')
    elif suma > maquina:
        print('Gana el humano')
    else:
        print('Gana la plataforma')