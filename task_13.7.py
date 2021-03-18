n = int(input())
mans = []
for i in range(0, n):
    mans.append(input())
k = int(input())
counter = 0
print(mans[0])
for i in range(0, n - 1):
    print(mans[k % n])
    k += 3
