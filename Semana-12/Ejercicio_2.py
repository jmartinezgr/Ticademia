from datetime import datetime

def format(days,seconds):
    horas = seconds//3600
    seconds -= horas*3600
    minutos = seconds//60
    seconds -= minutos*60

    return f'{days} dias, {horas} horas, {minutos} minutos, {seconds} segundos'

dic = dict()

for i in range(1,int(input())+1):
    letras = input().rstrip()
    dic[f'h{i}'] = datetime.strptime(letras,"%Y-%m-%d %H:%M:%S")

xd = list()

for j in range(1,len(dic)):
    rest = dic[f'h{j+1}']-dic[f'h{j}']
    print(format(rest.days,rest.seconds))
    xd.append(rest)

suma = xd[0]

for l in range(1,len(xd)):
    suma = suma + xd[l]

suma = suma/len(xd)
print()
print(f'Promedio: {format(suma.days,suma.seconds)}')


