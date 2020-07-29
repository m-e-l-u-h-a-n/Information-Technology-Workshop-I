"""i have hard-coded the list as i assumed that the question wants to test the skill of bubble sort
and not taking input and output"""
lst=[14,46,43,27,57,41,45,21,70]
x=len(lst)
for i in range(x):
    for j in range(i+1,x):
        if lst[i]>lst[j] :
            lst[i],lst[j]=lst[j],lst[i]
print(lst)