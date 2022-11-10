def funcion_posicion(lista,nuevo_elemento):
    longitud_inicial = len(lista)
    for j in range(len(lista)):
        if int(lista[j][3]) < int(nuevo_elemento[3]):
            lista.insert(j,nuevo_elemento)
            break
        elif int(lista[j][3]) == int(nuevo_elemento[3]):
            if int(lista[j][1]) <= int(nuevo_elemento[1]):
                lista.insert(j,nuevo_elemento)
                break
    
    if longitud_inicial  ==  len(lista):
        lista.append(nuevo_elemento)

    return lista


n = int(input())
lista = list()

for i in range(n):
    string = input().split()
    if string[2] == 'positiva':
        if len(lista) > 0:
            lista = funcion_posicion(lista,string)
        else:
            lista.append(string)

for i in lista:
    print(f'{i[1]} {i[2].upper()} {i[3]}')







