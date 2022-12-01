def fuckerman(m,n):
    if m > 0:
        if n > 0:
            return fuckerman(m-1,fuckerman(m,n-1))
        else:
            return fuckerman(m-1,1)
    else:
        return n+1

for i in range(int(input())):
    m = int(input())
    n = int(input())
    
    print(fuckerman(m,n))