def organizar(lista, nuevo_elemento):
    tamaño = len(lista)
    for i in range(tamaño):
        if lista[i][1] < nuevo_elemento[1]:
            lista.insert(i,nuevo_elemento)
            break
        elif lista[i][1] == nuevo_elemento[1]:
            if nuevo_elemento[0] > lista[i][0]:
                lista.insert(i,nuevo_elemento)
    
    if len(lista) == tamaño:
        lista.append(nuevo_elemento)

    return lista
        

n = int(input())
top_insalubre = list()

for i in range(n):
    string = input().split(',') 
    imc = round(float(string[1])/(float(string[2])**2),1) 
    if imc >25 and float(string[3])>100 and float(string[4])>150:
        if len(top_insalubre) == 0:
            top_insalubre.append([string[0],imc])
        else:
            top_insalubre = organizar(top_insalubre,[string[0],imc])

cont = 0    

for i in range(len(top_insalubre)):
    cont += 1
    print(f'{cont} {top_insalubre[i][0]} {top_insalubre[i][1]}')

