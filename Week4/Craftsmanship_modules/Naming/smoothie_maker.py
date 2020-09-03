import random

def collect_fruits():
    possible_fruits = ["banana", "apple", "orange", "lemon", "pear"]

    fruit_counts = {}

    for i in range(10):
        fruit = random.choice(possible_fruits)
        if fruit in fruit_counts:
            fruit_counts[fruit] += 1
        else:
            fruit_counts[fruit] = 1

    return fruit_counts


def ask_to_continue():
    answer = input("Would you like to add another fruit? type 'yes': ")
    if answer == "yes":
        return True
    else:
        return False


def make_smoothie(fruit_counts):
    smoothie_ingredients = []

    add_more_fruits = True
    while add_more_fruits:
        desired_fruit = input("Which fruit would you like to add to your smoothie? ")

        if desired_fruit in fruit_counts:
            print("OK, I am adding ", desired_fruit)
            smoothie_ingredients.append(desired_fruit)

            if fruit_counts[desired_fruit] == 1:
                fruit_counts.pop(desired_fruit)
            else:
                fruit_counts[desired_fruit] -= 1

        else:
            print("Unfortunately, we do not have that fruit.")

        add_more_fruits = ask_to_continue()

    print("Here is your smoothie with the following fruits: " + str(smoothie_ingredients))


fruit_counts = collect_fruits()
make_smoothie(fruit_counts)