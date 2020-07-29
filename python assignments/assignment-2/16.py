"""i have hard-coded the list as i assumed that the question wants to test the skill of merge sort
and not taking input and output"""
lst=[14,46,43,27,57,41,45,21,70]
def merge_sort(lst):
    x=len(lst)
    if x <= 1:
        return lst
    mid=x//2
    left,right=merge_sort(lst[:mid]),merge_sort(lst[mid:])
    return merge(left,right)
def merge(left,right):
    res=[]
    lp=rp=0
    while lp < len(left) and rp < len(right):
        if left[lp] <= right[rp]:
            res.append(left[lp])
            lp+=1
        else:
            res.append(right[rp])
            rp+=1
    res.extend(left[lp:])
    res.extend(right[rp:])
    return res
print(merge_sort(lst))