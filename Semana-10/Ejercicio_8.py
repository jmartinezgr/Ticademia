def conversion_mes(mes):
    meses = {
        'marzo':3, 
        'abril':4, 
        'mayo':5, 
        'junio':6,
        'julio':7, 
        'agosto':8, 
        'septiembre':9, 
        'octubre':10, 
        'noviembre':11,
        'diciembre':12, 
        'enero':1, 
        'febrero':2
    }
    return meses[mes]

def equivalencia(numero):
    dias={
        6:"sabado", 
        0:"domingo", 
        1:"lunes", 
        2:"martes",
        3:"miercoles",
        4:"jueves",
        5:"viernes"
        }
    
    return dias[numero]

def zeller(d,m,y):
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if m <3:
        y = y-1
    resultado = y + (y//4) - (y//100) + (y//400) + t[m-1] + d
    return equivalencia(resultado%7)

n = int(input())

for i in range(n):
    fecha = input().split('-')
    fecha[1] = conversion_mes(fecha[1])
    print(zeller(int(fecha[0]),fecha[1],int(fecha[2])))
