s=input()
x1=s.find('not')
x2=s.find('poor')
"""because according to example given 
for the question (if poor is followed by not) so third condition is applied"""
if x1>0 and x2>0 and x1<x2:
    s=s[:x1]+'good'+s[x2+4:]
print(s)