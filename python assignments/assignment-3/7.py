from collections import Counter
with open('test.txt')as file:
    print(Counter(file.read().split()))