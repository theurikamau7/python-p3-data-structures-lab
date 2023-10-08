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
new_spicy_food = {
    "name": "Hot Salsa",
    "cuisine": "Mexican",
    "heat_level": 7,
}


def get_names(spicy_foods):
   return [food["name"] for food in spicy_foods]

names = get_names(spicy_foods)
print(names)


def get_spiciest_foods(spicy_foods):
   spiciest_foods=[]

   for food in spicy_foods:
        if food["heat_level"] > 5: 
          spiciest_foods.append(food)
   return spiciest_foods
spiciest_foods = get_spiciest_foods(spicy_foods)
print(spiciest_foods)


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = "🌶" * food["heat_level"]
        print_spicy_foods(spicy_foods)
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None  # Return None if there is no cuisine
american_food = get_spicy_food_by_cuisine(spicy_foods, "American")
print(american_food) 


def print_spiciest_foods(spicy_foods):
    spiciest_food = [
        food for food in spicy_foods if food.get("heat_level") > 5]
    print_spicy_foods(spiciest_food)

def print_spicy_foods(food_list):
    for food in food_list:
        heat_level = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")


def get_average_heat_level(spicy_foods):
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    num_foods = len(spicy_foods)
    if num_foods == 0:
        return 0  
    average = total_heat / num_foods
    return int(average)
average = get_average_heat_level(spicy_foods)
print(average)


def create_spicy_food(spicy_foods, new_spicy_food):
   

    spicy_foods.append(new_spicy_food)
    return spicy_foods
updated_spicy_foods = create_spicy_food(spicy_foods, new_spicy_food)
print(updated_spicy_foods)