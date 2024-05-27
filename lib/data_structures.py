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
    names = []
    for food in spicy_foods:
        for key in food:
            if key == "name":
                name = food[key]
                names.append(name)
    return names

def get_spiciest_foods(spicy_foods):
    spiciest_food = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            spiciest_food.append(food)
    return spiciest_food
    

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        food_name = food["name"]
        heat_level = food["heat_level"]
        cuisine = food["cuisine"]
        spice = "🌶" * heat_level
        print(f"{food_name} ({cuisine}) | Heat Level: {spice}")
        

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    spiciest_food = get_spiciest_foods(spicy_foods)
    formatted = print_spicy_foods(spiciest_food)
    return formatted

def get_average_heat_level(spicy_foods):
    heat_levels = []
    for food in spicy_foods:
        heat_level = food["heat_level"]
        heat_levels.append(heat_level)

    sum_heat_levels = sum(heat_levels)
    average_of_heat_levels = sum_heat_levels / len(heat_levels)  
    return int(average_of_heat_levels)

def create_spicy_food(spicy_foods, spicy_food):
    spicy = spicy_foods
    spicy.append(spicy_food)
    return spicy

