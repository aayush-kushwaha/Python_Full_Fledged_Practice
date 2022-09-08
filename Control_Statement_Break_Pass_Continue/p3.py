'''
3. WAP to extract all the integers present at even index in a collection using
continue statement.
#Input: k = ['python', 12.5, 4, 6+3j, 4, 7, 5, True, 10, 'nohtyp']
'''
# Using Yield
def int_extractor():
    k = ['python', 12.5, 4, 6+3j, 4, 7, 5, True, 10, 'nohtyp']
    for i in k:
        if type(i) == int:
            yield i
        else:
            continue
res = int_extractor()
print(list(res))

#Using simple method
def int_extractor2():
    k = ['python', 12.5, 4, 6+3j, 4, 7, 5, True, 10, 'nohtyp']
    l = []
    for i in k:
        if type(i) == int:
            l.append(i)
        else:
            continue
    print(l)
int_extractor2()   
