lst=[]
x=int()
q=''
while q!='q':
    q = input('enter the number in sorted order,press q if you have entered them all: ')
    if q != 'q':
        try:
            d = int(q)
        except:
            print('enter integers only')
            exit(1)
        lst.append(d)
    else:
        break
sorted(lst)#i sorted just to make sure list contains sorted numbers before we begin search
# lst=[3,5,10,12,15,20]
var=int(input('enter the value to be searched: '))
lo=0
hi=len(lst)-1
while(hi>lo):
    mid=int((lo+hi)/2)
    if lst[mid] == var:
        print(var,' found at the index ',mid)
        exit(1)
    elif var<lst[mid]:
        hi=mid-1
    else:
        lo=mid+1
if lst[hi]==var:
    print(var, ' found at the index ', hi)
elif lst[lo]==var:
    print(var, ' found at the index ', lo)
else:
    print(var,'not found in the list')