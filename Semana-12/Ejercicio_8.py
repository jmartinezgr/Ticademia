for case in range(int(input())):
    jumps = {}
    for jump in range(int(input())):
        data = input().split(" ")
        jumps[data[0]] = data[1]

    ans = 0
    now = "C-137"
    for move in range(len(jumps)):
        if (jumps.get(now) == "C-137"):
            ans = move+1
            break
        else:
            now = jumps.get(now)

    print(f"Pueden volver a C-137 en {ans} saltos" if ans > 0 else "Deambulan por el multiverso")
