import random

names_string = input("Give me everybody's names, separated by comma.")

names = names_string.split(",")

# print(random.choice(names)) #

num_items = len(names)

random_choice = random.randint(0, names - 1)

person_who_will_pay = names[random_choice]


# fix this code later do not use random.choice(names)
