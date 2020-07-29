x=[[10,20],[40],[30,56,25],[10,20],[33],[40]]
y=[]
max=0
for i in x:
    if sum(i,0)>max:
        y=i
        #print('hi')
        max=sum(i)
print(y)