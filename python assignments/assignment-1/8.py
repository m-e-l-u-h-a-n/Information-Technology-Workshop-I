def sort_str(lst):
    for i in range(0,len(lst)):
        min_pos=i
        for j in range(i+1,len(lst)):
            if lst[min_pos]>lst[j]:
                min_pos=j
        lst[min_pos],lst[i]=lst[i],lst[min_pos]
    return lst
lst=input().split('-')
print(lst)
print(sort_str((lst)))
