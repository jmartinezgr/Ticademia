lista_modulos = [9, 11, 12, 8, 12, 9, 11, 8, 11, 10, 9, 10] 

n = int(input())
dic = {}
suma = 0 

for i in range(n):
    suma = 0
    string = input().split(',')
    string = list(map(lambda x: int(x),string))
    for j in range(1,13):
        suma += round(string[j]/lista_modulos[j-1]*5,1)
        string[j] = round(string[j]/lista_modulos[j-1]*5,1)
    
    nota = round(suma/12,1)
    dic[string[0]] = nota

for i in range(0,n):
    minimo = min(dic.keys())
    print(f'{minimo} {dic[minimo]}')
    dic.pop(minimo)
  


