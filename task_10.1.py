word = input()
number = int(input())
new_word = list(word)
if (len(word) >= number) and (number > 0):
    print(new_word[number - 1])
else:
    print('Ошибка')
