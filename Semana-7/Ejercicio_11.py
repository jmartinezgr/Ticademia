def factorial(n):
    if n!=0:
        fact = 1
        for x in range(1,n+1):
            fact *= x
        return fact
    else:
        return 1

for i in range(int(input())):
    x = input()
    sum = 0
    for digit in x:
        sum+=factorial(int(digit))

    print(f'{x} es fuerte' if sum == int(x) else f'{x} no es fuerte' )