'''
WAP to check whether the given string is having an upper case character as a
starting value or not. If the starting value is in uppercase print the string as it
is else convert the string into upper case and print the string.(If it is a special
character or number then print error.) #without using inbuilt function and inbuilt function.
'''

def Upper_char():
    a = input("Enter a string: ")
    if 'A' <= a[0] <= 'z':
        if 'A' <= a[0] <= 'Z':
            print(a)
        else:
            a = a.upper()
            print(a)
    else:
        print("It is Special Character or Number!!!")
Upper_char()