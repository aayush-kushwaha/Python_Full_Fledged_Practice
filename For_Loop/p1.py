'''
WAP to print all the uppercase characters present in a given string.
#input s= 'pRogRAMmInG'
'''
def uppercase_char_printer():
    s = 'pRogRAMmInG'
    for i in s:
        if "A" <= i <= "Z":
            print(i)
        else:
            pass
uppercase_char_printer()