def reverse(string):
    s=''
    for i in string:
        s = i+s
    return s
string= input('enter a multiword string: ')
print('before reversing: ',string)
print('after reversing: ',reverse(string))