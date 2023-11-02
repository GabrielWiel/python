vegetablefruits_to_growth_habit = {
    "carrot": "in the ground",
    "potato": "in the ground",
    "tomato": "on a plant",
    "cucumber": "on a plant",
    "lettuce": "in the ground",
    "broccoli": "in the ground",
    "spinach": "in the ground",
    "onion": "in the ground",
    "garlic": "in the ground",
    "pepper": "on a plant",
    "zucchini": "on a plant",
    "cabbage": "in the ground",
    "asparagus": "in the ground",
    "eggplant": "on a plant",
    "sweet potato": "in the ground",
    "cauliflower": "in the ground",
    "celery": "in the ground",
    "kale": "in the ground",
    "corn": "on a plant",
    "peas": "on a plant",
    "green beans": "on a plant",
    "radish": "in the ground",
    "beet": "in the ground",
    "pumpkin": "on a plant",
    "squash": "on a plant",
    "cantaloupe": "on a plant",
    "watermelon": "on a plant",
    "strawberry": "on a plant",
    "blueberry": "on a plant",
    "raspberry": "on a plant",
    "grape": "on a vine",
    "apple": "on a tree",
    "banana": "on a plant",
    "orange": "on a tree",
    "lemon": "on a tree",
    "lime": "on a tree",
    "pear": "on a tree",
    "peach": "on a tree",
    "plum": "on a tree",
    "cherry": "on a tree",
    "kiwi": "on a plant",
    "mango": "on a tree",
    "avocado": "on a tree",
    "pomegranate": "on a tree",
}
user_input = input("Enter a vegetable or fruit: ").lower()

if user_input in vegetablefruits_to_growth_habit:
    category = "vegetable" if user_input in {"carrot", "potato", "tomato", "cucumber", "lettuce", "broccoli", "spinach", "onion", "garlic", "cabbage", "asparagus", "cauliflower", "celery", "kale", "radish", "beet", "corn", "peas", "green beans", "zucchini", "eggplant", "sweet potato"} else "fruit"
    growth_habit = vegetablefruits_to_growth_habit[user_input]
    print(f"{user_input} is a {category} and it grows {growth_habit}.")
else:
    print("Sorry, I don't know about that vegetable or fruit.")
