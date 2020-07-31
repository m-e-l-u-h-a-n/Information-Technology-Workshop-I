import random
with open('test.txt') as file:
    lines=file.read().splitlines()
    print(random.choice(lines))