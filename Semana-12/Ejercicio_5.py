with open('discurso.txt','r') as f:
    data = f.readlines()

dic = dict()

for i in data:
    lista = list()
    for j in i.split():
        if j[len(j)-1] not in (':','.','?',';',','):
            palabra = j.lower()
        else:
            palabra = (j[0:len(j)-1].lower())
        
        if len(palabra) > 4 and palabra not in lista:
            lista.append(palabra)
            if dic.get(palabra):
                dic[palabra] += 1
            else:
                dic[palabra] = 1

sortedxd = sorted(dic.keys())

for i in sortedxd:
    print(i,dic[i])