"""files are opened and then converted tuples using the function file_to_tuple then
they are appended to a list some of dummy files are intentionally empty so that
we can have some empty tuples in our list"""
def file_to_tuple(file):
    data = file.read()
    return tuple(data.split(' '))
lst=[]
with open('test.txt') as file:
    lst.append(file_to_tuple(file))
with open('dummy_emp_file_q5-i.txt') as file:
    lst.append(file_to_tuple(file))
with open('dummy_emp_file_q5-ii.txt') as file:
    lst.append(file_to_tuple(file))
with open('dummy_emp_file_q5-iii.txt') as file:
    lst.append(file_to_tuple(file))
with open('dummy_emp_file_q5-iv.txt') as file:
    lst.append(file_to_tuple(file))
print('List before removing the empty tuples: ')
print(lst)
x=len(lst)-1
while(x>=0):
    if len(lst[x])<=1:
        lst.pop(x)
    x-=1

print('List after removing the empty tuples: ')
print(lst)