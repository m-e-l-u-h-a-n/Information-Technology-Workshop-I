file1=open('textfile1.txt','r').readlines()
file2=open('textfile2.txt','r').readlines()
for i,j in zip(file1,file2):
    print(i,j,end='')