s=input()
res={i : s.count(i) for i in s}
for key,value in res.items():
    print(key," ",value)