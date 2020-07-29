def insertion_sort(s):
    if(isinstance(s,str)):
        for i in range(0,len(s)):
            min_pos=i
            for j in range(i+1,len(s)):
                if(s[j]<s[min_pos]):
                    min_pos=j
            if min_pos != i:
                s=s[:i]+s[min_pos]+s[i+1:min_pos]+s[i]+s[min_pos+1:]
        return s
    else:
        print('pass a string as a string')
        return
s1=input()
print(insertion_sort(s1))