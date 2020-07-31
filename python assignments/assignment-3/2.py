from itertools import islice
def read_n_lines(file,n):
    with open(file) as f:
        for line in islice(f, n):
            print(line,end='')
read_n_lines('test.txt', 2)