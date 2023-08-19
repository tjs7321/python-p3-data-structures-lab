spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [i["name"] for i in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    spiciest = [i for i in spicy_foods if i["heat_level"] > 5]
    return spiciest

def print_spicy_foods(spicy_foods):
    for i in spicy_foods:
        print(f"{i['name']} ({i['cuisine']}) | Heat Level: {'🌶'*i['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    new_dict={}
    for i in spicy_foods:
        if i["cuisine"] == cuisine:
            new_dict.update(i)
    return new_dict

def print_spiciest_foods(spicy_foods):
    for i in spicy_foods:
        if i["heat_level"] > 5:
            print(f"{i['name']} ({i['cuisine']}) | Heat Level: {'🌶'*i['heat_level']}")

def get_average_heat_level(spicy_foods):
    list = [i["heat_level"] for i in spicy_foods]
    return sum(list)/len(list)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
