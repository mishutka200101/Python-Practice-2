n = int(input())
q = []
for _ in range(n):
    s = input().split()
    if 'встал' in s[1]:
        q.append(s[0])
    elif s[0] == 'Привет,':
        q.insert(q.index(s[1][:-1])+1, s[2])
    elif s[1] == 'хватит':
        q.remove(s[0][:-1])
print(*q, sep='\n')
