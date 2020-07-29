s=[]
x=''
while x!= 'q':
    x=input('enter the list item,press q when done: ')
    if x != 'q':
        s.append(int(x))
    else:
        break
print(s)
print('Maximum value: ',max(s),' ','Minimum value: ',min(s))