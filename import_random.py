import random

# from random2 import randint

courses = ["math", "science", "history", "art", "physics", "chemistry"]

random_course = random.choice(courses)
print(random_course)
# print(randint(1,2))

help(random.randint())

print("output a random number betwee 1 & 100:", random.randint(1, 100))
