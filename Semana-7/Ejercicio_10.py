def odiomivida(n):
    sum = 0
    for num in range(1,n):
        if n%num == 0:
            sum += num

    return f'{n} es perfecto' if n == sum else f'{n} no es perfecto'

for i in range(int(input())):
    print(odiomivida(int(input())))