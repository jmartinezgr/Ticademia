def hyperpar(n):
    for num in n:
        if int(num)%2 !=0:
            return 'No es hyperpar'

    return 'Hyperpar'

while True:
    n = input()    
    if n != '-1':
        print(hyperpar(list(n)))
    else:
        break