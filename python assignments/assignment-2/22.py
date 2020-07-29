import random
import string
for i in range(3):
    r= ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(11)])
    print(i+1,' random string ',r)