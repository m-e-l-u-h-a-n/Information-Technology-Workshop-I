dict1 = {'key1': 1, 'key2': 3, 'key3': 2}
dict2 = {'key1': 1, 'key2': 2}
for (i, j) in set(dict1.items()) & set(dict2.items()):
    print('%s: %s is present in both x and y' % (i, j))
