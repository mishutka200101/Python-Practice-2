word = list(input())
while len(word) != 1 and len(word) != 2:
    word.pop(0)
    word.pop(-1)
    print(''.join(word))
