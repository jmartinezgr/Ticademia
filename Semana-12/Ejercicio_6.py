from datetime import datetime 

for i in range(int(input())):
    nombre,x = input().split(',')
    x = int(x)
    dic = dict()
    lista = list()
    for j in range(x):
        dic[j] = datetime.strptime(input().rstrip(),"%Y-%m-%d")
    aux = dic[1] - dic[0]
    for k in range(1,x-1):
        if dic[k+1] - dic[k] == aux:
            pass
        else:
            aux = '0000-00-00'

    if aux != '0000-00-00':
        proximo_ataque = str(dic[x-1]+aux).split()
        print(f'{nombre} ataca cada {aux.days} dias y volvera a hacerlo en {proximo_ataque[0]}')
    else:
        print(f'{nombre} no es asesino(a) serial periodico')
    print()