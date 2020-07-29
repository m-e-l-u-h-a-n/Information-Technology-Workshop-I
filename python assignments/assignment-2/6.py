x=int(input('enter the number of tuples: '))
lst=[]
m=dict()
for i in range(x):
    p=int(input('enter the value: '))
    q=input('enter the key: ')
    lst.append((p,q))
    m[q]=p
print(lst)
print(m)