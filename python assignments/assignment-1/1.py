s=input()
if len(s)<2:
    exit(1)
s1=s[:2]+s[(len(s)-2):]
print(s1)