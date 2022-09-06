'''
WAP to print all the odd numbers given in a homogeneous list.
#input l = [10,20,30,1,2,3,9,7,6]
'''
def odd_no_from_list_printer():
    l = [10,20,30,1,2,3,9,7,6]
    for i in l:
        if i % 2 != 0:
            print(i)
odd_no_from_list_printer()