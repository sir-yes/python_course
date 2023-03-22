import random

names_string = input("Give me the names separated by a comma.")
names = names_string.split(",")

random_number = random.randint(0,len(names)-1)

who = names[random_number]

print(f"{who} is going to buy the meal today")


