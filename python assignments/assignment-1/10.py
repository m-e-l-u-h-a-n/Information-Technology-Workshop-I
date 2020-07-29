def count(s):
    if isinstance(s,str):
        u=0
        l=0
        for i in s:
            if ord(i)>=97 and ord(i)<=122:
                l+=1
            elif ord(i)>=65 and ord(i)<=90:
                u+=1
        return u,l
    else:
        print('pass string as the argument')
        return
s=input()
t=count(s)
print('no.of uppercase letters: ',t[0])
print('no.of lowercase letters: ',t[1])