n = int(input())
dic_traducciones = dict()

for i in range(n):
    string = input().split()
    dic_traducciones[string[0]] = string[1]

l = int(input())

for i in range(l):
    palabra = input()
    try:
        print(dic_traducciones[palabra])
    except:
        print('palabra no encontrada')