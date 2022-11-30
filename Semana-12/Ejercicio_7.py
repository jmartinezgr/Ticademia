for case in range(int(input())):
    n = int(input())
    cubo = [list(range(1,n+1)) for i in range(n)]
    moves = input().split(" ")
    for move in moves:
        if move[0] == "F":
            if move[2] == "+":
                cubo[int(move[1])-1] = [cubo[int(move[1])-1][-1]] + cubo[int(move[1])-1][:-1]
            elif move[2] == "-":
                cubo[int(move[1])-1] =  cubo[int(move[1])-1][1:] + [cubo[int(move[1])-1][0]]
        elif move[0] == "C":
            if move[2] == "+":
                aux = cubo[-1][int(move[1])-1]
                for row in range(n):
                    cubo[row][int(move[1])-1], aux = aux, cubo[row][int(move[1])-1]
            elif move[2] == "-":
                aux = cubo[0][int(move[1])-1]
                for row in range(n-1, -1, -1):
                    cubo[row][int(move[1])-1], aux = aux, cubo[row][int(move[1])-1]
    for row in cubo:
        print(''.join([str(i) for i in row]))
    print()
