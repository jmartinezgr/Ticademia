for case in range(int(input())):
    input()
    table = []
    for row in range(9):
        table.append(input().split(" "))

    ans = True
    # Check rows
    for row in range(9):
        if len(set(table[row])) < 9:
            ans = False
            break

    # Check cols
    for col in range(9):
        if len(set([table[row][col] for row in range(9)])) < 9:
            ans = False
            break

    conditions = []
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            conditions.append([row,row+2,col,col+2])
    groups = [[] for i in range(9)]
    # Check 3x3
    for row in range(9):
        for col in range(9):
            for condition in range(len(conditions)):
                if row >= conditions[condition][0] and row <= conditions[condition][1] and col >= conditions[condition][2] and col <= conditions[condition][3]:
                    groups[condition].append(table[row][col])

    for group in groups:
        if len(set(group)) < 9:
            ans = False
            break

    print("Resuelto" if ans else "No resuelto")
