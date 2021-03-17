n = int(input())
result = ''
for i in range(0, n):
    word = input()
    new_word = list(word)
    if new_word[0] == '%' and new_word[1] == '%':
        new_word.pop(0) and new_word.pop(0)
    elif new_word[0] == '#' and new_word[1] == '#' and new_word[2] == '#' and new_word[3] == '#':
        new_word = ''
    if str(new_word) != '':
        result += ''.join(new_word) + '\n'
print(result)
