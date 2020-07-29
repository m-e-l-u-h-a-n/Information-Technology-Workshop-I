s=input()
for i in range(1,len(s)-1):
    if s[i]==s[0]:
        s=s[:i]+'$'+s[i+1:]
if s[len(s)-1]==s[0]:
    s=s[:len(s)-1]+'$'
print(s)