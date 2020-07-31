with open('q8_ans_file.txt','a') as file:
    n=int(input('enter the number of items in the list: '))
    for i in range(0,n):
        x=input('enter list item: ')
        file.write(x+'\n')
with open('q8_ans_file.txt', 'r+') as file:
    print(file.read())
    file.truncate(0)
