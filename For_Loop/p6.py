'''
WAP to count the number of space character present in a given string.
#input st = 'east or west python is the best'
'''
def space_counter():
    st = 'east or west python is the best'
    count = 0
    for i in st:
        if i == ' ':
            count += 1
    print("The total space is:",count)
space_counter()