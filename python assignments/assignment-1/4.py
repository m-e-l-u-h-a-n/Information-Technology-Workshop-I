def func(s1,s2):
    if isinstance(s1,str) and isinstance(s2,str):
        x=int(len(s1)/2)
        s1=s1[:x]+s2+s1[x:]
        return s1
    else:
        print("please pass string type arguments")
        return
s1=input()
s2=input()
s1=func(s1,s2)
print(s1)