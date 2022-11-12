n = int(input())

lista_cronologica = list()
marcador = dict()

for i in range(n):
    var = input().split(': ')
    if marcador.get(var[0]):
        marcador[var[0]] += int(var[1])
    else:
        marcador[var[0]] = int(var[1])

ganador = list(marcador.keys())[0]

for i in marcador.keys():
    if marcador[ganador] < marcador[i]:
        ganador = i

print(f'El vendedor del mes es {ganador}')

