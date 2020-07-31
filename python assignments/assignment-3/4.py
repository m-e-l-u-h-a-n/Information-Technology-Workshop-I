"""if value of n exceeds the number of lines in the files the program will simply print all the lines"""
file = open('test.txt', 'r')
data = file.readlines()
n = int(input('enter the number of lines to be read: '))
count = 0
for line in open('test.txt').readlines(): count += 1
if n <= count:
    for i in range(count-n,count):
        if len(data[i])>0:
            print(data[i],end='')
else:
    for i in data:
        print(i)