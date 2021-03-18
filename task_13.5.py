n = int(input())
teams = []
points = []
winning_teams = []
for i in range(0, n):
    teams.append(input())
    points.append(int(input()))
while len(winning_teams) < n // 2:
    maxx = max(points)
    index = points.index(maxx)
    winning_teams.append(teams[index])
    points.pop(index)
    teams.pop(index)
winning_teams.sort()
teams.sort()
for i in winning_teams:
    print(i)
for i in teams:
    print(i)
