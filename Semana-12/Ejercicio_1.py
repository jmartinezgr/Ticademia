def contar_letras(palabra):
    new = dict()
    for i in list(palabra):
        if i != ' ':
            if new.get(i):
                new[i] += 1
            else:
                new[i] = 1

    return new

for i in range(int(input())):
    words = input().split(':')
    dic1 = contar_letras(words[0])
    dic2 = contar_letras(words[1])

    print('Es anagrama' if dic2 == dic1 else 'No es anagrama')
        

