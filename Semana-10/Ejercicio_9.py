longitud_r = int(input())
dic_r = dict()
for i in range(longitud_r):
    linea = input().split()
    for j in linea:
        if not(dic_r.get(j)):
            dic_r[j] = True

longitud_rock = int(input())
dic_rock = dict()
for i in range(longitud_rock):
    linea = input().split()
    for j in linea:
        if not(dic_rock.get(j)):
            dic_rock[j] = True

print(f'Reggaeton: {len(dic_r)} Rock: {len(dic_rock)}')