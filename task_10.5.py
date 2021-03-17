word = input()
new_word = list(word)
while new_word[0] == 'а' or new_word[0] == 'А':
    word = input()
    new_word = list(word)
