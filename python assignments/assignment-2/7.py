lst=[1,2,3,(1,2,3),5,2,46]
c=0
for i in range(len(lst)-1):
    if(isinstance(lst[i+1],tuple)):
        break
    else:
        c+=1
print(c+1)  #because the element just before the tuple element will be skipped as loop will be broken so c+1