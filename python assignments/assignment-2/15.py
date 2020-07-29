"""i have hard-coded the list as i assumed that the question wants to test the skill of selection sort
and not taking input and output"""
lst=[14,46,43,27,57,41,45,21,70]
x=len(lst)
for i in range(x):
    min_pos=i
    for j in range(i+1,x):
        if(lst[min_pos]>lst[j]):
            min_pos=j
    lst[i],lst[min_pos]=lst[min_pos],lst[i]
print(lst)