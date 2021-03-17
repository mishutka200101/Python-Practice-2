recipes_count = int(input())
recipes = []
for i in range(0, recipes_count):
    recipes.append(input())
days = int(input())
old_recipes = []
for i in range(0, days):
    old_recipes_count = int(input())
    for j in range(0, old_recipes_count):
        old_recipes.append(input())
        if old_recipes[j] in recipes:
            recipes.remove(old_recipes[j])
    old_recipes = []
for i in range(0, len(recipes)):
    print(recipes[i])
