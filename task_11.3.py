word = input()
n = int(input())
favourite_letter = input()
new_word = list(word)
if n > len(word) or n <= 0 or len(favourite_letter) > 1:
    print('Ошибка')
else:
    if favourite_letter == new_word[n-1]:
        print('Да')
    else:
        print('Нет')
