logins = []
passwords = []
names = []
string = []
indexes = []
s = input()
while s != '':
    string.append(s)
    s = input()
for i in range(0, len(string)):
    logins.append(string[i].split(':')[0])
    passwords.append(string[i].split(':')[1])
    names.append(string[i].split(':')[4].split(',')[0])
bad_passwords = input()
bad_passwords = bad_passwords.split(';')
for i in range(0, len(passwords)):
    if passwords[i] in bad_passwords:
        indexes.append(i)
if indexes:
    for i in indexes:
        print('To:', logins[i])
        print(names[i] + ',', 'ваш пароль слишком простой, смените его!')
