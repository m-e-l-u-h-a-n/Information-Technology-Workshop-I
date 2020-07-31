x=''
while x!='q':
    x = input('Enter the string to captalised, or press q to exit the program: ')
    if(x!='q'):
        print(x.upper())
    else:
        exit(1)