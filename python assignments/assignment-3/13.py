with open('textfile1.txt') as file:
    lines = file.read().splitlines()
    for i in lines:
        print(i.split())