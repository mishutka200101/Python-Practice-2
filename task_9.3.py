employees_count = int(input())
employees = []
counter = 0
for i in range(0, employees_count):
    employees.append(input())
for i in range(0, employees_count - 1):
    for j in range(i + 1, employees_count):
        if employees[i] == employees[j]:
            counter += 1
counter += 1
print(counter)
