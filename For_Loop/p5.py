'''
WAP to count the length of the collection without using len() function.
#input l = [10,20,30,1,2,3,9,7,6]
'''
def length_col():
    l = [10,20,30,1,2,3,9,7,6]
    count = 0
    for i in l:
        count += 1
    print("The total count is:",count)
length_col()