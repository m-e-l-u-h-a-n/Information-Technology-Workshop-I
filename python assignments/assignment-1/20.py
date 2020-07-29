def subtract(lst1,lst2):
    x=[]
    [x.append(i) for i in lst1 if i not in lst2]
    return x
lst1=[]
lst2=[]
t=""
while t != '0':
    t=input('enter the elements of first list,press zero to stop filling in this list: ')
    if t=='0':
        break;
    else:
        lst1.append(t)
t=''
while t != '0':
    t=input('enter the elements of second list,press zero to stop filling in this list: ')
    if t=='0':
        break;
    else:
        lst2.append(t)
if  len(lst1)>0 and len(lst2)>0:
    x=int('enter 1 and 2 for list1 - list2: ')
    if x==1:
        print(subtract(lst1,lst2))
    elif x==2:
        print(subtract(lst2, lst1))
    else:
        print('you did not enter the correct option')
else:
    print('none of the list should be empty')