'''
 WAP to get the following outputs
#Output: out = {'I':1, 'AM':2, 'GENIUS':6}
#input: st = ['I', 'AM', 'GENIUS']
'''
def out():
    st = ['I', 'AM', 'GENIUS']
    d = {}
    for i in st:
        count = 0
        if len(i) == 1:
            count += 1
            d[i] = count
        if len(i) > 1:
            for j in i:
                count += 1
                d[i] = count
    print(d)
out()


def out2():
    st = ['I', 'AM', 'GENIUS']
    d = {}
    for i in st:
        d[i] = len(i)
    print(d)
out2()