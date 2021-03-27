ch = input()
str = input()
str_mass = str.split(' ')
for i in range(0, len(str_mass)):
    if ch in str_mass[i]:
        print(str_mass[i])
