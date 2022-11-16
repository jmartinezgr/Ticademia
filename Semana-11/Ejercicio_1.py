from datetime import datetime

for i in range(int(input())):
    string = input().split()
    fecha_inicial = datetime.strptime(string[1],"%Y-%m-%d")
    fecha_final = datetime.strptime(string[2],"%Y-%m-%d")
    diferencia = fecha_final-fecha_inicial
    print(f'{diferencia.days} dias = {diferencia.days*24} horas = {diferencia.days*24*60} minutos = {diferencia.days*24*60*60} segundos')
