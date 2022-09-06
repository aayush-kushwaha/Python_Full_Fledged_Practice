'''
WAP to check whether the given collection is a set or not. If it is a set add a
new value 1000 to the existing set.
'''
def set_checker():
    a = {1,2,3,4,5,6,7,8}
    if type(a) == set:
        a.add(1000)
    print(a)
set_checker()