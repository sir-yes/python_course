import random

random_integer = random.randint(1,10)
print(random_integer)

random_float = random.random()
print(random_float)

# Range of random floats
random_float = random.random()
print(random_float * 5)

# Heads or Tails Game
result = random.randint(0,1)
if result == 0:
    print(f"{result} Tails")
else:
    print(f"{result} Heads")