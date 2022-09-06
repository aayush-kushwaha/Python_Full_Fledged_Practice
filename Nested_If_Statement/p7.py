''' 
WAP to check whether the given collection is having exact middle value or not. 
If it is having an exact middle value print the element present at the middle index.
'''
def mid_value():
    a = input("Enter collection: ")
    if len(a) % 2 != 0:
        mid_value = len(a)//2
        print(a[mid_value])
    else:
        print("It is even lengthed string!!!")
mid_value()