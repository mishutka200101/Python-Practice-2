n = int(input())
recipes = []
for i in range(0, n):
    recipe = input()
    if 'Лук' not in recipe and 'лук' not in recipe:
        recipes.append(recipe)
print(', '.join(recipes))
