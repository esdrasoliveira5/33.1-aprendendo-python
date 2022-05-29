def bigestName(list):
    biggest = ''
    for name in list:
        if(len(name) > len(biggest)):
            biggest = name

    return biggest


name = bigestName(['aasdas', 'abc', 'abcd', 'abcde', 'ab'])

print(name)
