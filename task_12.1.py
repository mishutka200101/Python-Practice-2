count_of_white_words = int(input())
white_words = []
for i in range(0, count_of_white_words):
    white_words.append(input())
count_of_requests = int(input())
good_requests = []
for i in range(0, count_of_requests):
    word = input()
    if word in white_words:
        good_requests.append(word)
for i in range(0, len(good_requests)):
    print(good_requests[i])
