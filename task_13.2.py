n = int(input())
numbers = []
for i in range(0, n):
    numbers.append(int(input()))
sorted_numbers = sorted(numbers, reverse=True)
for i in range(0, len(sorted_numbers)):
    print(sorted_numbers[i])
