'''
WAP to find the sum of all values present in a given homogeneous list using while
loop.
k = [1,2,3,4,5]
'''
def list_summer():
    k = [1,2,3,4,5]
    sum = 0 
    for i in k:
        sum += i
    print(sum)
list_summer()