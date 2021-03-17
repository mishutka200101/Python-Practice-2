count_of_positions = int(input())
positions = []
count = []
for i in range(0, count_of_positions):
    positions.append(input())
    count.append(int(input()))
positions.reverse()
count.reverse()
for i in range(0, count_of_positions):
    print(positions[i], count[i])
