def triangular_superior(width,mx):
    aux = False
    cont = 1
    for k in range(width-1):    
        for i in range(cont,width):
            #print(mx[k][i])
            if mx[k][i] != '0' and mx[k][i] != '0.0':
                aux = True
                return aux
        cont+=1
    return aux

def triangular_inferior(width,mx):
    aux = False
    cont = 1
    for k in range(1,width):
        for i in range(0,cont):
            #print(mx[k][i])
            if mx[k][i] != '0' and mx[k][i] != '0.0':
                aux = True
                return aux
        cont+=1
    
    return aux

for i in range(int(input())):
    matriz = list()
    l = int(input())
    for j in range(l):
        matriz.append(input().split())
    if triangular_superior(l,matriz) and triangular_inferior(l,matriz):
        print('Ni diagonal ni triangular')
    elif triangular_inferior(l,matriz) and not triangular_superior(l,matriz):
        print('Triangular inferior')
    elif triangular_superior(l,matriz) and not triangular_inferior(l,matriz):
        print('Triangular superior')
    else:
        print('Diagonal')