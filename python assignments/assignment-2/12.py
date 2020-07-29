def list_sum(lst):
    s=0
    for i in lst:
        if isinstance(i,list):
            s+=list_sum(i)
        else:
            s+=i
    return s
lst=[1,2,[3,4,[7,8,9]],5,6]
print(list_sum(lst))