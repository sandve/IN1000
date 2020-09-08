import random

def f():
    p = ["banana", "apple", "orange", "lemon", "pear"]

    fc = {}

    for i in range(10):
        f = random.choice(p)
        if f in fc:
            fc[f] += 1
        else:
            fc[f] = 1

    return fc


def c():
    answer = input("Would you like to add another fruit? type 'yes': ")
    if answer == "yes":
        return True
    else:
        return False


def s(fc):
    i = []

    m = True
    while m:
        f = input("Which fruit would you like to add to your smoothie? ")

        if f in fc:
            print("OK, I am adding ", f)
            i.append(f)

            if fc[f] == 1:
                fc.pop(f)
            else:
                fc[f] -= 1

        else:
            print("Unfortunately, we do not have that fruit.")

        m = c()

    print("Here is your smoothie with the following fruits: " + str(i))


fc = f()
s(fc)