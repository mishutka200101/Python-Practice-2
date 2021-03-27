string = input()
string_mass = string.split(' ')
counter = 0
for i in range(0, len(string_mass)):
    counter += len(string_mass[i])
print(counter)
