import random

names_string = input("Give me everybody's names, separated by comma.")

names = names_string.split(",")

print(random.choice(names))
