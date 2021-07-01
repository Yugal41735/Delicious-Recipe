recipes = {}
current_ingredients = ['chicken', 'butter', 'milk', 'bread', 'cheese']

# example file line: grilled_cheese butter bread cheese

with open("recipes.txt", 'r') as f:
    for line in f:
        words = line.split()
        if words:
            recipes[words[0]] = words[1:]

for recipe, ingredients in recipes.items():
    for ingredient in ingredients:
        if ingredient not in current_ingredients:
            break
    else:
        print('You have the ingredients to make: {}'.format(recipe))