dic_commits =  {
    'true vampires' : 0,
    'early birds' : 0,
    'sunny warmers' : 0,
    'lunch workers' : 0,
    'sunset lovers' : 0,
    'prime timers' : 0
}

for i in range(int(input())):
    commit = input().split()
    hora = int(commit[1].split(':')[0])
    if hora <= 3:
        dic_commits['true vampires'] += 1
    elif hora >=4 and 7 >= hora:
        dic_commits['early birds'] += 1
    elif hora >= 8 and 11 >=hora:
        dic_commits['sunny warmers'] += 1
    elif hora >= 12 and 15 >= hora:
        dic_commits['lunch workers'] +=1
    elif hora >=16 and 19 >=hora:
        dic_commits['sunset lovers'] += 1
    elif hora >= 20 and 23 >= hora:
        dic_commits['prime timers'] += 1

for clave,valor in dic_commits.items():
    print(clave,)