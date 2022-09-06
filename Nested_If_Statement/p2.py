'''
WAP to check whether the first character of a string is special character 
only if the given collection is even lengthed string.
'''
#Using Inbuilt Function
def first_char_checker(a):
    if len(a) % 2 == 0:
        if a[0].isalnum():
            return "It is not Special Character"
        else:
            return "It is Special Character"
    else:
        return "It is not even lengthed string."
print(first_char_checker(input("Enter a String: ")))

#-----------------------------------------------------------------------------#

#Without Inbuilt Function
def first_char_checker2(a):
    if len(a) % 2 == 0:
        if "A" <= a[0] <= "z" or "0" <= a[0] <= "9":
            return "It is not Special Character"
        else:
            return "It is Special Character"
    else:
        return "It is not even lengthed string"
print(first_char_checker2(input("Enter a String: ")))
