n = int(input())
s = [([0] * n) for i in range(n)]
for i in range(n):
    for j in range(n):
        s[i][j] = int(input())
m = int(input())
for i in range(m):
    b = int(input())
    a = int(input())
    if s[a][b] >= 8:
        s[a][b] -= 8
    else:
        s[a][b] = 0
    if a > 0:
        if s[a - 1][b] >= 4:
            s[a - 1][b] -= 4
        else:
            s[a - 1][b] = 0
        if b > 0:
            if s[a - 1][b - 1] >= 4:
                s[a - 1][b - 1] -= 4
            else:
                s[a - 1][b - 1] = 0
        if b < (n - 1):
            if s[a - 1][b + 1] >= 4:
                s[a - 1][b + 1] -= 4
            else:
                s[a - 1][b + 1] = 0
    if a < (n - 1):
        if s[a + 1][b] >= 4:
            s[a + 1][b] -= 4
        else:
            s[a + 1][b] = 0
        if b > 0:
            if s[a + 1][b - 1] >= 4:
                s[a + 1][b - 1] -= 4
            else:
                s[a + 1][b - 1] = 0
        if b < (n - 1):
            if s[a + 1][b + 1] >= 4:
                s[a + 1][b + 1] -= 4
            else:
                s[a + 1][b + 1] = 0
    if b > 0:
        if s[a][b - 1] >= 4:
            s[a][b - 1] -= 4
        else:
            s[a][b - 1] = 0
    if b < n - 1:
        if s[a][b + 1] >= 4:
            s[a][b + 1] -= 4
        else:
            s[a][b + 1] = 0
for i in range(n):
    for j in range(n):
        print(s[i][j], end=' ')
    print()
