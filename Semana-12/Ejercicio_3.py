def comprobar(string):
    cont = 0
    lista = list('saramago')
    aux = 0
    for i in string.lower():
        if i == lista[0]:
            lista.append(lista.pop(0))
            aux += 1
            if aux == 8:
                cont+=1
                aux=0

    return cont


with open('cameos.txt','r') as f:
    data = f.readlines()

for i in data:
    print(comprobar(i))
