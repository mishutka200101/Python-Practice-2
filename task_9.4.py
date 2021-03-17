fridge_count = int(input())
fridge_products = []
good_recipes = []
for i in range(0, fridge_count):
    fridge_products.append(input())
recipes = int(input())
recipe_products = []
is_ok = False
for i in range(0, recipes):
    recipe_name = input()
    products_count = int(input())
    for j in range(0, products_count):
        recipe_products.append(input())
        if recipe_products[j] in fridge_products:
            is_ok = True
        else:
            is_ok = False
    if is_ok:
        good_recipes.append(recipe_name)
    is_ok = False
    recipe_products = []
for i in range(0, len(good_recipes)):
    print(good_recipes[i])
