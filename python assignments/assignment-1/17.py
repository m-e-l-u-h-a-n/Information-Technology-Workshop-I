x=[[10,20],[40],[30,56,25],[10,20],[33],[40]]
y=[]
[y.append(i) for i in x if i not in y]
x=y
print(x)