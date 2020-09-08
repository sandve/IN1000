import random

def collect_a_dictionary_of_random_fruits_with_their_frequency_values():
    all_the_possible_fruits_to_choose_from = ["banana", "apple", "orange", "lemon", "pear"]

    fruit_names_and_their_frequency_values = {}

    for count_index in range(10):
        randomly_chosen_fruit = random.choice(all_the_possible_fruits_to_choose_from)
        if randomly_chosen_fruit in fruit_names_and_their_frequency_values:
            fruit_names_and_their_frequency_values[randomly_chosen_fruit] += 1
        else:
            fruit_names_and_their_frequency_values[randomly_chosen_fruit] = 1

    return fruit_names_and_their_frequency_values


def ask_if_the_user_wants_to_continue_adding_fruits():
    whether_the_user_wants_to_add_another_fruit = input("Would you like to add another fruit? type 'yes': ")
    if whether_the_user_wants_to_add_another_fruit == "yes":
        return True
    else:
        return False


def make_smoothie_based_on_fruits_chosen_by_the_user(fruit_names_and_their_frequency_values):
    ingredients_that_the_user_has_chosen_for_their_smoothie = []

    add_more_fruits_to_the_smoothie = True
    while add_more_fruits_to_the_smoothie:
        fruit_that_the_user_wants_to_add_to_the_smoothie = input("Which fruit would you like to add to your smoothie? ")

        if fruit_that_the_user_wants_to_add_to_the_smoothie in fruit_names_and_their_frequency_values:
            print("OK, I am adding ", fruit_that_the_user_wants_to_add_to_the_smoothie)
            ingredients_that_the_user_has_chosen_for_their_smoothie.append(fruit_that_the_user_wants_to_add_to_the_smoothie)

            if fruit_names_and_their_frequency_values[fruit_that_the_user_wants_to_add_to_the_smoothie] == 1:
                fruit_names_and_their_frequency_values.pop(fruit_that_the_user_wants_to_add_to_the_smoothie)
            else:
                fruit_names_and_their_frequency_values[fruit_that_the_user_wants_to_add_to_the_smoothie] -= 1

        else:
            print("Unfortunately, we do not have that fruit.")

        add_more_fruits_to_the_smoothie = ask_if_the_user_wants_to_continue_adding_fruits()

    print("Here is your smoothie with the following fruits: " + str(ingredients_that_the_user_has_chosen_for_their_smoothie))


fruit_names_and_their_frequency_values = collect_a_dictionary_of_random_fruits_with_their_frequency_values()
make_smoothie_based_on_fruits_chosen_by_the_user(fruit_names_and_their_frequency_values)